from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import dotenv_values
import os

config = dotenv_values(".env")
os.environ["TAVILY_API_KEY"] = config["TAVILY_API_KEY"]

travily_search = TavilySearchResults()
travily_search.description = "一個針對全面、準確且值得信賴的結果而優化的搜尋引擎。當您需要回答有關時事或是詢問某家公司的股票代碼的問題時很有用。"
