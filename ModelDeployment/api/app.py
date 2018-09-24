from flask import Flask, jsonify, request
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
import pickle

# declare constants
HOST = '0.0.0.0'
PORT = 8081

# initialize flask application
app = Flask(__name__)
@app.route('/api/iris/train', methods=['POST'])
def iris_train():
    # get parameters from request
    parameters = request.get_json()
    
    # read iris data set
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # fit model
    clf = svm.SVC(C=float(parameters['C']),
                  probability=True,
                  random_state=1)
    clf.fit(X, y)
    # persist model
    joblib.dump(clf, 'model.pkl')
    return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})

@app.route('/api/iris/predict', methods=['POST'])
def iris_predict():
    # get iris object from request
    X = request.get_json()
    X = [[float(X['sepalLength']), float(X['sepalWidth']), float(X['petalLength']), float(X['petalWidth'])]]

    # read model
    clf = joblib.load('model.pkl')
    probabilities = clf.predict_proba(X)

    return jsonify([{'name': 'Iris-Setosa', 'value': round(probabilities[0, 0] * 100, 2)},
                    {'name': 'Iris-Versicolour', 'value': round(probabilities[0, 1] * 100, 2)},
                    {'name': 'Iris-Virginica', 'value': round(probabilities[0, 2] * 100, 2)}])

@app.route('/api/titanic/predict', methods=['POST'])
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
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)