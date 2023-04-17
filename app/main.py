from fastapi import FastAPI
from .routers import contents, state


app = FastAPI()


app.include_router(contents.router)
app.include_router(state.router)
