from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('house_price_model.pkl')

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and predict price
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    main_road = int(request.form['main_road'])
    semi_furnished = int(request.form['semi_furnished'])
    unfurnished = int(request.form['unfurnished'])

    # Prepare features array for prediction
    features = np.array([[area, bedrooms, bathrooms, main_road, semi_furnished, unfurnished]])

    # Make prediction
    predicted_price = model.predict(features)[0]

    # Render the same page with the predicted price
    return render_template('index.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
