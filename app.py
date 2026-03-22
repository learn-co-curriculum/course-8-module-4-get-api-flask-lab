from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 499.99},
    {"id": 3, "name": "Coffee Maker", "category": "Home Appliances", "price": 79.99},
    {"id": 4, "name": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": 5, "name": "Blender", "category": "Home Appliances", "price": 59.99},
]


@app.route("/")
def home():
    return "<h1>Welcome to the Product API!</h1>"  #return a simple welcome message

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    products_list = products  # TODO: Filter products by category if query parameter is provided
    return jsonify(products_list)


# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)  # TODO: Find product by ID
    if product:
        return jsonify(product)
    else:
     return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
