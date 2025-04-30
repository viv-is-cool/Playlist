def download_audio(url, quality):
    try:
        if not url.startswith("http"):
            st.warning(f"⚠️ Invalid URL skipped: {url}")
            return

        # Ensure downloads path exists
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)

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
            'ignoreerrors': True,
            'http_headers': {  # Add headers to mimic a browser
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.5',
            },
            'cookiefile': 'cookies.txt',  # Use cookies for restricted videos
        }

        # Debug logging
        st.write(f"Debug: Attempting to download URL: {url}")

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])

        if result == 0:
            st.success(f"✅ Successfully downloaded: {url}")
        else:
            st.error(f"❌ Failed to download {url}. Check if the URL is correct or restricted.")
    except yt_dlp.utils.DownloadError as e:
        st.error(f"❌ Download error for {url}: {str(e)}")
    except Exception as e:
        st.error(f"❌ Unexpected error for {url}: {str(e)}")
