import pandas as pandas
import streamlit as st

## Working with Widgets 
## Buttons/Radio/Checkbox/Select

# Working with Buttons
st.button("Submit", key="test")

name = "Rahul"
if st.button("Submit", key="upper"):
	st.write("Name is {}".format(name.upper()))

if st.button("Submit", key='lower'):
	st.write("Name is {}".format(name.lower()))


########### --------------- ##############
###          RADIO BUTTON              ###
########### --------------- ##############
status = st.radio("What is your status",  ("Active", "Inactive"))

if status == "Active":
	st.success("You are active.")
elif status == "Inactive":
	st.warning("Inactive")

# Working with Checkbox
if st.checkbox("Show/Hide"):
	st.text("Show something")

## Expander
with st.expander("Python"):
	st.success("Hello")
	st.write("Bye")


### Select/Multiple Select
my_lang = ['Python', 'Julia', 'Go', 'Rust']

choice = st.selectbox("Language", my_lang)
st.write("You selected: {}".format(choice))

## Multiple Select
spoken_lang = ("English", "Spanish", "French", "K", "G", "R", "S")
my_spoken_lang = st.multiselect("Spoken Lang", 
					spoken_lang, default="English"
				)

### Slider
age = st.slider("Age", 1, 101)

### Any Datatype
# Select Slider
op = ['yellow', 'red', 'blue', 'black']

color = st.select_slider("Choose Color", options = op) #, label_visibility="visible")
### Task is to make all these options visible
