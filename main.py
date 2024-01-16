from fastapi import FastAPI
from mangum import Mangum
from routers.labyrinthRouter import lab
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(lab)
handler = Mangum(app)

@app.get("/")
def read_root():
    return {"Hello World"}