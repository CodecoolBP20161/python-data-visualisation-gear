from model import Database
from project import Project
from company import Company


class Manager():

    def __init__(self, raw_data):
        self.name = raw_data[0]
        self.weight = raw_data[1]
        self.avg_color = raw_data[2]

    @classmethod
    def get_manager_names_and_companies(cls):
        cursor = Database.find_db()
        cursor.execute("SELECT manager, company_name FROM project WHERE manager IS NOT NULL ORDER BY name;")
        managers = cursor.fetchall()
        return managers

    @classmethod
    def get_budget_by_project(cls):
        cursor = Database.find_db()
        # projects witout name are removed
        cursor.execute("SELECT name, budget_value, budget_currency FROM project WHERE manager IS NOT NULL ORDER BY name;")
        budget_list = []
        for i in cursor.fetchall():
            budget_list.append(list(i))
        for i in budget_list:
            i[1] = "%.0f" % (Project.currency_conversion(i[2]) * float(i[1]))
            i[2] = "EUR"
        return budget_list

    @staticmethod
    def merge_data(raw_data, raw_budget, raw_color):
        to_return = []
        for i in range(len(raw_data)):
            to_append = []
            if len(str(raw_budget[i][1])) <= 3:
                raw_budget[i][1] = 1
            if len(str(raw_budget[i][1])) >= 4:
                raw_budget[i][1] = int(raw_budget[i][1]) // 1000
            to_append.append(raw_data[i][0])
            to_append.append(raw_budget[i][1])
            to_append.append(raw_color[i])
            to_return.append(to_append)
        return to_return

    @classmethod
    def assign_colors_to_managers(cls):
        colors = []
        for i, j in enumerate(cls.get_manager_names_and_companies()):
            for k in Company.get_companies():
                if j[1] == k.name:
                    colors.append(k.avg_color)
        return colors

    @classmethod
    def get_all(cls):
        managers = cls.merge_data(
            cls.get_manager_names_and_companies(),
            cls.get_budget_by_project(),
            cls.assign_colors_to_managers())
        return [Manager(raw_man) for raw_man in managers]

# print(Manager.get_all()[-1].weight)
# print(Manager.get_budget_by_project())

