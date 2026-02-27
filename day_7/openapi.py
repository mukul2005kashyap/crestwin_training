"""OpenAPI is a specification that defines how REST APIs should be described.

It allows developers to:

    Describe API endpoints
    Define request/response formats
    Document authentication
    Generate interactive documentation automatically
    Earlier it was known as Swagger Specification, and later it became OpenAPI Specification (OAS) under the Linux Foundation.

 What is Swagger?

Swagger is a set of tools built around the OpenAPI specification.

Main Swagger Tools:

    Swagger UI
    Swagger Editor
    Swagger Codegen
    Swagger UI provides an interactive web interface to test APIs directly from the browser.

 OpenAPI in FastAPI

One of the biggest advantages of FastAPI is that it automatically generates OpenAPI documentation.

When you create a FastAPI app:

uvicorn app:main --reload

/docs

What is OpenAPI JSON?

FastAPI automatically creates:

http://127.0.0.1:8000/openapi.json

This file contains:

    All endpoints
    Request schemas
    Response schemas
    Validation rules

This JSON follows the OpenAPI standard.

 How FastAPI Generates Docs Automatically

FastAPI uses:

Python type hints

Pydantic models

Path operation decorators

Example with request body:

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user

Now Swagger automatically shows:

Request body schema

Field types

Required fields

Example JSON

No manual documentation needed.

 Advantages of OpenAPI & Swagger

        ✅ Automatic documentation
        ✅ Interactive API testing
        ✅ Client SDK generation
        ✅ Clear API contract
        ✅ Useful for frontend-backend integration
        ✅ Helpful in microservices architecture"""