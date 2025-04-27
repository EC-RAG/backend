from pydantic import BaseModel

from typing import List

class DocSliceResponse(BaseModel):
    title: str
    content: str
    index: int
    embedding: List[float]

class DocResponse(BaseModel):
    title: str
    slice_cnt: int

class DocAddRequest(BaseModel):
    title: str
    document: str

class DocQueryResponse(BaseModel):
    title: str
    content: str
    index: int
    distance: float