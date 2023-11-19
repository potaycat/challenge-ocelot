## Simple Bookstore

Hi! The Bookstore API is made for the coding challenge.


## Setting up and running locally

*Usage of virtualenv is recomended*
```sh
python -m venv venv
./venv/bin/activate
```

Install dependancies:
```sh
pip install -r ./requirements.txt
```

No database migration needed. Start the project:
```sh
python ./manage.py runserver
```

## Pack and deploy
Install `flyctl` to deploy the app to Fly.io
```sh
flyctl deploy
```
Curently deployed and live at https://challenge-ocelot--longnh.fly.dev/



## API functionalities

- CRUD operations for Books
- User account creation, authentication
- S3 upload for images
- A faster endpoint

## API specification
https://challenge-ocelot--longnh.fly.dev/swagger/