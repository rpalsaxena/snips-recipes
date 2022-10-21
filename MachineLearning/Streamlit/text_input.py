import streamlit as st

# Text input
fname = st.text_input("Enter the firstname:")
st.title(fname)

passkey = st.text_input("Enter Password", type="password")
#st.title(passkey)

## Text Area
message = st.text_area("Enter Message:")
st.write(message)

## Numbers
numbers = st.number_input("Enter number", 1, 1000, 10)
st.write(numbers)

## Date Input
myappointment = st.date_input("Appointment Date Select:")
st.write(myappointment)

## Time Input
mytime = st.time_input("My Time")
st.write(mytime)

# Color Picker
color = st.color_picker("Select Color")
st.write(color)