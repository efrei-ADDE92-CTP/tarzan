from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from flask import Flask, request, jsonify
import joblib

# Load the Iris dataset
iris = datasets.load_iris()

# Create feature and target arrays
X = iris.data
y = iris.target

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a k-NN classifier
knn = KNeighborsClassifier()

# Fit the classifier to the data
knn.fit(X_train, y_train)

# Evaluate the model
accuracy = knn.score(X_test, y_test)
print('Test set accuracy: {:.2f}'.format(accuracy))

# Make predictions on unseen data
X_new = [[5.1, 3.5, 1.4, 0.2], [6.3, 3.3, 4.7, 1.6]] # data : [ [sl, sw, pl, pw ]]

predictions = knn.predict(X_new)
print('Predictions: {}'.format(predictions))

# Evaluate the model using cross-validation
scores = cross_val_score(knn, X, y, cv=5)
training_score = knn.score(X_train, y_train)

# Evaluate the model on the test set
test_score = knn.score(X_test, y_test)

print('Training score: {:.2f}'.format(training_score))
print('Test score: {:.2f}'.format(test_score))

if training_score > test_score:
    print('Model is overfitting')
else:
    print('Model is not overfitting')

# Save the model as a pickle in a file with the name knn_model.pkl using joblib
joblib.dump(knn, 'knn_model.pkl')

# Create a Flask app

app = Flask(__name__)

# Load the model
model = joblib.load('knn_model.pkl')

# Create a route for the home page (just for test)
@app.route('/')
def home():
    return "Hello, World!"

# Create a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # reshape data
    #data = [data['sl'], data['sw'], data['pl'], data['pw']]

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict(data)

    # labels
    iris_labels = ['iris setosa', 'iris versicolor', 'iris virginica']
    # Take the first value of prediction
    output = iris_labels[prediction[0]]

    return jsonify(output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)