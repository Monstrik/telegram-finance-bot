#Telegram Expenses Bot


Env vars

`TELEGRAM_API_TOKEN` — Bot token

`TELEGRAM_ACCESS_ID` — Telegram user Id


###Docker:
add ENV values to Dockerfile, 

set local dir instead `local_project_path`. 
SQLite will be created: `db/finance.db`.

```
docker build -t tgfinance ./
docker run -d --name tg -v /local_project_path/db:/home/db tgfinance
```

Container:

```
docker exec -ti tg bash
```

SQL:

```
docker exec -ti tg bash
sqlite3 /home/db/finance.db
```


