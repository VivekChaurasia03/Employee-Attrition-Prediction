# Trainig the model - task from config.json will let this file know which model to go for in-order to train the data.
from sklearn.metrics import accuracy_score, confusion_matrix

def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    """Train and evaluate model"""
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)

    # checking if model has method called predicts_probab
    if hasattr(model, "predict_proba"):
        # predict_proba return a matrix of two columns (negative and positive), [:, 1] means probab of the class in test data
        y_prob = model.predict_proba(X_test)[:, 1]

    else: 
        # if model doesnt have predict_proba it uses decision_function for each test instance 
        y_prob = model.decision_function(X_test)

    return accuracy, cm, y_test, y_prob