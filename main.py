import uvicorn
from fastapi import FastAPI

from src.main.routes import registries_routes


app = FastAPI()
app.include_router(registries_routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
