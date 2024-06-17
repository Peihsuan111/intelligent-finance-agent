from typing import cast
from langchain_core.pydantic_v1 import SecretStr
from serpapi import GoogleSearch
from langchain_community.utilities.google_finance import GoogleFinanceAPIWrapper


class GoogleFinanceAPIWrapperPrice(GoogleFinanceAPIWrapper):

    def run(self, query: str) -> str:
        """Run query through Google Finance with Serpapi"""
        serpapi_api_key = cast(SecretStr, self.serp_api_key)
        params = {
            "engine": "google_finance",
            "hl": "zh-tw",
            "api_key": serpapi_api_key.get_secret_value(),
            "q": query,
        }

        total_results = {}
        client = self.serp_search_engine(params)
        total_results = client.get_dict()

        if not total_results:
            return "Nothing was found from the query: " + query

        markets = total_results.get("markets", {})
        res = "\nQuery: " + query + "\n"

        if "futures_chain" in total_results:
            futures_chain = total_results.get("futures_chain", [])[0]
            stock = futures_chain["stock"]
            price = futures_chain["price"]
            temp = futures_chain["price_movement"]
            percentage = temp["percentage"]
            movement = temp["movement"]
            res += (
                f"stock: {stock}\n"
                + f"price: {price}\n"
                + f"percentage: {percentage}\n"
                + f"movement: {movement}\n"
            )

        else:
            res += "No summary information\n"
            return res

        for key in markets:
            if (key == "us") or (key == "asia") or (key == "europe"):
                res += key
                res += ": price = "
                res += str(markets[key][0]["price"])
                res += ", movement = "
                res += markets[key][0]["price_movement"]["movement"]
                res += "\n"

        return res
