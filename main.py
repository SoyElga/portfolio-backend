import os
from fastapi import FastAPI
from mangum import Mangum
from routers.labyrinthRouter import lab
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(lab)
handler = Mangum(app)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello World"}