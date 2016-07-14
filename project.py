from model import Database


class Project():

    def __init__(self, raw_data):
        self.name = raw_data[0]
        self.project_budget = raw_data[1]   # budget value in eur by projects
        self.project_color = raw_data[2]
        self.maintenance = raw_data[3]  # boolean value

    @staticmethod
    # converts all currencies to eur
    def currency_conversion(curr):
        if curr == 'GBP':
            x = float(1.19)
        elif curr == 'USD':
            x = float(0.91)
        else:
            x = 1
        return x

    @classmethod
    def get_budget_by_project(cls):
        cursor = Database.find_db()
        # projects witout name are removed
        cursor.execute("SELECT name, budget_value, budget_currency FROM project ORDER BY name;")
        budget_list = []
        for i in cursor.fetchall():
            budget_list.append(list(i))
        for i in budget_list:
            i[1] = "%.2f" % (cls.currency_conversion(i[2]) * float(i[1]))
            i[2] = "EUR"
        return budget_list

    @classmethod
    def get_project_colors(cls):
        cursor = Database.find_db()
        # returns project colors by companies
        cursor.execute("SELECT main_color FROM project ORDER BY name;")
        project_colors = []
        for i in cursor.fetchall():
            project_colors.append(list(i))
        for i, j in enumerate(project_colors):
            project_colors[i][0] = Database.hex_to_rgb(j[0])
        return project_colors

    @classmethod
    # returns list of boolean values
    def is_maintenance_requested(cls):
        cursor = Database.find_db()
        # projects without names are removed
        cursor.execute("SELECT maintenance_requested FROM project ORDER BY name")
        maintenance_requested = []
        for i in cursor.fetchall():
            if i[0] == 'true':
                maintenance_requested.append(True)
            else:
                maintenance_requested.append(False)
        return maintenance_requested

    @staticmethod
    def merge_project_data(raw_data, raw_colors, raw_maintenance):
        to_return = []
        for i in range(len(raw_data)):
            to_append = []
            to_append.append(raw_data[i][0])
            to_append.append(raw_data[i][1])
            to_append.append(tuple(raw_colors[i][0]))
            to_append.append(raw_maintenance[i])
            to_return.append(to_append)
        return to_return

    @classmethod
    def get_projects(cls):
        project_data = cls.merge_project_data(
            cls.get_budget_by_project(),
            cls.get_project_colors(),
            cls.is_maintenance_requested()
        )
        # list of all project instances
        return [Project(raw_project) for raw_project in project_data]

# print(Project.get_project_colors())
# print(Project.get_budget_by_project())
# print(Project.is_maintenance_requested())
# print(Project.get_projects()[10].maintenance)

class NamedProject(Project):

    def __init__(self, *args, **kwargs):
        super(NamedProject, self).__init__(*args, **kwargs)

    @classmethod
    def get_all_named_projects(cls):
        named_projects = []
        for i, j in enumerate(Project.get_projects()):
            if j.name is not None:
                named_projects.append(Project.get_projects()[i])
        return named_projects

print(NamedProject.get_all_named_projects()[-1].name)
