import os
from dotenv import load_dotenv, dotenv_values
from langchain_community.tools.google_finance import GoogleFinanceQueryRun
from .wrapper.GoogleFinanceAPIWrapperPrice import GoogleFinanceAPIWrapperPrice
from .wrapper.GoogleFinanceAPIWrapperNews import GoogleFinanceAPIWrapperNews

config = dotenv_values(".env")
os.environ["SERPAPI_API_KEY"] = config["SERPAPI_API_KEY"]

google_finance = GoogleFinanceQueryRun(api_wrapper=GoogleFinanceAPIWrapperPrice())
google_finance.name = "google_finance"
google_finance.description = """工具描述：用於從Google Finance獲取最新股票價格(Price)和股票代碼(Ticker)。輸入應為股票代碼(Ticker)或是公司名稱(Company)
這個工具整合LangChain工具程式，可以根據使用者的請求提供即時股票價格資訊。使用者可以通過詢問這個工具來獲取當前的股票價格、查詢股票信息，或者詢問具體股票的購買情況。
特點：
- 從Google Finance獲取最新股票價格。
- 支持使用股票代碼進行查詢。
- 提供最新的股票價格和相關指標信息。

使用方式：
這個工具專為LangChain Agent程式設計：
- 詢問特定股票的當前價格。
- 通過公司名稱獲取股票代碼，以進行後續的查詢。
- 幫助使用者做出買賣股票的決策。

範例使用:
agent.ask("TSMC")
agent.ask("國泰金")"""

google_news = GoogleFinanceQueryRun(api_wrapper=GoogleFinanceAPIWrapperNews())
google_news.name = "google_news"
google_news.description = """工具描述：用於從Google Finance獲取台灣股票相關的財金新聞及財務報表資訊。
輸入應為股票代碼(Ticker)，可以從google_finance()功能的輸出取得。
這個工具整合LangChain工具程式，可以根據使用者的請求提供即時股票相關新聞及財務報表內容。使用者可以通過詢問這個工具來獲取當前台灣的股票新聞、查詢股票信息，或者詢問具體股票最近情況。

特點：
- 從Google Finance News獲取最新股票新聞與財務報表資訊。
- 僅支持使用股票代碼進行查詢。

使用方式：
這個工具專為LangChain Agent程式設計：
- 詢問特定股票的當前財金新聞及此檔股票表現(財務報表資訊)。
- 通過股票代碼查詢。
- 幫助使用者做出買賣股票的決策。

範例使用:
agent.ask("2330:TPE")
agent.ask("2882:TPE")"""
