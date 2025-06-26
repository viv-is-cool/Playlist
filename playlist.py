import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Download Instant Audio", page_icon="https://bing.com/th/id/BCO.28aa445c-2071-40ea-986c-c5c97734fbb1.png", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/639374f7-8061-4072-954d-7ffedb7c8859/TSsO5f8zpK.json")

# ---- HEADER SECTION ----
with st.container():
    

    st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, teal, deepskyblue, mediumseagreen);
        padding: 40px;
        border-radius: 8px;
        color: black;
        font-size: 60px;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 20px 10px rgba(0, 0, 0, 0.15);">
        🎧 Introducing Instant Audio 🎶
    </div>
    """,
    unsafe_allow_html=True
)





st.title("Listen to all your songs on the go")
st.write("Why use wifi or pay a fee to download your favorite songs! Just use Instant audio! Instant Audio can download all your favorite songs at once for free! ")
st.write("best part its totally free")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What Instant Audio does")
        st.write("##")
        st.write(
            """
🎧 Instant Audio is your ultimate solution for fast, reliable, and hassle-free music downloads from YouTube. Designed with simplicity and performance in mind, this lightweight tool empowers users to access their favorite tracks within seconds—no waiting, no clutter, just instant gratification.

Whether you're building a playlist for offline listening or archiving rare audio, Instant Audio delivers unmatched speed and clarity without demanding much from your system. With a footprint of just 100MB, it runs effortlessly on virtually any computer, making it the ideal companion for students, travelers, creators, and casual listeners alike.

What sets Instant Audio apart? It’s completely open source. Developers and curious minds can explore the code, contribute improvements, or integrate it into custom workflows. This transparency builds trust and fosters a community that believes in accessible, high-quality tools for everyone

Whether you're commuting, studying, or creating, Instant Audio makes sure your music is never more than a few clicks away!
"""
)
st.divider()

with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

cola, colb, colc = st.columns(3)
with colb:

    


    st.markdown("""
    <style>
    .download-box {
        background: linear-gradient(135deg, #3a0ca3, #4361ee, #4cc9f0);
        padding: 32px;
        border-radius: 18px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.3);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        margin: 40px 0;
    }

    .download-box h2 {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .download-box p {
        font-size: 17px;
        line-height: 1.6;
        margin-bottom: 28px;
    }

    .download-box a.download-btn {
        display: inline-block;
        padding: 20px 40px;
        background: rgba(255, 255, 255, 0.15);
        color: white;
        font-size: 20px;
        font-weight: 600;
        border-radius: 10px;
        text-decoration: none;
        transition: all 0.3s ease;
        margin-left: 125px
    }

    .download-box a.download-btn:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
    }
    </style>

    <div class="download-box">
        <h2> Ready to download?</h2>
        <p>
            click the button below to start the download! or scroll down to learn more
        </p>
        <a href="https://github.com/viv-is-cool/Instant-Audio/releases/download/v1.1.0/Instant.audio.zip" class="download-btn" target="_blank">
            🚀 Download Now
        </a>
    </div>
