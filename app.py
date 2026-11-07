from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample restaurant menu data served by the Python backend
menu = [
    {
        "name": "Classic Burger",
        "description": "Juicy beef burger with fresh vegetables.",
        "price": "₱120",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=80"
    },
    {
        "name": "Creamy Pasta",
        "description": "Pasta tossed in a rich, creamy sauce.",
        "price": "₱135",
        "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=900&q=80"
    },
    {
        "name": "Chicken Meal",
        "description": "Golden chicken served with rice.",
        "price": "₱150",
        "image": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=900&q=80"
    }
]

@app.route("/")
def home():
    return render_template("index.html", menu=menu)

@app.route("/api/menu")
def menu_api():
    return jsonify(menu)

if __name__ == "__main__":
    app.run(debug=True)
