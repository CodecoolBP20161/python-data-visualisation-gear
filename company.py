from model import Database


class Company():
    # including null values
    def __init__(self, raw_data):
        self.company_name = raw_data[0]
        self.weight = raw_data[1]   # number of projects by companies
        self.avg_color = raw_data[2]    # avg of rgb color codes of projects by companies

    @classmethod
    def get_client_and_number_of_projects(cls):
        cursor = Database.find_db()
        cursor.execute("""SELECT company_name, COUNT(company_name)
                              FROM project GROUP BY company_name ORDER BY company_name;""")
        rows = cursor.fetchall()
        return rows

    @classmethod
    def get_project_colors(cls):
        cursor = Database.find_db()
        # returns project colors by companies
        cursor.execute("SELECT company_name, main_color FROM project ORDER BY company_name;")
        colors = cursor.fetchall()
        client_colors = []
        for i in colors:
            client_colors.append(list(i))
        for i, j in enumerate(client_colors):
            client_colors[i][1] = Database.hex_to_rgb(j[1])
        return client_colors

    @staticmethod
    def avg(values1, values2):
        to_return = []
        for i in range(len(values1)):
            to_calculate = values1[i] + values2[i]
            to_return.append(int(to_calculate / 2))
        return tuple(to_return)

    @staticmethod
    def get_average_color_codes_by_companies(nested_list):
        list_of_companies = []
        to_return = []
        for i in nested_list:
            if i[0] not in list_of_companies:
                list_of_companies.append(i[0])
                to_return.append([i[0], i[1]])
            else:
                current_company_index = list_of_companies.index(i[0])
                to_pass = Company.avg(to_return[current_company_index][1], i[1])
                to_return[current_company_index][1] = to_pass
        return to_return

    @staticmethod
    def merge_company_data(raw_data, raw_colors):
        to_return = []
        for i in range(len(raw_data)):
            to_append = []
            to_append.append(raw_data[i][0])
            to_append.append(raw_data[i][1])
            to_append.append(tuple(raw_colors[i][1]))
            to_return.append(to_append)
        return to_return

    @classmethod
    def get_companies(cls):
        companies_data = cls.merge_company_data(
            cls.get_client_and_number_of_projects(),
            cls.get_average_color_codes_by_companies(cls.get_project_colors())
        )
        # list of all company instances
        return [Company(raw_company) for raw_company in companies_data]
