from fastapi import FastAPI
from mangum import Mangum
from routers.labyrinthRouter import lab
from Class.Responses import Response

app = FastAPI()
app.include_router(lab)
handler = Mangum(app)

@app.get("/")
def read_root():
    return Response.success(message="Connection Successfull")