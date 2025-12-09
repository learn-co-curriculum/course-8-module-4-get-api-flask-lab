from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Implement homepage route that returns a welcome message
@app.route("/", methods=["GET"])
def home():
    # Return a welcome message
    return jsonify({"message": "Welcome to the Product Catalog API!"})


# Implement GET /products route that returns all products or filters by category

@app.route("/products", methods=["GET"])
def get_products():
    # Get the 'category' query parameter from the URL, if it exists
    category = request.args.get("category")

    # If a category is provided, filter the products list
    if category:
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products)

    # If no category is provided, return all products
    return jsonify(products)

# Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    # Loop through the list of products to find a match by id
    #Return product by ID or 404
    for product in products:
        if product["id"] == id:
            return jsonify(product)
        
    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
