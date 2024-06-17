from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.memory import ConversationBufferWindowMemory
from langchain.schema.runnable import RunnablePassthrough
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents import AgentExecutor
from tools.google_tool import google_finance, google_news
from tools.travily_search import travily_search
from tools.user_portfolio import user_portfolio
from dotenv import load_dotenv, dotenv_values
from util.util import load_prompt_from_md
import os

config = dotenv_values(".env")
os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]

current_path = os.path.dirname(os.path.realpath(__file__))


def conversation_agent():
    tools = [google_finance, google_news, user_portfolio, travily_search]
    functions = [convert_to_openai_function(f) for f in tools]
    model = ChatOpenAI(model_name="gpt-4-turbo", temperature=0).bind(
        functions=functions
    )  # gpt-3.5-turbo-0125

    # customize prompt
    prompt_text = load_prompt_from_md(
        os.path.join(current_path, "util/prompt_template.md")
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", prompt_text),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    memory = ConversationBufferWindowMemory(
        return_messages=True, memory_key="chat_history", k=5
    )

    agent = (
        RunnablePassthrough.assign(
            agent_scratchpad=lambda x: format_to_openai_functions(
                x["intermediate_steps"]
            )
        )
        | prompt
        | model
        | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
    )
    return agent_executor
