class Company():

    def __init__(self, raw_data):
        self.company_name = raw_data[0]
        self.weight = raw_data[1]
        self.avg_color = raw_data[2]

    @staticmethod
    def get_all():
        from model import Database
        return Database.get_companies()
