
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# deserialize pickle object
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # inputted values from user
    user_features = [int(x) for x in request.form.values()]
    final_features = [np.array(user_features)]
    # creates prediciton using model
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    # outputs to html file
    # ZIPCODE, BEDS, BATHS, SQFT, LOT_SIZE, YEAR_BUILT
    return render_template('index.html', prediction_text=(f'Predicted Home Value: ${output}'))


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0')
