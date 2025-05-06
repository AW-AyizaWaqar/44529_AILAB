import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Load dataset
dataset = pd.read_csv('iris.csv')  

# Encode categorical variables
label_encoders = {}
for column in dataset.columns:
    if dataset[column].dtype == 'object':
        le = LabelEncoder()
        dataset[column] = le.fit_transform(dataset[column])
        label_encoders[column] = le


X = dataset.drop('Salary', axis=1)  # All except target
y = dataset['Salary']              # Target variable

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Naive Bayes model
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predict and evaluate
y_pred = classifier.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("✅ Confusion Matrix:\n", cm)
print("\n✅ Accuracy Score:", acc)
print("\n✅ Classification Report:\n", report)


