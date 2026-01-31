# 🏠 House Price Prediction – End-to-End Machine Learning Project

## 📌 Overview
This project is an end-to-end machine learning system that predicts house prices based on property features.  
It includes data preprocessing, model training, log-transformed target regression, and deployment using Flask.

---

## 🚀 Features
- Data cleaning & preprocessing
- Feature scaling and categorical encoding
- Log transformation of target variable
- Model training using XGBoost
- Model serialization using Joblib
- Web deployment using Flask

---

## 🧠 Machine Learning Pipeline
1. Handle missing values
2. Encode categorical variables
3. Scale numerical features
4. Train regression model on log-transformed prices
5. Save preprocessing objects and model
6. Deploy with Flask and inverse log transformation

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Flask
- Joblib

---

## 📊 Features Used
- Rooms
- Bathroom
- BuildingArea-
- Type-
- YearBuilt
- Suburb
- Distance
- Landsize


---

## 📈 Model Output
The model predicts **log(price)**, which is converted back to the actual price using exponential transformation.

---

## 📸 Screenshots
welcome page
<img width="1920" height="965" alt="Welcome page" src="https://github.com/user-attachments/assets/d5f1acec-582b-49fd-a809-ab6951c7d11f" />
detail filling page
<img width="1920" height="965" alt="filling page" src="https://github.com/user-attachments/assets/5125c40a-5da3-477a-875f-9a5326662190" />
prediction page
<img width="1918" height="969" alt="Prediction page" src="https://github.com/user-attachments/assets/0ff55905-b4b2-458e-a76c-fe193e02f978" />




## 🖥️ How to Run Locally

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
pip install -r requirements.txt
python app.py

---

## 📸Scree shots






