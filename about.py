   
"""This is about page"""

# import necessary modules
import streamlit as st


def app():
    """This function runs the about page"""
    # Add balloons animation when page opens
    st.balloons()

    # Add title
    st.title("Welcome to the about me page")

    # Add email
    st.markdown('''### Name:
    Mohammedsohil Shaikh''')

    # Add name
    st.markdown('''### Email:
    sohilshaikh1609@gmail.com''')

    # Add github
    st.markdown('''### GitHub: [Mohammedsohil Shaikh](https://github.com/sohil-hub)''')

    # Add linkedin
    st.markdown('''### Linkedin: [Mohammedsohil Shaikh](https://www.linkedin.com/in/mohammedsohil-shaikh-02b5401ba/)''')
