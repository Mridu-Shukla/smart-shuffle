# Smart-Shuffle Music Portal (SS Music)
It is a music recommendation system which uses **Collaborative Filtering Recommendation Algorithm** to help the user in creating their playlists based on their favourites.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Clone it
```
$ git clone [git_copy_url]
```

### Change directory
```
$ cd smart-shuffle
```

### Setup and activate a python virtual environment (perferrably in a folder outside your project)
```
$ virtualenv -p python3 venv
```
```
$ source venv/bin/activate
```

### Install dependencies
```
pip install Django
```
```
pip install pillow
```
### Make Django aware of models 
```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```
### Run the application
```
$ python manage.py runserver
```

## Built With

* **Django** - The web framework used
* **SPOTIFY API** - For getting Dataset


## Team

* **Mridu Shukla**
* **Rahul Bera**
* **Divyansh Jain**





