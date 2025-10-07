from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("index.html", name=name)


@app.get("/calculate")
def show_calculate_form():
    return render_template("calculate.html")


@app.post("/calculate")
def calculate():
    input1 = float(request.form.get("input1"))
    input2 = float(request.form.get("input2"))
    result = input1 + input2
    return render_template("result.html", input1=input1, input2=input2, result=result)


@app.get("/api/time")
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"time": current_time})


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
