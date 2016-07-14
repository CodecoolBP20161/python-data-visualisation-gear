from model import Database


class Project():

    def __init__(self, raw_data):
        self.name = raw_data[0]
        self.project_budget = raw_data[1]   # budget value in eur by projects
        self.project_color = raw_data[2]
        self.project_duedate = raw_data[3]

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
        cursor.execute("SELECT name, budget_value, budget_currency FROM project WHERE name IS NOT NULL ORDER BY name;")
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
        cursor.execute("SELECT main_color FROM project WHERE name IS NOT NULL ORDER BY name;")
        project_colors = []
        for i in cursor.fetchall():
            project_colors.append(list(i))
        for i, j in enumerate(project_colors):
            project_colors[i][0] = Database.hex_to_rgb(j[0])
        return project_colors

    @classmethod
    def get_project_duedates(cls):
        cursor = Database.find_db()
        cursor.execute("SELECT duedate FROM project WHERE name IS NOT NULL ORDER BY name;")
        project_duedates = []
        return cursor.fetchall()

    @classmethod
    def is_maintenance_requested(cls):
        cursor = Database.find_db()
        cursor.execute("SELECT maintenance_requested FROM project WHERE name IS NOT NULL ORDER BY name")
        maintenance_requested = []
        return (cursor.fetchall())

    @staticmethod
    def merge_project_data(raw_data, raw_colors, raw_duedates):
        to_return = []
        for i in range(len(raw_data)):
            to_append = []
            to_append.append(raw_data[i][0])
            to_append.append(raw_data[i][1])
            to_append.append(tuple(raw_colors[i][0]))
            due_dates = str(raw_duedates[i]).replace("(datetime.date(", "")
            yr = []
            for i in range(4):
                yr.append(due_dates[i])
            year = ''.join(yr)
            to_append.append(int(year))
            to_return.append(to_append)
        return to_return

    @classmethod
    def get_projects(cls):
        project_data = cls.merge_project_data(
            cls.get_budget_by_project(),
            cls.get_project_colors(),
            cls.get_project_duedates()
        )
        # list of all company instances
        return [Project(raw_project) for raw_project in project_data]


for i in Project.get_projects():
    print(i.name)
    print(i.project_budget)
    print(i.project_color)
    print(i.project_duedate)
    print("------------")
