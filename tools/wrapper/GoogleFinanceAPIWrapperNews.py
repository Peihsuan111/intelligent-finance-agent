from typing import cast
from langchain_core.pydantic_v1 import SecretStr
from serpapi import GoogleSearch
from langchain_community.utilities.google_finance import GoogleFinanceAPIWrapper


class GoogleFinanceAPIWrapperNews(GoogleFinanceAPIWrapper):

    def run(self, query: str) -> str:
        """Run query through Google Finance with Serpapi"""
        serpapi_api_key = cast(SecretStr, self.serp_api_key)
        params = {
            "engine": "google_finance",
            "api_key": serpapi_api_key.get_secret_value(),
            "hl": "zh-tw",
            "q": query,
        }

        search = GoogleSearch(params)
        total_results = search.get_dict()

        if not total_results:
            return "Nothing was found from the query: " + query

        # Process news results
        news_results = total_results.get("news_results", [])
        if not news_results:
            return "No news found for query: " + query

        result_summary = "News results:\n"
        for news in news_results:
            snippet = news.get("snippet", "No snippet")
            link = news.get("link", "No link")
            source = news.get("source", "No source")
            result_summary += f"Snippet: {snippet}\nLink: {link}\nSource: {source}\n\n"

        # Process finance report
        report_results = total_results.get("financials", [])
        if not report_results:
            result_summary +=  "No finance report founded"
        
        for section in report_results:
            result_summary += f"{section['title']}:\n"
            for result in section["results"]:
                result_summary += f"日期: {result['date']}\n"
                for table in result["table"]:
                    result_summary += f"- {table['title']}: {table['value']} ({table['change']})\n"
                    result_summary += f"  描述: {table['description']}\n"

        return result_summary



