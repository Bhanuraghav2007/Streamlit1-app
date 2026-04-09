import streamlit as st
st.title("streamlit app")
about_page=st.Page(
    page ='views/about.py',
    title='About us',

)
contact_page=st.Page(
    page='views/contact.py',
    title='contact us',
)
profile_page=st.Page(
    page='views/profile.py',
    title='My profile',
    default=True,
)
nb=st.navigation(pages=[about_page,contact_page,profile_page])


