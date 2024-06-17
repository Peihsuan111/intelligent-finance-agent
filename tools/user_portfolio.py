from langchain.tools import tool
from pydantic.v1 import BaseModel, Field, ValidationError
from typing import Dict


class UserModel(BaseModel):
    user_id: str = Field(..., description="User id.")


@tool(args_schema=UserModel)
def user_portfolio(user_id: str) -> Dict[str, int]:
    """回傳使用者現有的投資組合"""
    return {"2882:TPE": 291000, "2301:TPE": 107500, "2603:TPE": 398000}
