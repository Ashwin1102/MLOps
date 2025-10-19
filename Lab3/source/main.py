# Import necessary libraries
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import joblib

if __name__ == '__main__':
    # Load the Diabetes dataset
    diabetes = load_diabetes()
    X, y = diabetes.data, diabetes.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    # Add a constant (intercept term) to the features
    X_train_sm = sm.add_constant(X_train)

    # Train an OLS regression model
    model = sm.OLS(y_train, X_train_sm).fit()

    # Print model summary
    print(model.summary())

    # Save the model using joblib
    joblib.dump(model, 'diabetes_ols_model.pkl')

    print("The model training was successful")
