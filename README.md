# Smart-Shuffle Music Portal (SS Music)
It is a music recommendation system which uses **Collaborative Filtering Recommendation Algorithm** to help the user in creating their playlists based on their favourites.


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
$ pip install Django
$ pip install pillow

# Make Django db migrations 
$ python manage.py makemigrations
$ python manage.py migrate

# Launch server
$ python manage.py runserver
```

### Built With

* **Django** - The web framework used
* **SPOTIFY API** - For getting Dataset and playing the track





