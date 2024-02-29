from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils.bankid import get_bankid_client
from dotenv import load_dotenv
from utils.config import Config
from routes import auth

load_dotenv()

config = Config("config.yml").config

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.config = config
    app.state.bankid_client = get_bankid_client(test_server=True)
    yield


app = FastAPI(lifespan=lifespan)

routes = [
    auth.router,
]

for route in routes:
    app.include_router(route)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
