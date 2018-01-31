import pymysql.cursors
from DBManager import DBManager


class UnivDBManager(DBManager):
    def __init__(self):
        DBManager.__init__(self)
        UnivDBManager.create_univ()
        return

    @staticmethod
    def create_univ():
        conn = pymysql.connect(host='localhost',
                               user=DBManager.USER,
                               password=DBManager.PW,
                               db='sookmyung',
                               charset='utf8mb4')

        with conn.cursor() as cursor:
            sql = '''
                   CREATE TABLE IF NOT EXISTS univ( 
                    id int(11) NOT NULL,
                    large_category varchar(50) NOT NULL,
                    small_category varchar(50) NOT NULL, 
                    title varchar(200) NOT NULL,
                    content varchar(5000)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
            '''
            cursor.execute(sql)
        return


    @staticmethod
    def insert(id, large_category, small_category, title, content):
        conn = pymysql.connect(host='localhost',
                               user=DBManager.USER,
                               password=DBManager.PW,
                               db='sookmyung',
                               charset='utf8mb4')

        with conn.cursor() as cursor:
            sql = 'INSERT INTO univ (id, large_category, small_category, title, content) VALUES (%s,%s,%s,%s,%s)'
            cursor.execute(sql, (str(id), large_category, small_category, title, content))
        conn.commit()
        # 1 (last insert id)
        return

    @staticmethod
    def select():
        conn = pymysql.connect(host='localhost',
                               user=DBManager.USER,
                               password=DBManager.PW,
                               db='sookmyung',
                               charset='utf8mb4')

        with conn.cursor() as cursor:
            sql = 'SELECT * FROM univ'
            cursor.execute(sql)
            conn.commit()
            result = cursor.fetchall()
            for row in result:
                print(row)
            # (1, 'test@test.com', 'my-passwd')
        return

    @staticmethod
    def delete_all():
        conn = pymysql.connect(host='localhost',
                               user=DBManager.USER,
                               password=DBManager.PW,
                               db='sookmyung',
                               charset='utf8mb4')

        with conn.cursor() as cursor:
            sql = 'DELETE FROM univ'
            cursor.execute(sql)
            conn.commit()
        return

