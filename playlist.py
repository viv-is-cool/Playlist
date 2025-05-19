import os
import streamlit as st
import yt_dlp
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_icon="🎧",
    page_title="Playlist.com 🎶",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add custom CSS for styling
st.markdown("""
    <style>
    .glow-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 1vh;
    }
    .glow {
        font-size: 48px;
        color: #fff;
        text-shadow: 0 0 10px #00FFFF;
    }
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1533109721025-d1ae7ee7c1e1?q=80&w=3270&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    <div class="glow-container">
        <div class="glow">🎧 Make your own playlist 🎶</div>
    </div>
""", unsafe_allow_html=True)

# Downloads path
downloads_path = str(Path.home() / "Downloads")

# Ensure downloads folder exists
if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)

# Function to download audio
def download_audio(url, quality):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            }],
            'quiet': False,
            'verbose': True,
            'ignoreerrors': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        st.error(f"❌ Download error for {url}: {str(e)}")
    except Exception as e:
        st.error(f"❌ Unexpected error for {url}: {str(e)}")

# Sidebar options
st.sidebar.title("Options")
st.sidebar.divider()
button_1 = st.sidebar.button("Show copyable playlist")
button_2 = st.sidebar.button("Hide copyable playlist")
st.sidebar.divider()
code = st.sidebar.text_input("Enter code!", type="password")
st.sidebar.divider()

# Author info
if code == "Vivaan_27":
    st.write("Hello, website creator!")
elif code == "ULTRAFUNK":
    st.audio("videoplayback.mp4", format="audio/wav", loop=True, autoplay=True)
elif code == "Friend_27":
    st.write("Hello, Vivaan's friends!")
elif code == "Brother_27":
    st.write("Hello, Vivaan's brother!")

# Playlist input
if "Song_playlist" not in st.session_state:
    st.session_state.Song_playlist = []

col_1, col_2 = st.columns([1, 1])
with col_1:
    add_song = st.button("Add song URL")
    if add_song:
        st.session_state.Song_playlist.append("")
with col_2:
    if st.button("Delete last song"):
        if st.session_state.Song_playlist:
            st.session_state.Song_playlist.pop()

# Display playlist
for index, song in enumerate(st.session_state.Song_playlist):
    st.session_state.Song_playlist[index] = st.text_input(f"Song {index + 1} URL", value=song, key=f"song_{index}")

# Quality selector
if "advanced_clicked" not in st.session_state:
    st.session_state.advanced_clicked = False

with st.expander("🎚 Select Audio Quality"):
    quality_option = st.radio("Choose download quality:", ["High (320 kbps)", "Medium (256 kbps)", "Low (192 kbps)"])
    quality = "320" if "High" in quality_option else "256" if "Medium" in quality_option else "192"
    if st.button("Show advanced options"):
        st.session_state.advanced_clicked = True
    if st.button("Hide advanced options"):
        st.session_state.advanced_clicked = False
    if st.session_state.advanced_clicked:
        y = st.slider("Choose your custom quality", min_value=64, max_value=320, value=int(quality))
        quality = str(y)

# Download button
if st.sidebar.button("Download all songs"):
    with st.spinner("🔍 Downloading your songs..."):
        for url in st.session_state.Song_playlist:
            if url.startswith("http"):
                try:
                    download_audio(url, quality)
                    st.success(f"✅ Downloaded: {url}")
                    st.audio("Ding_Sound_Effect.mp3", format="audio/mp3", autoplay=True)
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Failed to download {url}\nError: {e}")
            else:
                st.warning(f"⚠️ Skipped invalid URL: {url}")

# Show/hide playlist
if button_1:
    st.write("Your Playlist is:", st.session_state.Song_playlist)


st.sidebar.write("download the working version here for free:  https://github.com/viv-is-cool/Instant-Audio  ")
