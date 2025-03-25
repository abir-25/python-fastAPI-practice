from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'data': {'name': 'Abir'}}


@app.get("/about")
def about():
    return {'data': {'about': 'The superstar developer of this company'}}