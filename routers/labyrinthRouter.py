from fastapi import APIRouter
from Class.Responses import Response
from schemas.labyrinthSchema import LabyrinthSchema
from algorithms.aStarAlgorithm import a_star_algorithm

lab = APIRouter()

def get_answer_route(answer):
    node = answer.father
    coords = []
    while not node.father is None:
        coords.append([node.x, node.y])
        node = node.father
    return coords

@lab.post("/solve-labyrinth/a-star")
async def solve_labyrinth(labyrinth: LabyrinthSchema):
    try:
        answer = a_star_algorithm(labyrinth.labyrinth, (labyrinth.start_col, labyrinth.start_row), (labyrinth.goal_col, labyrinth.goal_row))
        if isinstance(answer, str):
            return Response.error(message=answer)
        else:
            solution = get_answer_route(answer)
            return Response.success(data=solution, message="A route has been found")
    except Exception as e:
        print(e)
        return Response.error()