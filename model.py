import psycopg2
from common import get_average_color_codes_by_companies, merge_company_data
from common import read_from_txt


class Database():

    conn_data = read_from_txt()
    # setup connection string
    connect_str = "dbname=" + conn_data[0] + " user=" + conn_data[1] + " host='localhost' password=" + conn_data[2]
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    @classmethod
    def get_companies(cls):
        from company import Company
        return [Company(raw_company)]

    @classmethod
    def get_client_and_number_of_projects(cls):
        cls.cursor.execute("SELECT company_name, COUNT(company_name) FROM project GROUP BY company_name ORDER BY company_name;")
        rows = cls.cursor.fetchall()
        return rows

    @classmethod
    def get_project_colors(cls):
        from common import hex_to_rgb
        # returns colors by company
        cls.cursor.execute("SELECT company_name, main_color, name FROM project ORDER BY company_name;")
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
        from common import currency_conversion
        cls.cursor.execute("SELECT name, budget_value, budget_currency FROM project;")
        budget_list = []
        for i in cls.cursor.fetchall():
            budget_list.append(list(i))
        for i in budget_list:
            i[1] = "%.2f" % (currency_conversion(i[2]) * float(i[1]))
            i[2] = "EUR"
        return budget_list


# print(get_average_color_codes_by_companies(Database.get_project_colors()))
# print("--------------------------------------------------------------------------")
# print(Database.get_client_and_number_of_projects())
# print("--------------------------------------------------------------------------")
# print(merge_company_data(Database.get_client_and_number_of_projects(),get_average_color_codes_by_companies(Database.get_project_colors())))
# print(Database.get_project_colors())

# print(Database.get_budget_by_project())
