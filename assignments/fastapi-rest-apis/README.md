# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework in Python. You will create endpoints for managing a simple resource, such as a list of items or tasks.

## 📝 Tasks

### 🛠️	Basic API Endpoints

#### Description
Create a FastAPI application with basic CRUD (Create, Read, Update, Delete) endpoints for a simple resource like "items" or "tasks".

#### Requirements
Completed program should:

- Have a root endpoint (/) that returns a welcome message
- Have a GET endpoint to retrieve all items
- Have a POST endpoint to create a new item
- Have a GET endpoint to retrieve a single item by ID
- Have a PUT endpoint to update an item by ID
- Have a DELETE endpoint to delete an item by ID
- Use appropriate HTTP status codes
- Include basic error handling


### 🛠️	Advanced Features

#### Description
Enhance your API with advanced FastAPI features like data models, validation, and documentation.

#### Requirements
Completed program should:

- Use Pydantic models for request/response data validation
- Include path and query parameters where appropriate
- Add automatic API documentation (Swagger UI)
- Implement proper error responses with custom exception handlers
- Add at least one endpoint with query parameters for filtering or searching