import psycopg2
import os.path


def read_from_txt():
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'user.txt')
    data = []
    with open(filename) as f:
        for l in f.readlines():
            content = l.strip("\n")
            data.append(content)
        return data

conn_data = read_from_txt()


class Db_connect():

    # setup connection string
    connect_str = "dbname=" + conn_data[0] + " user=" + conn_data[1] + " host='localhost' password=" + conn_data[2]
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()


class Client(Db_connect):

    @classmethod
    def client_data(cls):
        cls.cursor.execute("SELECT company_name, COUNT(company_name) AS oszlopok FROM project GROUP BY company_name;")
        rows = cls.cursor.fetchall()
        # for i in rows:
        #     print(i)
        return rows

# print(Client.client_data())
