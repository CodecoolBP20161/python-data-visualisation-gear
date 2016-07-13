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

    @classmethod
    def get_client_and_number_of_projects(cls):
        cls.cursor.execute("SELECT company_name, COUNT(company_name) FROM project GROUP BY company_name;")
        rows = cls.cursor.fetchall()
        # for i in rows:
        #     print(i)
        return rows

    @classmethod
    def get_project_colors(cls):
        from hex_rgb import hex_to_rgb
        # returns colors by company
        cls.cursor.execute("SELECT company_name, main_color, name FROM project;")
        colors = cls.cursor.fetchall()
        client_colors = []
        for i in colors:
            client_colors.append(list(i))
        for i, j in enumerate(client_colors):
            client_colors[i][1] = hex_to_rgb(j[1])
            # client_colors[i] = tuple(client_colors[i])
        return client_colors

    @classmethod
    def get_budget_by_project(cls):
        from currency_conversion import currency_conversion
        cls.cursor.execute("SELECT name, budget_value, budget_currency FROM project;")
        budget_list = []
        for i in cls.cursor.fetchall():
            budget_list.append(list(i))
        for i in budget_list:
            i[1] = "%.2f" % (currency_conversion(i[2]) * float(i[1]))
            i[2] = "EUR"
        return budget_list


def get_average_color_codes_by_companies(nested_list):
    list_of_companies = []
    to_return = []
    for i in nested_list:
        if i[0] not in list_of_companies:
            list_of_companies.append(i[0])
            to_return.append([i[0], i[1]])
        else:
            current_company_index = list_of_companies.index(i[0])
            to_pass = avg(to_return[current_company_index][1], i[1])
            to_return[current_company_index][1] = to_pass
    return to_return


def avg(values1, values2):
    to_return = []
    for i in range(len(values1)):
        to_calculate = values1[i] + values2[i]
        to_return.append(int(to_calculate / 2))
    return to_return


# print(get_average_color_codes_by_companies(Database.get_client_colors()))
# print("--------------------------------------------------------------------------")
# print(Database.get_client_colors())

# print(Database.get_project_colors())
# print(Database.get_budget_by_project())
