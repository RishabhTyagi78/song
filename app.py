import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import pyttsx3
import streamlit as st
import webbrowser

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()


def google_search(query, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': 'query',
        'key': 'AIzaSyB7YjWIqnFrT6kvpz24SscL3Si696qkAyM',
        'cx': '61da6ebd9518e4a60',
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Extract and print search results
        if 'items' in data:
            for item in data['items']:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                webbrowser.open(item['link'])
                print("\n")
                break
        else:
            print("No results found.")

    except Exception as e:
        print(f"Error: {e}")

def search(search_query):
    results = sp.search(q=search_query, type='track', limit=1)

    api_key = 'YOUR_GOOGLE_API_KEY'
    cx = 'YOUR_SEARCH_ENGINE_ID'

    # Extract relevant information from the search results
    if results['tracks']['items']:
        track_info = results['tracks']['items'][0]
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']
        track_id = track_info['id']
        
        print(f"Track: {track_name}")
        print(f"Artist: {artist_name}")
        query = f"spotify:track:{track_id}"
        
        # Generate Spotify embed URL
        embed_url = f"https://open.spotify.com/embed/track/{track_id}"
        
        return embed_url
    else:
        print("No results found.")
        return None

# Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Spotify application credentials
client_id = 'a0f8ce243f584f7e8bdfab4d5f36ea38'
client_secret = '25972c1dbfed4c1d944b436f4b23def1'

# Set up Spotify API credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Streamlit app
st.title('SONG SEARCH WEBSITE WITH SPOTIFY')
song = st.text_input("Enter song: ")

if st.button('search'):
    text_to_speech('searching for ' + song)
    embed_url = search(song)
    if embed_url:
        st.text("Playing the song:")
        st.markdown(f'<iframe src="{embed_url}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)
