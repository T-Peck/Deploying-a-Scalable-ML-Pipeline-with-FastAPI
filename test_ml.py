import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from ml.data import process_data
from ml.model import (train_model)
from sklearn.linear_model import LogisticRegression

# TODO: implement the first test. Change the function name and input as needed
def test_shape():
    """
    Does the training and test datasets have the expected shape.
    """
    data= pd.DataFrame({
        
            "1": [1,2,3],
            "2": [1,2,3],
            "3": [1,2,3],}
        
    )
    assert data.shape == data.dropna().shape
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_algorithm():
    """
    Does the ML model uses the expected algorithm.
    """
    data=pd.DataFrame({
        "1": [1,2,3],
        "2": [1,1,1],
        "3": [1,0,1],
    })
    X_train, y_train, _, _ = process_data(
        data,
        categorical_features=["1"],
        label="3",
        training=True,
    )
    model = train_model(X_train, y_train)

    assert isinstance(model, LogisticRegression)
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_type():
    """
    Does any ML functions return the expected type of result.
    """
    data=pd.DataFrame({
        "1": [1,2,3],
        "2": [1,1,1],
        "3": [1,0,1],
    })
    X_train, y_train, _, _ = process_data(
        data,
        categorical_features=["1"],
        label="3",
        training=True,
    )
    model = train_model(X_train, y_train)
    expected_model_type=LogisticRegression
    assert isinstance(model,expected_model_type)
    pass
