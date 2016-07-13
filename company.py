class Company():

    def __init__(self, raw_data, raw_colors):
        self.company_name = raw_data[0]
        self.weight = raw_data[1]
        self.avg_color = raw_colors[1]
