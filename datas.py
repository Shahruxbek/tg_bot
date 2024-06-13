import sqlite3


async def start_db():
    global db,cursor
    db = sqlite3.connect('my_db.db')
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tel(
               name TEXT,
               pamet INTEGER,
               operativ INTEGER,
               dyum INTEGER,
               color TEXT,
               pixel TEXT,
               year INTEGER,
               sena TEXT,
               photo TEXT
    
    )
               ''')
    

async def add_to_db(ati,xotira,operat,ulkenligi,reni,kam,jili,cena,photo):
    cursor.execute('''
    INSERT INTO tel(
                name,pamet,operativ,dyum,color,pixel,year,sena,photo
    )
                VALUES(?,?,?,?,?,?,?,?,?)


    ''',(ati,xotira,operat,ulkenligi,reni,kam,jili,cena,photo))
    db.commit()

async def  show_datas():
    cursor.execute('SELECT * FROM tel')
    datas = cursor.fetchall()
    return datas
