# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL, 
        start_time BIGINT NOT NULL, 
        user_id INT NOT NULL, 
        level VARCHAR(255), 
        song_id VARCHAR(255), 
        artist_id VARCHAR(255), 
        session_id VARCHAR(255), 
        location VARCHAR(255), 
        user_agent VARCHAR(255),
        PRIMARY KEY (songplay_id));
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT, 
        first_name VARCHAR(255), 
        last_name VARCHAR(255), 
        gender VARCHAR(255), 
        level VARCHAR(255),
        PRIMARY KEY (user_id));
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR(255), 
        title VARCHAR(255), 
        artist_id VARCHAR(255), 
        year INT, 
        duration DOUBLE,
        PRIMARY KEY (song_id));
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(255), 
        name VARCHAR(255), 
        location VARCHAR(255), 
        lattitude DOUBLE, 
        longitude DOUBLE,
        PRIMARY KEY (artist_id));
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time BIGINT, 
        hour INT, 
        day INT, 
        week INT, 
        month INT, 
        year INT, 
        weekday INT,
        PRIMARY KEY (start_time));
""")

# INSERT RECORDS

songplay_table_insert = ("""

""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
