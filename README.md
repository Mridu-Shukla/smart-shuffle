# Smart-Shuffle Music Portal (SS Music)
It is a music recommendation system which uses **Collaborative Filtering Recommendation Algorithm** to help the user in creating their playlists based on their favourites.

The Dataset for project has been generated using the Spotipy, a Spotify API which provides all the songs in the playlists along with the 
audio features.

### Quick Start Guide
```bash
# clone the repository
$ git clone https://github.com/Mridu-Shukla/smart-shuffle.git

# Change directory
$ cd smart-shuffle

# Setup and activate a python virtual environment
$ virtualenv -p python venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Make Django db migrations 
$ python manage.py makemigrations
$ python manage.py migrate

# Launch server
$ python manage.py runserver
```

### Built With

* **Django** - The web framework used
* **SPOTIFY API** - For getting Dataset and playing the track





