import streamlit as st

import pandas as pd

# Read csv
df = pd.read_csv("iris.csv")


st.markdown("### Display Data")

## 1.  Scrollable table
st.dataframe(df)

	# Modify height and width of table
st.dataframe(df, 200, 100)	# very small size

## Adding a color style from pandas
st.dataframe(df.style.highlight_max(axis=0))

## 2. Static table
# st.table(df)

## 3. Using superfunction st.write
st.write(df.head())


## Display JSON
st.json({'data': 'name'})

## Display Code
mycode = """
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
"""

st.code(mycode, language='ruby')