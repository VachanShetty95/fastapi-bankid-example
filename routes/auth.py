import time

from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse

from src.generate_qr import generate_qr_code_content
from utils.config import Config

config = Config("config.yml").config

router = APIRouter(
    prefix=config["urls"]["auth"]["index"],
    tags=["auth"],
)

# Global variables to store the authentication and order time, NOT RECOMMENDED (Use Session or Cache instead)
auth = None
order_time = None


def authenticate_user(request, user_ip):
    global auth
    if auth is None:
        auth = request.app.state.bankid_client.authenticate(
            end_user_ip=user_ip, requirement={"tokenStartRequired": False}
        )
    return auth


@router.get("")
async def index_page():
    return RedirectResponse(url="/docs", status_code=200)


@router.get("/same-device")
async def same_device_authentication(request: Request, response: Response):
    auth = authenticate_user(request, request.client.host)

    return JSONResponse(
        content={
            "orderRef": auth["orderRef"],
            "autoStartToken": auth["autoStartToken"],
        },
        status_code=200,
    )


@router.get("/other-device")
async def bankid_initiate(request: Request, response: Response):
    auth = authenticate_user(request, request.client.host)

    global order_time
    order_time = time.time()

    qr_content = generate_qr_code_content(
        auth["qrStartToken"], order_time, auth["qrStartSecret"]
    )  # Generate the first QR code content

    response = JSONResponse(
        content={
            "qr_content": qr_content,
            "order_ref": auth["orderRef"],
            "auto_start_token": auth["autoStartToken"],
        },
        status_code=200,
    )

    return response


@router.get("/get-qr-code/{order_ref}")
async def get_qr_code(order_ref: str, request: Request):
    if order_ref is None:
        qr_content = ""
    else:
        auth = authenticate_user(request, request.client.host)

        qr_content = generate_qr_code_content(
            auth["qrStartToken"], order_time, auth["qrStartSecret"]
        )  # Genrates the rest of the QR codes

    return JSONResponse(content=qr_content, status_code=200)


@router.get("/collect/{order_ref}")
async def collect(order_ref: str, request: Request):
    try:
        collect_response = request.app.state.bankid_client.collect(order_ref)
    except Exception:
        response = JSONResponse(content={"status": "failed"}, status_code=401)
        return response

    if collect_response["status"] == "complete":
        status_code = 200
    elif collect_response["status"] == "pending":
        status_code = 202
    else:
        status_code = 408

    response = JSONResponse(content=collect_response, status_code=status_code)

    return response
