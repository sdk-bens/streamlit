import streamlit as st
import pandas as pd
st.title("My CE App")
st.header('Data Visualization Section')  # Sets a header for a section
st.subheader('Subsection: Pie Chart Analysis')  # Sets a subheader for a subsection

st.text('This section focuses on data preprocessing.')
st.markdown('**This is some bold text**')
data = {
    'A': [45, 37, 89, 67],
    'B': ['John', 'Max', 'Lisa', 'Chris']
}
df = pd.DataFrame(data)

st.write(df)


age = st.slider('Your age', min_value=0, max_value=100)  # Returns the value selected by the user
if st.button('Say Hello'):  # Returns True if the user clicks the button
    st.write('Hello!')
show_df = st.checkbox('Show DataFrame')  # Returns True if the user checks the box, False otherwise
if show_df:
    st.write(df)
