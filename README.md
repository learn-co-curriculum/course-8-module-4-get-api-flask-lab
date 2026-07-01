# Product Catalog REST API

A simple RESTful API built with Flask that provides access to a fictional product catalog. The API demonstrates REST principles by exposing GET endpoints, returning JSON responses, supporting dynamic route parameters, and filtering data using query parameters.

## Features

* Welcome endpoint for the API.
* Retrieve all products.
* Retrieve a single product by its ID.
* Filter products by category using a query string.
* JSON-formatted responses using `jsonify()`.
* Appropriate HTTP status codes for successful and unsuccessful requests.

## Technologies Used

* Python 3
* Flask
* Pipenv
* JSON

## Project Structure

```text
product-catalog-api/
├── app.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── pytest.ini
```

## Installation

1. Clone the repository.

```bash
git clone git@github.com:wanja-juma/course-8-module-4-get-api-flask-lab.git
```

2. Navigate to the project directory.

```bash
cd product-catalog-api
```

3. Install the project dependencies.

```bash
pipenv install
```

4. Activate the virtual environment.

```bash
pipenv shell
```

## Running the Application

Start the Flask development server:

```bash
flask --app app run
```

or

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Home

**Endpoint**

```text
GET /
```

Returns a welcome message for the Product Catalog API.

**Example Response**

```json
{
  "message": "Welcome to the Product Catalog API"
}
```

---

### Get All Products

**Endpoint**

```text
GET /products
```

Returns a list of all available products.

**Example Response**

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 899.99,
    "category": "electronics"
  },
  {
    "id": 2,
    "name": "Book",
    "price": 14.99,
    "category": "books"
  },
  {
    "id": 3,
    "name": "Desk",
    "price": 199.99,
    "category": "furniture"
  }
]
```

---

### Get a Product by ID

**Endpoint**

```text
GET /products/<id>
```

Returns the product matching the specified ID.

**Success Response**

**Status Code:** `200 OK`

**Error Response**

**Status Code:** `404 Not Found`

```json
{
  "error": "Product not found"
}
```

---

### Filter Products by Category

**Endpoint**

```text
GET /products?category=<category_name>
```

Returns only the products that belong to the specified category.

**Example**

```text
GET /products?category=books
```

**Example Response**

```json
[
  {
    "id": 2,
    "name": "Book",
    "price": 14.99,
    "category": "books"
  }
]
```

## HTTP Status Codes

| Status Code       | Description                               |
| ----------------- | ----------------------------------------- |
| **200 OK**        | Request completed successfully.           |
| **404 Not Found** | The requested product could not be found. |

## Display Image

Screenshot 2026-07-02 020105.png

Screenshot 2026-07-02 020134.png

## Example Requests

```text
GET /
GET /products
GET /products/1
GET /products/10
GET /products?category=electronics
GET /products?category=books
```

## Author

Ruth Juma
