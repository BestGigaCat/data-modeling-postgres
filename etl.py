import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """

    Process data for song and artists

    :param cur: cursor
    :param filepath: song and artist file path
    """
    print("Loading file %s in process_song_file...\n", filepath)

    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    cur.execute(song_table_insert, (df['song_id'][0], df['title'][0], df['artist_id'][0], int(df['year'][0]), df['duration'][0]))

    # insert artist record
    cur.execute(artist_table_insert, (df['artist_id'][0], df['artist_name'][0], df['artist_location'][0], df['artist_latitude'][0], df['artist_longitude'][0]))


def process_log_file(cur, filepath):
    """

    Process log file.

    :param cur: cursor
    :param filepath: log file path
    """
    print("Loading file %s in process_log_file...\n", filepath)

    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # insert songplay records
    for index, row in df.iterrows():

        # insert into times table
        d = pd.to_datetime(row['ts'], unit='ms')
        cur.execute(time_table_insert, (row['ts'], d.hour, d.day, d.weekofyear, d.month, d.year, d.weekday()))

        # insert into user table
        cur.execute(user_table_insert, (row['userId'], row['firstName'], row['lastName'], row['gender'], row['level']))

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        cur.execute(songplay_table_insert, (row['ts'], row['userId'], row['level'], songid, artistid, row['sessionId'], row['location'], row['userAgent']))


def process_data(cur, conn, filepath, func):
    """
    Generic data processing function for inserting data to all tables.

    :param cur: cursor
    :param conn: db connection
    :param filepath: file path where the data to be inserted stays
    :param func: data processing function
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
