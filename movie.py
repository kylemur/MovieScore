import sqlite3

def create_connection():
    conn = sqlite3.connect('movies.db')
    return conn

def create_table(conn):
    sql_create_movies_table = """
    CREATE TABLE IF NOT EXISTS movies (
        title TEXT NOT NULL PRIMARY KEY,
        score INTEGER,
        runtime INTEGER,
        release_year INTEGER,
        rated TEXT,
        genre TEXT,
        director TEXT,
        actors TEXT
    );
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_movies_table)
    except sqlite3.Error as e:
        print(e)

def insert_movie(conn, title, score, runtime=None, release_year=None, rated=None, genre=None, director=None, actors=None):
    sql = ''' INSERT INTO movies(title, score, runtime, release_year, rated, genre, director, actors)
              VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (title, score, runtime, release_year, rated, genre, director, actors))
    conn.commit()
    return cur.lastrowid

def is_title(conn, title):
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM movies WHERE title=?", (title,))
    return cur.fetchone() is not None

def update_movie(conn, title, score=None, runtime=None, release_year=None, rated=None, genre=None, director=None, actors=None):
    sql = ''' UPDATE movies
              SET score = ?
              SET runtime = ?
              SET release_year = ?
              SET rated = ?
              SET genre = ?
              SET director = ?
              SET actors = ?
              WHERE title = ?'''
    cur = conn.cursor()
    cur.execute(sql, (title, score, runtime, release_year, rated, genre, director, actors))
    conn.commit()

def delete_movie(conn, title):
    sql = 'DELETE FROM movies WHERE title=?'
    cur = conn.cursor()
    cur.execute(sql, (title,))
    conn.commit()

def display_all_movies(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def get_average_score(conn):
    cur = conn.cursor()
    cur.execute("SELECT AVG(score) FROM movies")
    return cur.fetchone()[0]

def get_movie_count(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM movies")
    return cur.fetchone()[0]


def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)

        option = 0

        m_title = ''
        m_runtime = 0
        m_release_year = 0
        m_rated = ''
        m_genre = ''
        m_director = ''
        m_actors = ''
        m_score = 0

        while option != 7:
            print('\n---Menu---')
            print('1. Insert a movie')
            print("2. Update a movie's data")
            print('3. Delete a movie')
            print('4. Display all movie data')
            print('5. Get average score')
            print('6. Get movie count')
            print('7. Exit')
            option = int(input('Enter option: '))
            print()

            if option == 1: # Insert movies
                m_title = input('Enter movie title: ')
                m_score = int(input('Enter movie score: '))
                m_runtime = int(input('Enter movie runtime: '))
                m_release_year = int(input('Enter movie release year: '))
                m_rated = input('What is the movie rated: ')
                m_genre = input('Enter movie genre: ')
                m_director = input('Enter movie director: ')
                m_actors = input('Enter movie actors: ')
                insert_movie(conn, m_title, m_score, m_runtime, m_release_year, m_rated, m_genre, m_director, m_actors)
            
            elif option == 2: # Update a movie
                m_title = input('Enter movie title: ')
                if is_title(conn, m_title):
                    m_score = int(input('Enter movie score: '))
                    m_runtime = int(input('Enter movie runtime: '))
                    m_release_year = int(input('Enter movie release year: '))
                    m_rated = input('What is the movie rated: ')
                    m_genre = input('Enter movie genre: ')
                    m_director = input('Enter movie director: ')
                    m_actors = input('Enter movie actors: ')
                    update_movie(conn, m_title, m_score, m_runtime, m_release_year, m_rated, m_genre, m_director, m_actors)
                else:
                    print('Movie not found.')
            
            elif option == 3: # Delete a movie
                m_title = input('Enter movie title: ')
                if is_title(conn, m_title):
                    delete_movie(conn, m_title)
                    print(f'{m_title} deleted.')
                else:
                    print('Movie not found.')
            
            elif option == 4: # Display all movies
                display_all_movies(conn)
            
            elif option == 5: # Get average score
                average_score = get_average_score(conn)
                print(f"Average score: {average_score: .2f}")
            
            elif option == 6: # Get movie count
                print("Total movies:", get_movie_count(conn))

            elif option == 7: # Exit
                print('Goodbye!')
                conn.close()

            else:
                print('Invalid option. Please try again.\n')
        
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()