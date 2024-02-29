import hashlib
import hmac
import time
from math import floor


def generate_qr_code_content(
    qr_start_token: str, order_time: time, qr_start_secret: str
) -> str:
    """Given QR start token, time.time() when initiated authentication call was made and the
    QR start secret, calculate the current QR code content to display.
    """
    qr_time = str(int(floor(time.time() - order_time)))
    qr_auth_code = hmac.new(
        qr_start_secret.encode(), msg=qr_time.encode(), digestmod=hashlib.sha256
    ).hexdigest()

    qr_data = str.join(".", ["bankid", qr_start_token, qr_time, qr_auth_code])

    return qr_data
