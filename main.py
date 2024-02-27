from fastapi import FastAPI, Request, Response
from contextlib import asynccontextmanager
from utils.bankid import get_bankid_client
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

load_dotenv()

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.bankid_client = get_bankid_client(test_server=True)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/same-device")
async def same_device_authentication(request: Request, response: Response):
    user_ip = request.client.host

    auth = request.app.state.bankid_client.authenticate(
        end_user_ip=user_ip,
        requirement={"tokenStartRequired": False}
    )
    
    return JSONResponse(
        content={
            "orderRef": auth["orderRef"],
            "autoStartToken": auth["autoStartToken"]},
        status_code=200
    
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
