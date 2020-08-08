from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    symptom1 = request.form['sym1']
    symptom2 = request.form['sym2']
    symptom3 = request.form['sym3']
    features = np.array([[symptom1, symptom2, symptom3]])
    pred = model.predict(features)


    return render_template('index.html', prediction_text='Hey {}, symptoms are {}, {}, {} and probable disease is {}'.format(name, symptom1, symptom2, symptom3, pred))

if __name__ == '__main__':
    app.run(debug=True)