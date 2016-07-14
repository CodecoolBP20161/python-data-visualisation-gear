from model import Database


class Manager():

    def __init__(self, raw_data):
        self.name = raw_data[0]
        self.company = raw_data[1]

    @classmethod
    def get_manager_names_and_companies(cls):
        cursor = Database.find_db()
        cursor.execute("SELECT manager, company_name FROM project ORDER BY name;")
        managers = cursor.fetchall()
        return managers

    @classmethod
    def get_all(cls):
        managers = cls.get_manager_names_and_companies()
        return [Manager(raw_man) for raw_man in managers]
