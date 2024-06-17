# intelligent-finance-agent


<a name="readme-top"></a>

<!-- 專案簡介 -->
## About The Project

<img src="image/DALL-E_Intelligent_Advisor.png" alt="Logo" width="200" height="200">

An intelligent financial bot built with LangChain. It integrates multiple APIs to provide users with stock analysis, real-time news, and portfolio management insights. By leveraging large language models, offering personalized investment advice based on comprehensive data and sophisticated reasoning.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Installation

- Install Package
   ```sh
   pip install -r requirments.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Additional screenshots, code examples and demos work -->
## Usage

1. Make sure put .env file inside in folder
   ```
   OPENAI_API_KEY=YOUR_OPENAI_TOKEN
   SERPAPI_API_KEY=YOUR_SERPAPI_TOKEN
   TAVILY_API_KEY=YOUR_TAVILY_TOKEN
   ```

    - [Get OPENAI API TOKEN](https://platform.openai.com/docs/quickstart?context=python)
    - [Get SERPAPI API TOKEN](https://serpapi.com/users/sign_up)
    - [Get TAVILY API TOKEN](https://app.tavily.com)

2. Run service locally
   ```
   python3 -m streamlit run chatbot_ui.py 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Demo
- Front Page:
![front-end page1](/image/front-page.png?raw=true "Demo Page 1")

- Analysis Capability:
![analysis-stock page1](/image/analysis-stock.png?raw=true "Demo Page 1")
(Agent thinking process)
  - Invoke tool `google_finance` -> `google_news`
    ![thinking-chain page1](/image/thinking-chain1-1.png?raw=true "Demo Page 1")
    ![thinking-chain page2](/image/thinking-chain1-2.png?raw=true "Demo Page 1")

- Communicate with Internal Data:
![internal-data page1](/image/internal-data.png?raw=true "Demo Page 1")
(Agent thinking process)
  - Invoke tool `google_finance`
    ![thinking-chain page3](/image/thinking-chain2-1.png?raw=true "Demo Page 1")
  - Invoke tool `user_portfolio`
    ![thinking-chain page4](/image/thinking-chain2-2.png?raw=true "Demo Page 1")

<!-- Improved -->
## Further improved

- [ ] Streaming reply

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- 其他相關資訊 -->
## Acknowledgments

* LangChain Agent Doc: [LangChain Official Site](https://python.langchain.com/v0.1/docs/modules/agents/how_to/custom_agent/)
* LangChain Tool List: [LangChain Official Tool List](https://python.langchain.com/v0.1/docs/integrations/tools/)
* Agent Project Reference: [country-compass-ai](https://github.com/nirbar1985/country-compass-ai)