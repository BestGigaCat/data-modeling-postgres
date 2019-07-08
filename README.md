# Data Modeling with Postgres for music play data

## DBs

![DBs](./images/DBs.png) 

## How to run the project

Create DB and Tables: 

```
python3 create_tables.py
```

Load Tables: 

```
python3 etl.py
```

## Check DB loads manually

Connect to sparkifydb:

```
psql sparkifydb
```

List the table you want to check:

```
SELECT count(*) from users;
```
