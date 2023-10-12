# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from utils import load_config
from prediction import Prediction



def main():
    # Setting Application title
    st.title("Personal Loan Prediction App")

    # Setting Application description
    st.markdown(
        """
     :dart:  This  app is made to predict whether customer will take Personal loan or not.
    The application is functional for both online prediction and batch data prediction. \n
    """
    )
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    # Setting Application sidebar default
    #image = Image.open("./app/App.jpg")
    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?", ("Online", "Batch")
    )
    st.sidebar.info("This app is created to predict Personal Loan")
    #st.sidebar.image(image)

    config = load_config()
    p = Prediction()
    model_weight_path = config['model_weight_path']
    feature_path = config['feature_path']
    
    if add_selectbox == "Online":
        st.info("Input data below")
        # Based on our optimal features selection
        st.subheader("Demographic data")
        Age = st.number_input(
            "The Age of the Person",
            min_value=0,
            max_value=150,
            value=0,
        )
        Experience = st.number_input(
            "The no years of Experience  of the Person",
            min_value=0,
            max_value=150,
            value=0,
        )
        Family = st.number_input(
            "No of Family members in Family",
            min_value=0,
            max_value=50,
            value=0,
        )
        Education = st.number_input(
            "Education level",
            min_value=0,
            max_value=50,
            value=0,
        )

        st.subheader("Finance data")
        Income = st.slider(
            "The Income of the Person",
            min_value=0,
            max_value=100000000,
            value=0,
        )
        st.subheader("Credit Card Spend")
        CCAvg = st.slider(
            "Avg Credit Card Spend of the person",
            min_value=0,
            max_value=100000000,
            value=0,
        )
        st.subheader("Mortgage")
        Mortgage = st.selectbox(
            "Does the customer has Mortgages", (1, 0)
        )
        st.subheader("Securities_Account")
        Securities_Account = st.selectbox(
            "Does the customer has Securities Account", (1, 0)
        )
        st.subheader("CD_Account")
        CD_Account = st.selectbox(
            "Does the customer has CD Account", (1, 0)
        )
        st.subheader("Online Account")
        Online = st.selectbox(
            "Does the customer has Online Account", (1, 0)
        )
        st.subheader("CreditCard")
        CreditCard = st.selectbox(
            "Does the customer has CreditCard", (1, 0)
        )

        data = {
            'Age':Age,
            'Experience':Experience,
            'Income': Income,
            'Family':Family,
            'CCAvg':CCAvg,
            'Education':Education,
            'Mortgage':Mortgage,
            'Securities Account':Securities_Account,
            'CD Account':CD_Account,
            'Online':Online,
            'CreditCard':CreditCard
                }
        features_df = pd.DataFrame.from_dict([data])
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.write("Overview of input is shown below")
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        st.dataframe(features_df)

        # Preprocess inputs
        prediction = p.live_predict(features_df,model_weight_path, feature_path )
        print(prediction)

        if st.button("Predict"):
            if prediction == 1:
                st.warning("Yes, the customer will Take Personal Loan.")
            else:
                st.success("No, the customer will not Take Personal Loan.")

    else:
        st.subheader("Dataset upload")
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            # Get overview of data
            st.write(data.head())
            st.markdown("<h3></h3>", unsafe_allow_html=True)
            if st.button("Predict"):
                # Get batch prediction
                prediction = p.live_predict(data,model_weight_path, feature_path)
                data["Predictions"] = prediction
                data["Predictions_Inference"] = data["Predictions"].replace(
                    {
                        1: "Yes, the customer will Take Personal Loan.",
                        0: "No, the customer will not Take Personal Loan.",
                    }
                )

                st.markdown("<h3></h3>", unsafe_allow_html=True)
                st.subheader("Prediction")
                st.write(data)


if __name__ == "__main__":
    main()