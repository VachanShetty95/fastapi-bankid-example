## FastAPI BankID Implementation

This repository serves as a comprehensive example of integrating BankID functionality into a FastAPI project. It demonstrates how to leverage the FastAPI framework to build a robust backend service that interacts with BankID for secure authentication and identification purposes. By following this example, developers can learn best practices for implementing BankID in their FastAPI applications, ensuring a seamless and secure user authentication experience.

### Features:

- **FastAPI Integration:** Utilizes the FastAPI framework for building efficient and scalable API endpoints.
- **BankID Implementation:** Demonstrates the integration of BankID services using the `pybankid` library for secure user authentication and identification.
- **Example Endpoints:** Includes sample endpoints illustrating how to incorporate BankID functionality into various parts of a FastAPI application.
- **Documentation:** Provides clear documentation and usage instructions to facilitate easy adoption and understanding for developers.

Whether you're new to FastAPI or looking to integrate BankID into your existing FastAPI project, this example repository serves as a valuable resource for implementing secure authentication with BankID.

## Running the application

To run the app, you need to have Docker Compose installed on your machine.

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the root directory of the project.
3. Run the following command to start the app:
    ```shell
    docker compose up --build
    ```
4. To run in detached mode:
    ```shell
    docker compose up -d --build
    ```

## API Endpoints

1. Documentation for all the API endpoints can be found at:
    ```shell
    http://localhost:8080/docs
    ```

## References

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyBankID](https://pybankid.readthedocs.io/)