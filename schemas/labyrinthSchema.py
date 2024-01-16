from pydantic import BaseModel
from typing import List

class LabyrinthSchema(BaseModel):
    labyrinth: List[List[int]]
    start_row: int
    start_col: int
    goal_row: int
    goal_col: int