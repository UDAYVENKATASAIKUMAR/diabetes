import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import joblib
Diabetes= pd.read_csv('diabetes_data_upload.csv')
dtacpy1 = Diabetes.copy()
number = preprocessing.LabelEncoder()
for column in dtacpy1.columns:
    dtacpy1[column] = number.fit_transform(dtacpy1[column])
X = dtacpy1.drop('class', axis=1)
y = dtacpy1['class']
correlation = X.apply(lambda x: x.corr(y))
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X = dtacpy1.drop('class', axis=1)
y = dtacpy1['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
rf_classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)

# Train the model on the scaled training data
rf_classifier.fit(X_train_scaled, y_train)

# Make predictions on the scaled test data
y_pred_rf = rf_classifier.predict(X_test_scaled)

# Evaluate the model on the test set
accuracy_rf = accuracy_score(y_test, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
classification_rep_rf = classification_report(y_test, y_pred_rf)

print("Random Forest Classifier:")
print(f"Accuracy: {accuracy_rf:.2f}")
print("Confusion Matrix:")
print(conf_matrix_rf)
print("Classification Report:")
print(classification_rep_rf)

# Perform cross-validation on the training set
accuracies_rf = cross_val_score(estimator=rf_classifier, X=X_train_scaled, y=y_train, cv=10)

# Display the cross-validation results
print("Cross-Validation Results:")
print("Accuracy: {:.2f} %".format(accuracies_rf.mean() * 100))
print("Standard Deviation: {:.2f} %".format(accuracies_rf.std() * 100))


