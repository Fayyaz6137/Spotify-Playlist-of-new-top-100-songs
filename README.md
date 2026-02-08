# 🎵 Billboard Hot 100 to Spotify Playlist

Create a **Spotify playlist** containing the **Billboard Hot 100 songs** for any date in history using Python automation.

This script scrapes Billboard’s Hot 100 chart for a given date, searches the tracks on Spotify, and automatically creates a **private playlist** in your Spotify account.

---

## 🚀 Features

- Scrapes **Billboard Hot 100** chart data for a specific date
- Searches songs using the **Spotify Web API**
- Automatically creates a **new private Spotify playlist**
- Adds the matched tracks to the playlist
- Uses OAuth for secure authentication

---

## 🛠 Tech Stack

- **Python**
- **Requests** – HTTP requests
- **BeautifulSoup** – Web scraping
- **Spotipy** – Spotify Web API wrapper
- **python-dotenv** – Environment variable management

---

## 📂 Project Structure

```bash
spotify-playlist-creator/
├── spotify_playlist_creator.py  # Main script
├── Dockerfile
├── docker-compose.yml
├── .env                         # Spotify credentials
├── README.md
└── requirements.txt     
```

## ⚡ Setup and Usage

1. Install dependencies:

```bash
git clone https://github.com/Fayyaz6137/Spotify-Playlist-of-new-top-100-songs.git

cd Spotify-Playlist-of-new-top-100-songs

pip install -r requirements.txt
```

2. Create a .env file in the project root:

```bash
CLIENT_ID=your_spotify_client_id

CLIENT_SECRET=your_spotify_client_secret
```

3. Run the script locally:

```bash
python main.py
```

---

## 🐳 Run With Docker

```bash
docker compose up --build
```
The script reads .env variables for API keys.

---

## ⚠️ Notes

* Make sure your Spotify app has the correct redirect URI (http://127.0.0.1:8888/callback) set in your Spotify Developer Dashboard.
* The script currently limits to 4 songs for testing; you can remove the if counter > 4: break line to process all top 100 tracks.

---

## 📌 References

- [Billboard Hot 100](https://www.billboard.com/charts/hot-100/)
- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)





