import psycopg2


class Database():

    @staticmethod
    def read_from_txt():
        import os.path
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'user.txt')
        data = []
        with open(filename) as f:
            for l in f.readlines():
                content = l.strip("\n")
                data.append(content)
            return data

    @classmethod
    def find_db(cls):
        conn_data = cls.read_from_txt()
        # setup connection string
        connect_str = "dbname=" + conn_data[0] + " user=" + conn_data[1] + " host='localhost' password=" + conn_data[2]
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        return(conn.cursor())

    @staticmethod
    # converts color hex codes to rgb
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
