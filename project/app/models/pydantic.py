"""
Provide pydantic models.
"""
from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str
