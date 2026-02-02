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

```text
.
├── main.py
├── requirements.txt
├── .env.example
└── README.md

````

## ⚙️ Installation & Setup

1. Clone the repository
   ```text

   git clone <YOUR_GITHUB_REPO_URL>
   cd billboard-spotify-playlist

2. Create and activate a virtual environment (recommended)
   ```text

   python -m venv venv

   macOS / Linux:
   source venv/bin/activate

   Windows:
   venv\Scripts\activate

3. Install dependencies
   ```text

   pip install -r requirements.txt
   
    ```

   requirements.txt contents:
    ```text

   beautifulsoup4==4.14.2
   requests==2.32.5
   spotipy==2.25.2
   python-dotenv==1.1.1

4. Configure Spotify Developer Dashboard

   - Go to: https://developer.spotify.com/dashboard
   - Create a new application
   - Add the following Redirect URI:
    ```text

     http://127.0.0.1:8888/callback

5. Set up environment variables

   Create a .env file in the project root:
    ```text

   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
    
     ```

   Do NOT commit the .env file to GitHub.

6. Run the application
    ```text

   python main.py
    
     ```
   When prompted, enter the date in the following format:

   YYYY-MM-DD

   A private Spotify playlist will be created automatically in your account.



