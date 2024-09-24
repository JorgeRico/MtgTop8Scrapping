# Mtg Tournament scrapper
Mtg scrapper

#### Execute app
```bash
1. Build and run docker - Database + api
2. Execute python on terminal to fill database
```

#### Build
```bash
 - docker-compose build
```

#### Run
```bash
 - docker-compose up -d
```

#### Run scrapper
```bash
 - python app.py
```

#### Endpoints
```bash
 - GET http://localhost:8000/leagues/{id}/tournaments
 - GET http://localhost:8000/tournaments/{id}
 - GET http://localhost:8000/tournaments/{id}/stats
 - GET http://localhost:8000/tournaments/{idTournament}/players/{idPlayer}/decks
```
