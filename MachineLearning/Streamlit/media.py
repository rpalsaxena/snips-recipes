import streamlit as st

## Let's try some videos/images/audio files


## Plot images
from PIL import Image
import urllib.request

urllib.request.urlretrieve(
	"https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
	"image.png"
	)
img = Image.open("image.png")

st.image(img, use_column_width=True)


### To directly load image from url
st.image("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")


############################################
####          VIDEO FILE                 ###
############################################

st.video("https://www.youtube.com/watch?v=Irw8llgSC3s", start_time=100)

## Display Audio/ Working with Audio

st.audio("http://commondatastorage.googleapis.com/codeskulptor-assets/week7-brrring.m4a")

