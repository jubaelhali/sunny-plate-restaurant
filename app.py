from flask import Flask, jsonify, render_template

app = Flask(__name__)

MENU = [
    {"id": 1, "name": "Chicken Burger", "category": "Burgers", "price": 129, "description": "Juicy grilled chicken, fresh lettuce, and our house sauce.", "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?auto=format&fit=crop&w=900&q=85"},
    {"id": 2, "name": "Classic Beef Burger", "category": "Burgers", "price": 159, "description": "A hearty beef patty with cheese, tomato, and pickles.", "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=85"},
    {"id": 3, "name": "Creamy Carbonara", "category": "Pasta", "price": 149, "description": "Creamy white sauce, parmesan, and savory bacon bits.", "image": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=900&q=85"},
    {"id": 4, "name": "Classic Spaghetti", "category": "Pasta", "price": 120, "description": "Our comforting tomato sauce with herbs and parmesan.", "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=900&q=85"},
    {"id": 5, "name": "Crispy French Fries", "category": "Sides", "price": 79, "description": "Golden, crispy fries served with a tasty dip.", "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=900&q=85"},
    {"id": 6, "name": "Iced Coffee", "category": "Drinks", "price": 89, "description": "Smooth, refreshing coffee served chilled.", "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=900&q=85"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/menu")
def menu():
    return jsonify(MENU)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "Sunny Plate is running"})

if __name__ == "__main__":
    app.run(debug=True)
