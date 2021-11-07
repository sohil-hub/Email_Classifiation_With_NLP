"""This is the prediction page of the web app"""

# Import necessary modules
import streamlit as st
import numpy as np
import sklearn
import joblib
import numpy as np
import tensorflow as tf

def app():
    """This funciton runs the prediction page"""

    st.write("Welcome to the Prediction Page")

    # Create a method to take text input from a user
    Email = st.text_input("Enter Emain Text:")
    Listed_Email = [Email]
    
    CV = joblib.load("From Scratch/CountVectorizer")
    model_Gaussian = joblib.load("From Scratch/Gaussian_Classifier")

    model = tf.keras.models.load_model('From Scratch/ann_classifier.h5')

    # Create a button to get the prediction values on click
    if (st.button("Predict")):
        

        def get_prediction(reviews):
            CV = joblib.load('From Scratch/CountVectorizer')
            model_ann = tf.keras.models.load_model('From Scratch/ann_classifier.h5')
            X_to_be_predicted = CV.transform(reviews).toarray()
            y_predicted = model_ann.predict(X_to_be_predicted)
            y_predicted = np.where(y_predicted > 0.5, 1, 0)
            return y_predicted

        result = get_prediction(Listed_Email)
        st.success("Prediction successful!!!")
        if result[0][0] == 1:
            st.success("The given email has been predicted to be a spam")
        else:
            st.success("The given email has been predicted to be not a spam")
