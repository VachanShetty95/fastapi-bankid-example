import os
import logging
from bankid import BankIDJSONClient
from bankid.certutils import split_certificate


def get_bankid_client(test_server: bool = True) -> BankIDJSONClient:
    """
    Returns an instance of BankIDJSONClient for interacting with the BankID service.

    Args:
        test_server (bool, optional): Flag indicating whether to use the test server or production server.
            Defaults to True.

    Returns:
        BankIDJSONClient: An instance of BankIDJSONClient.

    Raises:
        ValueError: If one or more required environment variables are not set.
    """
    try:
        cert_path = os.getenv("TEST_CERT_PATH" if test_server else "PROD_CERT_PATH")
        dest_path = os.getenv("TEST_DEST_PATH" if test_server else "PROD_DEST_PATH")
        password = os.getenv(
            "TEST_CERT_PASSWORD" if test_server else "PROD_CERT_PASSWORD"
        )

    except ValueError as e:
        logging.error(f"One or more required environment variables not set {e}")

    cert_paths = split_certificate(cert_path, dest_path, password)
    return BankIDJSONClient(cert_paths, test_server=test_server)
