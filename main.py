from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/view", StaticFiles(directory="view"), name="view")

@app.get("/")
def main():
    return RedirectResponse(url="/view/index.html")