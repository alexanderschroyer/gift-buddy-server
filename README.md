# Gift Buddy API

Gift Buddy is an application made to allow a user to create recipients/buddies which they can then add interests and gift ideas they are told, or casually picked up in conversation. The user can then search gift ideas and see a google shopping results they can navigate.

## Local Setup

1. Clone this repository (github.com/alexanderschroyer/gift-buddy-server) and then cd into the directory in your terminal.
2. Run `pipenv shell` in the main directory. 
3. Run `pipenv install`.
4. Run `makemigrations` and then `migrations`

### Seed Database

Run `python3 manage.py loaddata` <table name>

1. recipients
2. interests
3. recipientinterests

Now run `python3 manage.py runserver`

### Gift Buddy ERD

https://drawsql.app/nss-4/diagrams/gift-buddy#

### Gift Buddy Moqup

https://app.moqups.com/wTguXyETSOHfi49OvlDWONsZC1yutxmQ/edit/page/ad64222d5

### Documentation

1. Register a new user to login.
2. Select Buddies and then select `create buddy`.
3. Enter a recpient name and select some prepopulated interests.
4. You can add more by editing the buddy.
