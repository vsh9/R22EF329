from pydantic import BaseModel
from typing import List

class output(BaseModel):
    windowPrevState: List[int]
    windowCurrState: List[int]
    numbers: List[int]
    p: int

