
# Product Catalog API

This Flask API serves a small in-memory product catalog. It exposes read-only endpoints for returning a welcome message, listing products, filtering by category, and retrieving a single product by ID.

## What the API does

The app is designed to act as a simple backend for a product catalog. It provides:

- A home route that returns a welcome message
- A `GET /products` endpoint that returns all products
- A `GET /products?category=<category>` endpoint to filter products by category
- A `GET /products/<id>` endpoint to fetch one product by its ID
- JSON responses with appropriate HTTP status codes (`200` for success, `404` if a product is not found)

## Endpoints

### `GET /`
Returns a welcome message.

Example response:

```json
{
  "message": "Welcome to our Home Page!"
}
```

### `GET /products`
Returns all products in the catalog.

```bash
curl http://localhost:5000/products
```

Example response:

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

### `GET /products?category=books`
Returns only the products in the selected category.

```bash
curl "http://localhost:5000/products?category=books"
```

Example response:

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

### `GET /products/<id>`
Returns a single product by its numeric ID.

```bash
curl http://localhost:5000/products/2
```

Example response:

```json
{
  "id": 2,
  "name": "Book",
  "price": 14.99,
  "category": "books"
}
```

If the product does not exist, the API returns a `404` response:

```json
{
  "message": "Product not found"
}
```

## Running the app

1. Install Flask if needed:

```bash
pip install flask
```

2. Start the server:

```bash
python app.py
```

3. Visit the endpoints in a browser or call them with `curl`.

## Example usage

### Using curl

```bash
curl http://localhost:5000/
curl http://localhost:5000/products
curl http://localhost:5000/products/1
curl "http://localhost:5000/products?category=electronics"
```

### Example JSON response

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 899.99,
  "category": "electronics"
}
```

## Project notes

This project is a simple example of building RESTful GET routes in Flask using:

- `@app.route()` for endpoint definitions
- `request.args.get()` for query-string filtering
- `jsonify()` for returning JSON data
- HTTP status codes for successful and unsuccessful responses

This makes it a good starting point for learning how to build read-only APIs before moving on to create, update, and delete routes.
