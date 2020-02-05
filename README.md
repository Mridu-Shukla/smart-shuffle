# Smart-Shuffle Music Portal (SS Music)

Please follow the following initial steps to use the project

# Clone it
$ git clone [copy_url]

# Change directory
$ cd vpropel-v2


# Setup and activate a python virtual environment (perferrably in a folder outside your project)
$ virtualenv -p python3 venv
$ source venv/bin/activate

# Install dependencies

install Django within venv

# Make Django aware of models 
$ python manage.py makemigrations
$ python manage.py migrate

# Run the application
$ python manage.py runserver
