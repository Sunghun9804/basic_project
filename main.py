from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/view", StaticFiles(directory="view"), name="view")

@app.get("/")
def main():
    return RedirectResponse(url="/view/index.html")

@app.get("/one")
def step_one():
    return {"one": "one"}

@app.get("/two")
def step_two():
    return {"two": "two"}

@app.get("/three")
def step_three():
    return {"three": "three"}
