joblib.dump(knn, 'knn_model.pkl')
app = Flask(__name__)
if __name__ == "__main__":
    app.run(host="0.0.0.0")

# Load the model from the file
    model = joblib.load('knn_model.pkl')

# Load the Iris dataset
    iris = datasets.load_iris()

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Make prediction using the model
    prediction = model.predict(data)

    # Get the names of the iris species
    species = [iris.target_names[i] for i in prediction]

    # Return the prediction as a response
    return jsonify(species)