# Mtg Tournament scrapper
Python + fastapi + mysql + React + nginx

#### Database + api
> If you want to load a database, add .sql file on /data/ folder
- docker-compose build
- docker-compose up -d

#### Dumps
- /dump/clean_database
- /dump/last

#### Swagger
- http://localhost:8000/docs

#### React stats website
> Website to show the stats
- /react-website
- docker build -t react-website:1.0 .
- docker run -d -p 4000:80 --name react-website react-website:1.0 
- http://localhost:4000/

#### Scrapper
> If your database is empty you can run python scrapper to fill with data.
- /scrapper
- docker-compose build
- docker-compose up -d

#### References
- https://fastapi.tiangolo.com/
- https://hub.docker.com/
