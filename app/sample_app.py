import streamlit as st
from streamlit_chat import message


def main():
    # Setting Application title
    st.title("This is my Sample APP ! Hello ")

    # Setting Application description

    #message("My message") 
    #message("Hello bot!", is_user=True)  # align's the message to the right 

    # Text Box 
    Age =  st.number_input(
            "The Age of the Person", min_value=0, max_value=150,value=0)

    if st.button("OK"):
        st.text("My Age is : " + str(Age))


if __name__ == "__main__":
    main()
