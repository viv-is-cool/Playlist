import streamlit as st

st.set_page_config(
    page_icon="🎧",
    page_title="Download Instant Audio 🎶",
    layout="centered",
)


def set_background(url):
    page_bg_img = f"""
    <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set background image
set_background("https://bing.com/th/id/BCO.119f0310-be61-48e9-9f99-22f580d3c2d8.png")

st.title("All your songs with you wherever you go!")
st.divider()


st.subheader("Why use wifi or pay a fee to download your favorite songs! Just use Instant audio! Instant Audio can download all your favorite songs at once for free! ")

col_1, col_2 = st.columns([1, 1])

with col_1:
    st.subheader("Pros:")
    st.write("• Can download any song on youtube (with the exclustion of private and age Restricted videos)")
    st.write("• Takes only seconds for your songs to be in your hands so that you can have them on the go!")
    st.write("• Super lightweight so that any computer can handle it!")
    st.write("• Only 100mb which anyone can spare")
    st.write("All open sourced on github ---> (https://github.com/viv-is-cool/Instant-Audio)")

with col_2:
    st.subheader("Cons")
    st.write("• On windows and linux but not mac")

st.divider()

st.subheader("Best part is its totally free and you can download it with the button below!")

st.link_button("download Instant Audio, the solution to downloading songs here! ", "https://github.com/viv-is-cool/Instant-Audio/releases/download/v1.1.0/Instant.audio.zip")
