from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)
app.json.compact = False

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Click2Buy Shop", "resource_end_point": "/products"}), 200
# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products(): # TODO: Return all products or filter by ?category=
    category = request.args.get("category")
    if category:
        filtered_products = [product for product in products if product["category"].lower() == category.lower()]
        return jsonify(filtered_products), 200
    return jsonify(products)

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id): # TODO: Return product by ID or 404
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
