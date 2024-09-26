# Mtg Tournament scrapper
Mtg scrapper + fastapi + mysql

#### Database + api
> If you want to load a database, add .sql file on /data/ folder
- docker-compose build
- docker-compose up -d

#### Dumps
- /dump/clean_database/
- /dump/last/

#### Swagger
- http://localhost:8000/docs

#### Scrapper
> If your database is empty you can run python scrapper to fill with data.
- /scrapper
- docker-compose build
- docker-compose up -d

#### References
- https://fastapi.tiangolo.com/
- https://hub.docker.com/
