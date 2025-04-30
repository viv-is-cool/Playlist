import streamlit as st
import yt_dlp
import os
from pathlib import Path

# Streamlit app configuration
st.set_page_config(
    page_icon="🎧",
    page_title="playlist.com 🎶",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add glowing title and background CSS
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

# Path for downloads
downloads_path = str(Path.home() / "Downloads")

# Function to download audio
def download_audio(url, quality):
    try:
        # Ensure downloads path exists
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)

        # Clean the URL (remove timestamps)
        clean_url = url.split('?')[0]

        # yt_dlp options
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
            'ignoreerrors': True,  # Continue even if some videos fail
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([clean_url])

        st.success(f"✅ Successfully downloaded: {clean_url}")
    except Exception as e:
        st.error(f"❌ Failed to download {url}\nError: {e}")

# Sidebar options
st.sidebar.title("Options")
st.sidebar.divider()
button_1 = st.sidebar.button("Show copyable playlist")
button_2 = st.sidebar.button("Hide copyable playlist")
st.sidebar.divider()
code = st.sidebar.text_input("Enter code!", type="password")
st.sidebar.divider()

# Authorization logic
if code == "Vivaan_27":
    st.write("Hello, website creator!")

if code == "ULTRAFUNK":
    st.audio("videoplayback.mp4", format="audio/wav", loop=True, autoplay=True)

if code == "Friend_27":
    st.write("Hello, Vivaan's friends!")

if code == "Brother_27":
    st.write("Hello, Vivaan's brother!")

# Download all songs button
download = st.sidebar.button("Download all songs")
st.sidebar.divider()
name = st.sidebar.text_input("Name your playlist here")
if name != "":
    st.subheader(name)
st.sidebar.divider()
st.sidebar.write("Rate Us")
st.sidebar.divider()
selected = st.sidebar.feedback("stars")
if selected is not None:
    st.sidebar.write("Thank you for rating us!")

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

for index, song in enumerate(st.session_state.Song_playlist):
    st.session_state.Song_playlist[index] = st.text_input(f"Song {index + 1} URL", value=song, key=f"song_{index}")

# Quality selector and estimates
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

    # Show estimated file size and download time
    avg_minutes = 4
    bitrate_kbps = int(quality)
    est_size_MB = round((bitrate_kbps * 1000 / 8 * avg_minutes * 60) / (1024 * 1024), 2)
    download_speed_mbps = 5  # Assume 5 Mbps download speed
    download_speed_Bps = download_speed_mbps * 125000
    est_time_sec = round((est_size_MB * 1024 * 1024) / download_speed_Bps, 1)

    st.info(f"📦 Estimated file size per song: {est_size_MB} MB")
    st.info(f"⏱️ Lowest download time per song: {est_time_sec} seconds")
    st.info("If your speeds are slower than these, something is wrong.")

# Download logic
if download:
    with st.spinner("🔍 Downloading your songs..."):
        for url in st.session_state.Song_playlist:
            if url.startswith("http"):
                try:
                    download_audio(url, quality)
                    st.audio("Ding_Sound_Effect.mp3", format="audio/mp3", autoplay=True)
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Failed to download {url}\nError: {e}")
            else:
                st.warning(f"⚠️ Skipped invalid URL: {url}")

# Show/hide playlist
if button_1:
    st.write("Your Playlist is:", st.session_state.Song_playlist)
