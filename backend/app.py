from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Allow cross-origin requests

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

# 🔹 Rule-based product recommendations
products = {
    "shoes": ["Running Shoes", "Sports Shoes", "Sneakers", "Walking Shoes", "Formal Shoes"],
    "laptop": ["Laptop Bag", "Cooling Pad", "Mouse", "Keyboard", "USB Hub"],
    "phone": ["Phone Cover", "Screen Guard", "Charger", "Earphones", "Power Bank"],
    "tshirt": ["Denim Jacket", "Hoodie", "Cap", "Sneakers", "Wristband"],
    "watch": ["Watch Straps", "Screen Guard", "Watch Case", "Charging Dock"],
    "bag": ["Wallet", "Keychain", "Water Bottle", "Travel Pouch", "Sling Bag"]
}

@app.get("/")
def home():
    return "Backend is Running!"

@app.get("/recommend")
def recommend():
    item = request.args.get("item", "").lower()
    result = products.get(item, ["No recommendations available for this product"])
    return jsonify({
        "input": item,
        "recommendations": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

