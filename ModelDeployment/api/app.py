from flask import Flask, jsonify, request
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
import pickle


# initialize flask application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return 'Welcome to Titanic Prediction API'


@app.route('/api/predict', methods=['POST'])
def titanic_predict():
    # get request data
    X = request.get_json()
    X = [[int(X['Pclass']), 
          int(X['Sex']), 
          int(X['Age']), 
          int(X['Fare']),
          int(X['Embarked']),
          int(X['Title']),
          int(X['IsAlone'])]]

    # read model
    clf = pickle.load(open('./models/titanic-random-forest-model.pkl', 'rb'))
    probabilities = clf.predict_proba(X)

    return jsonify([{'name': 'NotSurvived', 'value': round(probabilities[0, 0] * 100, 2)},
                    {'name': 'Survived', 'value': round(probabilities[0, 1] * 100, 2)}])

if __name__ == '__main__':
    # run web server
    app.run(host='0.0.0.0',
            debug=True,  # automatic reloading enabled
            port=80)