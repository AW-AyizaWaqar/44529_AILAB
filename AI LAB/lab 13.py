import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Step 1: Prepare the data
data = {
    'Hours_Studied': [2, 5, 1, 4, 6, 3, 5, 2],
    'Sleep_Hours': [5, 6, 4, 5, 7, 6, 8, 6],
    'Tuition_Attended': [0, 1, 0, 1, 1, 0, 1, 1],
    'Pass': [0, 1, 0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Step 2: Define features and labels
X = df[['Hours_Studied', 'Sleep_Hours', 'Tuition_Attended']]
y = df['Pass']

# Step 3: Train the Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Step 4: Predict for a new student
new_student = [[3, 7, 1]]  # Hours_Studied = 3, Sleep_Hours = 7, Tuition_Attended = 1
prediction = model.predict(new_student)

print(f"Prediction for new student: {'Pass (1)' if prediction[0] == 1 else 'Fail (0)'}")

# Step 5: Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=['Hours_Studied', 'Sleep_Hours', 'Tuition_Attended'], class_names=['Fail', 'Pass'], filled=True)
plt.title("Decision Tree for Student Pass Prediction")
plt.show()
