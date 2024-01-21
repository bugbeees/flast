from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

rugs_data = [
    {"id": 1, "name": "Traditional Rug", "price": 99.99, "image": "rug1.jpg"},
    {"id": 2, "name": "Modern Design Rug", "price": 129.99, "image": "rug2.jpg"},
    {"id": 3, "name": "Vintage Area Rug", "price": 79.99, "image": "rug3.jpg"},
]

@app.route("/")
def home():
    return render_template("index.html", rugs=rugs_data)

@app.route("/rug/<int:rug_id>")
def view_rug(rug_id):
    rug = next((item for item in rugs_data if item["id"] == rug_id), None)
    if rug:
        return render_template("rug_details.html", rug=rug)
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
