import pandas as pd
import sqlite3
import os


if __name__ == '__main__':
    # Create dataframe:
    df = pd.DataFrame(data={
     's':['g', 'v', 'f'],
     'x':[3, 5, 8],
     'y':[9, 7, 7]})
    print("New dataframe:\n" + str(df.head()))

    # Create new sqlite3 file
    FILEPATH = os.path.dirname(__file__)
    DB_FILEPATH = os.path.join(FILEPATH, "demo_data.sqlite3")
    connection = sqlite3.connect(DB_FILEPATH)
    cursor = connection.cursor()
    
    query = """
    CREATE TABLE IF NOT EXISTS challenge (
        s varchar,
        x int,
        y int
    );
    """

    cursor.execute(query)

    print("Checking database for currently existing data...")
    cursor.execute("SELECT * from challenge;")
    result = cursor.fetchall()
    if len(result) == 0:
        print("No data in database. Filling it up!")
        rows = list(df.itertuples(index=False, name=None))
        insertion_query = """
        INSERT INTO challenge VALUES (?, ?, ?)
        """
        cursor.executemany(insertion_query, rows)
    else:
        print("Looks like the data is already there!")
    
    connection.commit()

    print("\nQuestion: Count how many rows you have - it should be 3!")
    query = """
    SELECT COUNT(*) FROM challenge
    """
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print("ANSWER:", result)

    print("\nQuestion: How many rows are there where both x and y are at least 5?")
    query = """
    SELECT COUNT(*) FROM challenge
    WHERE x >= 5 AND y >= 5
    """
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print("ANSWER:", result)
    
    print("\nQuestion: How many unique values of y are there ?")
    query = """
    SELECT COUNT(DISTINCT y) FROM challenge
    """
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print("ANSWER:", result)
