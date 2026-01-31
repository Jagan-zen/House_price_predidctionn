
from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from datetime import date

#importing melbourne dataset
df = pd.read_csv("./data/melb_data.csv")

app = Flask(__name__)

# model and encoders
model = joblib.load("model/houseprice.joblib")
le_suburb = joblib.load("model/le_suburb.pkl")
le_type = joblib.load("model/le_type.pkl")
scaler = joblib.load("model/scaler.pkl")

# Data for display in form
suburbs = df["Suburb"].unique()
year = date.today().year




@app.route("/")
def home():
    return render_template("Welcome.html")





@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        rooms = float(request.form["rooms"])
        bathroom = float(request.form["bathrooms"])
        building_area = float(request.form["area"])
        type_raw = request.form["type"]
        year_built = float(request.form["year"])
        suburb_raw = request.form["suburb"]
        distance = float(request.form["distance"])
        land_size_raw = float(request.form["landsize"])

        type_enc = le_type.transform([type_raw])[0]
        suburb_enc = le_suburb.transform([suburb_raw])[0]

        # 3️⃣ Scale Landsize (ONLY Landsize)
        land_size_scaled = scaler.transform([[land_size_raw]])[0][0]

        # 4️⃣ Arrange features in EXACT training order
        x = np.array([[
            rooms,
            bathroom,
            building_area,
            type_enc,
            year_built,
            suburb_enc,
            distance,
            land_size_scaled
        ]])

        # 5️⃣ Predict LOG(price)
        log_price = model.predict(x)[0]

        # 6️⃣ INVERSE LOG TRANSFORM (CRITICAL)
        actual_price = np.exp(log_price)

        print(actual_price)

        return render_template(
            "pred.html",
            prediction=int(actual_price)
        )
    return render_template("index.html", suburbs=suburbs, year=year)


if __name__ == '__main__':
    app.run(debug=True)
