from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

saved = joblib.load('house_price_model.pkl')
model = saved['model']
location_avg = saved['location_avg']
society_avg = saved['society_avg']
columns = saved['columns']

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "House Price Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    size = data['size_marla']
    bedrooms = data['bedrooms']
    bathrooms = data['bathrooms']
    location = data['location']
    society = data['society']

    loc_val = location_avg.get(location, location_avg.mean())
    soc_val = society_avg.get(society, society_avg.mean())

    new_data = pd.DataFrame([[size, bedrooms, bathrooms, loc_val, soc_val]], columns=columns)
    predicted_price = model.predict(new_data)[0]

    return jsonify({'predicted_price': round(predicted_price)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    