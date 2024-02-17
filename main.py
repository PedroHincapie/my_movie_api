from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "movie": "The Shawshank Redemption",
        "rating": 9.2,
        "image": "images/shawshank.jpg",
        "imdb_url": "https://www.imdb.com/title/tt0111161/",
    },
    {
        "id": 2,
        "movie": "The Godfather",
        "rating": 9.2,
        "image": "images/godfather.jpg",
        "imdb_url": "https://www.imdb.com/title/tt0068646/",
    },
    {
        "id": 3,
        "movie": "The Dark Knight",
        "rating": 9,
        "image": "images/dark_knight.jpg",
        "imdb_url": "https://www.imdb.com/title/tt0468569/",
    },
    {
        "id": 4,
        "movie": "Pulp Fiction",
        "rating": 8.9,
        "image": "images/pulp_fiction.jpg",
        "imdb_url": "https://www.imdb.com/title/tt0110912/",
    },
    {
        "id": 5,
        "movie": "The Lord of the Rings: The Return of the King",
        "rating": 9,
        "image": "images/lotr_return_king.jpg",
        "imdb_url": "https://www.imdb.com/title/tt0167260/",
    },
]


@app.get("/", tags=["Home"])
def message():
    return "Hola Mundo!"


@app.get("/web", tags=["Home-web"])
def hello():
    return HTMLResponse("<h1>Holii Mamá</h1>")


@app.get("/movies", tags=["Lista peliculas"])
def get_movies():
    return movies


@app.get("/movies/{id}")
def get_movies_by_id(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return {}
