import psycopg2
# from common import get_average_color_codes_by_companies, merge_company_data


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

    # @classmethod
    # def get_client_and_number_of_projects(cls):
    #     cursor = cls.find_db()
    #     cursor.execute("""SELECT company_name, COUNT(company_name)
    #                           FROM project GROUP BY company_name ORDER BY company_name;""")
    #     rows = cursor.fetchall()
    #     return rows

    # @classmethod
    # def get_project_colors(cls):
    #     from company import hex_to_rgb
    #     cursor = cls.find_db()
    #     # returns colors by company
    #     cursor.execute("SELECT company_name, main_color, name FROM project ORDER BY company_name;")
    #     colors = cursor.fetchall()
    #     client_colors = []
    #     for i in colors:
    #         client_colors.append(list(i))
    #     for i, j in enumerate(client_colors):
    #         client_colors[i][1] = hex_to_rgb(j[1])
    #         # client_colors[i] = tuple(client_colors[i])
    #     return client_colors

    @classmethod
    def get_budget_by_project(cls):
        from common import currency_conversion
        cursor = cls.find_db()
        cursor.execute("SELECT name, budget_value, budget_currency FROM project;")
        budget_list = []
        for i in cursor.fetchall():
            budget_list.append(list(i))
        for i in budget_list:
            i[1] = "%.2f" % (currency_conversion(i[2]) * float(i[1]))
            i[2] = "EUR"
        return budget_list

    # @classmethod
    # def get_companies(cls):
    #     from company import Company
    #     companies_data = merge_company_data(
    #         Company.get_client_and_number_of_projects(),
    #         get_average_color_codes_by_companies(Company.get_project_colors())
    #         )
    #     return [Company(raw_company) for raw_company in companies_data]


# print(get_average_color_codes_by_companies(Database.get_project_colors()))
# print("--------------------------------------------------------------------------")
# print(Database.get_client_and_number_of_projects())
# print("--------------------------------------------------------------------------")
# print(companies_data)
# print(merge_company_data(Database.get_client_and_number_of_projects(),get_average_color_codes_by_companies(Database.get_project_colors())))
# print(Database.get_project_colors())

# print(Database.get_budget_by_project())
