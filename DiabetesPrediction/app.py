from flask import Flask, render_template, request
import numpy as np
import joblib
from keras.models import Sequential
from keras.layers import Dense

app = Flask(__name__)

# Load trained stacking model
stacking_model = joblib.load('stacking_model_2.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = float(request.form['age'])

        # Preprocess input data
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        deep_model = Sequential()
        deep_model.add(Dense(12, input_dim=8, activation='relu'))
        deep_model.add(Dense(8, activation='relu'))
        deep_model.add(Dense(1, activation='sigmoid'))  # Số lượng units trong lớp cuối cùng là 1
        deep_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        transformed_input = deep_model.predict(input_data)
        # Make prediction
        prediction = stacking_model.predict(transformed_input)
   
        # Format prediction
        if prediction[0] >= 0.5:
            result = 'Positive'
        else:
            result = 'Negative'

        return render_template('index.html', prediction_text='{}'.format(result))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
