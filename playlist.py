import os
import yt_dlp
import streamlit as st

# Define the function to download audio
def download_audio(url, quality):
    try:
        # Validate URL
        if not url.startswith("http"):
            st.warning(f"⚠️ Invalid URL skipped: {url}")
            return

        # Ensure downloads folder exists
        downloads_path = "downloads"
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)

        # yt_dlp options
        ydl_opts = {
            'format': 'bestaudio/best',  # Choose the best available audio
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),  # Save in the downloads folder
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extract audio using FFmpeg
                'preferredcodec': 'mp3',  # Convert to MP3
                'preferredquality': quality,  # Set bitrate quality
            }],
            'cookiefile': 'cookies.txt',  # Use cookies for restricted videos
            'quiet': False,
            'verbose': True,
            'ignoreerrors': True,
            'http_headers': {  # Add headers to mimic a browser
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.5',
            },
        }

        # Debug logging for the user
        st.write(f"Debug: Attempting to download URL: {url}")

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])

        # Check for success or failure
        if result == 0:
            st.success(f"✅ Successfully downloaded: {url}")
        else:
            st.error(f"❌ Failed to download {url}. Check if the URL is correct or restricted.")
    except yt_dlp.utils.DownloadError as e:
        st.error(f"❌ Download error for {url}: {str(e)}")
    except Exception as e:
        st.error(f"❌ Unexpected error for {url}: {str(e)}")

# Main function for the Streamlit app
if __name__ == "__main__":
    # Set the Streamlit title
    st.title("YouTube Audio Downloader 🎵")

    # Input field for the YouTube URL
    video_url = st.text_input("Enter YouTube video URL:")

    # Dropdown menu for selecting audio quality
    quality = st.selectbox("Select audio quality (kbps):", ["192", "256", "320"], index=0)

    # Button to trigger the download
    if st.button("Download"):
        download_audio(video_url, quality)
