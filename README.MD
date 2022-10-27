# DJANGO PROJECT

## Clone

git clone <project_url>

cd <project_url>

## Setup Virtual Env

python3 -m venv env

source env/bin/activate

python -m pip install -r requirements.txt

## install brew if not installed

/bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>)"

## install mongo on local server

brew tap mongodb/brew

brew update

brew install mongodb-community@6.0

brew services start mongodb-community@6.0

## install mongodb compass if you like

mongo compass makes data visualization easy

click on this link then install in your mac

<https://downloads.mongodb.com/compass/mongodb-compass-1.33.1-darwin-x64.dmg?_ga=2.125839433.594291216.1666847836-26054368.1665909771>

open compass then connect to localhost (usually it is already given there just click on connect)


## Run your project

cd snsweb
python manage.py runserver

you can go here to check if your website is running

<http://127.0.0.1:8000/>
