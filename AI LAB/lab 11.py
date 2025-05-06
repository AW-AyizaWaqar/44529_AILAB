# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Load the dataset from local file
# Make sure the file is in the same directory as your script
dataset = pd.read_csv('Social_Network_Ads.csv')

# Display basic info
print("Dataset Head:\n", dataset.head())
print("\nDataset Info:\n")
dataset.info()

# Select features and target
X = dataset.iloc[:, [2, 3]].values  # Age and EstimatedSalary
y = dataset.iloc[:, 4].values       # Purchased

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train the Naive Bayes model
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Evaluate the model
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Output results
print("\nConfusion Matrix:\n", cm)
print("\nAccuracy Score:", accuracy)
print("\nClassification Report:\n", report)
