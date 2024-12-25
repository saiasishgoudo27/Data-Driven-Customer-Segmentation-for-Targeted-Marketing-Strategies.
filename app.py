from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained K-Means model
with open('model/model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        gender = request.form['gender']
        age = int(request.form['age'])
        income = float(request.form['income'])
        spending_score = float(request.form['spendingScore'])

        # Map gender to numeric values
        gender_map = {'Male': 0, 'Female': 1, 'Other': 2}
        gender_num = gender_map[gender]

        # Create feature array for prediction
        features = np.array([[gender_num, age, income, spending_score]])

        # Predict the cluster using the loaded KMeans model
        cluster_index = kmeans_model.predict(features)[0]

        # Cluster descriptions
        cluster_descriptions = {
            0: "Cluster 1 (Brown): These customers have a low annual income but a high spending score. Therefore, we can suggest a few products to these customers.",
            1: "Cluster 2 (Red): These customers have both a low annual income and a low spending score. Thus, we likely can't suggest many products to these customers.",
            2: "Cluster 3 (Black): These customers have a medium annual income and a medium spending score. Hence, we can suggest a moderate number of products to these customers.",
            3: "Cluster 4 (Green): These customers have a high annual income and a high spending score. Consequently, we don't need to suggest many products to these customers.",
            4: "Cluster 5 (Yellow): These customers have a high annual income but a low spending score. Therefore, we should suggest more products to these customers."
        }

        # Get the description for the predicted cluster
        cluster_description = cluster_descriptions.get(cluster_index, "Cluster description not found")

        
       
        

        # Return the result to the user, passing the description and background color to the template
        return render_template('index.html', description=cluster_description)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
