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


class Database():

    # setup connection string
    connect_str = "dbname=" + conn_data[0] + " user=" + conn_data[1] + " host='localhost' password=" + conn_data[2]
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    @staticmethod
    def hex_to_rgb(value):
        if value is not None:
            value = value.lstrip('#')
            lv = len(value)
            if lv == 1:
                v = int(value, 16)*17
                return v, v, v
            if lv == 3:
                return tuple(int(value[i:i+1], 16)*17 for i in range(0, 3))
            return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))
        else:
            return (0, 0, 0)

    @classmethod
    def get_client_and_number_of_projects(cls):
        cls.cursor.execute("SELECT company_name, COUNT(company_name) FROM project GROUP BY company_name;")
        rows = cls.cursor.fetchall()
        # for i in rows:
        #     print(i)
        return rows

    @classmethod
    def get_client_colors(cls):
        # returns colors by company
        cls.cursor.execute("SELECT company_name, main_color FROM project;")
        colors = cls.cursor.fetchall()
        client_colors = []
        for i in colors:
            client_colors.append(list(i))
        for i, j in enumerate(client_colors):
            client_colors[i][1] = cls.hex_to_rgb(j[1])
            # client_colors[i] = tuple(client_colors[i])
        return client_colors



print(Database.get_client_colors())
