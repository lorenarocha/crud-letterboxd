from services.db import DB_NAME, open_conn
import models.diary as diary

conn = open_conn()
con = conn.raw_connection()
cursor = con.cursor()
cursor.execute(f'USE {DB_NAME}')

def create(diary):
    insert = cursor.execute('INSERT INTO diary (Name, Rating, `Watched Date`, Rewatch) VALUES (%s, %s, %s, %s)',
                          (diary.name, diary.rating, diary.watched_date, diary.rewatch))
    cursor.commit()
    
    
def read():
    select = cursor.execute('SELECT * FROM diary')
    diarylist = []
    for row in cursor.fetchall():
        diarylist.append(diary.Diary(row[1],
                                     row[4],
                                     row[7],
                                     row[5]))
    return diarylist
    
