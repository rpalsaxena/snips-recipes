import streamlit as st

### Set page title, headers 
# st.set_page_config(page_title="hello rahul",
# 					page_icon = ":smiley::heart:",
# 					layout="wide",
# 					initial_sidebar_state = "auto" #auto / expanded/ collapsed
# 					)


## Another method is to create a dict and pass to set_page_config
page_config = {
	"page_title": "Hello",
	"page_icon": ":smiley:"
}
st.set_page_config(**page_config)


def main():
	"""
	implement all the code here
	"""
	st.title("Hello Streamlit Lovers ❤️ 😃 ")
	st.sidebar.success("Menu")
	st.sidebar.write("Rahul")
	st.sidebar.warning("Warn")


if __name__ == "__main__":
	main()