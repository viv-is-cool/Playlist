import streamlit as st
import yt_dlp
import os
from pathlib import Path  

st.set_page_config(
    page_icon="🎧",
    page_title="playlist.com 🎶",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""
    <style>
    .glow-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 1vh;  /* Full viewport height */
    }
    .glow {
        font-size: 48px;
        color: #fff;
        text-shadow: 0 0 10px #00FFFF;
    }
    </style>
    <div class="glow-container">
        <div class="glow">🎧 Make your own playlist 🎶</div>
    </div>
""", unsafe_allow_html=True)

downloads_path = str(Path.home() / "Downloads")

def download_audio(url, quality):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        },
        'geo_bypass': True,  # Bypass regional restrictions
        'verbose': True,  # Enable detailed logs for debugging
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        st.error(f"❌ Failed to download {url}\nError: {e}")

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
set_background("https://images.unsplash.com/photo-1533109721025-d1*

