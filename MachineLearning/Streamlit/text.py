import streamlit as st
import pandas as pd

# Header
st.header("This is header of the site")


## Subheader
st.subheader("Let's print subheader")

# Title
st.title("This is a title.")

st.text("Hello World this is a text.")

name = "Rahul"
st.text("This is {}".format(name))

# Markdown
st.markdown(" ### This is markdown")

# Display Colored Text/Bootstraps Alert
st.success("Successful")
st.warning("This is danger.")
st.info("This is information")
st.error("This is an error.")

### Superfunction
st.write("Normal Text")
st.write("## This is a markdown text")
st.write(1+2)


st.write(dir(st))
st.help(range)