""", unsafe_allow_html=True)
    






with cola:

    
    st.markdown("""
    <style>
    .instant-audio-box {
        background: linear-gradient(135deg, #3a0ca3, #4361ee, #4cc9f0);
        padding: 32px;
        border-radius: 18px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.3);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        margin: 40px 0;
    }

    .instant-audio-box h2 {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .instant-audio-box p {
        font-size: 17px;
        line-height: 1.6;
        margin-bottom: 28px;
    }

    </style>

    <div class="instant-audio-box">
        <h2> still not Ready to download?</h2>
        <p>
           ⬇️ scroll down to find out more! 
        </p>
    </div>
""", unsafe_allow_html=True)


with colc:

    
    st.markdown("""
    <style>
    .instant-audio-box {
        background: linear-gradient(135deg, #3a0ca3, #4361ee, #4cc9f0);
        padding: 32px;
        border-radius: 18px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.3);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        margin: 40px 0;
    }

    .instant-audio-box h2 {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .instant-audio-box p {
        font-size: 17px;
        line-height: 1.6;
        margin-bottom: 28px;
    }

    </style>

    <div class="instant-audio-box">
        <h2> still not Ready to download?</h2>
        <p>
            scroll down to find out more! 	⬇️
        </p>
    </div>
""", unsafe_allow_html=True)





st.divider()

st.markdown("""
    <style>
    .instant-audio-box {
        background: linear-gradient(135deg, #3a0ca3, #4361ee, #4cc9f0);
        padding: 32px;
        border-radius: 18px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.3);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        margin: 40px 0;
    }

    .instant-audio-box h2 {
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }

    .instant-audio-box p {
        font-size: 17px;
        line-height: 1.6;
        margin-bottom: 28px;
    }

    </style>

    <div class="instant-audio-box">
        <h2> ⬇️   And the best part is!  ⬇️ </h2>
    </div>
""", unsafe_allow_html=True)

st.divider()
col1, col2, col3, = st.columns(3)


with col1:
    st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, teal, deepskyblue, mediumseagreen);
        padding: 40px;
        border-radius: 8px;
        color: black;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 20px 10px rgba(0, 0, 0, 0.15);">
        Can download any song on YouTube
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
        st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, teal, deepskyblue, mediumseagreen);
        padding: 40px;
        border-radius: 8px;
        color: black;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 20px 10px rgba(0, 0, 0, 0.15);">
        Takes only seconds for your songs to be in your hands
    </div>
    """,
    unsafe_allow_html=True
)
        

with col3:
        st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, teal, deepskyblue, mediumseagreen);
        padding: 40px;
        border-radius: 8px;
        color: black;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 20px 10px rgba(0, 0, 0, 0.15);">
        Super lightweight so that any computer can handle it 
    </div>
    """,
    unsafe_allow_html=True
)

col_one, col_two = st.columns(2)

with col_one:
        st.divider()
        st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, teal, deepskyblue, mediumseagreen);
        padding: 40px;
        border-radius: 8px;
        color: black;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 20px 10px rgba(0, 0, 0, 0.15);">
        Only 100MB which anyone can spare 
    </div>
    """,
    unsafe_allow_html=True
        )


with col_two:
        st.divider()
        st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, teal, deepskyblue, mediumseagreen);
        padding: 40px;
        border-radius: 8px;
        color: black;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 20px 10px rgba(0, 0, 0, 0.15);">
        All open sourced on GitHub 
    </div>
    """,
    unsafe_allow_html=True
        )


st.divider()
st.markdown(
    """
<div style="
    background: linear-gradient(90deg, teal, deepskyblue, mediumseagreen);
    padding: 20px;
    border-radius: 8px;
    color: black;
    font-size: 40px;
    font-weight: 600;
    text-align: center;
    box-shadow: 0 20px 10px rgba(0, 0, 0, 0.15);">
    100% Free! 
</div>
""",
unsafe_allow_html=True
    )


st.markdown("""
    <style>
    .instant-audio-box {
        background: linear-gradient(135deg, #3a0ca3, #4361ee, #4cc9f0);
        padding: 32px;
        border-radius: 18px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.3);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        margin: 40px 0;
    }

    .instant-audio-box h2 {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px; 
    }

    .instant-audio-box p {
        font-size: 17px;
        line-height: 1.6;
        margin-bottom: 28px;
        text-align: center;
    }

    .instant-audio-box a.button {
        display: inline-block;
        padding: 20px 40px;
        background: rgba(255, 255, 255, 0.15);
        color: white;
        font-size: 20px;
        font-weight: 600;
        border-radius: 10px;
        text-decoration: none;
        transition: all 0.3s ease;
        margin-left: 825px;
            
    }

    .instant-audio-box a.button:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
    }
    </style>

    <div class="instant-audio-box">
        <h2> Ready to download?</h2>
        <p>
            click the button below to start the download!
        </p>
        <a href="https://github.com/viv-is-cool/Instant-Audio/releases/download/v1.1.0/Instant.audio.zip" class="button" target="_blank">
            🚀 Download here
        </a>
    </div>
""", unsafe_allow_html=True)
