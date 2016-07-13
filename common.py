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


# converts color hex codes to rgb
def hex_to_rgb(value):
    if value is not None:
        value = value.lstrip('#')
        lv = len(value)
        if lv == 1:
            v = int(value, 16)*17
            return v, v, v
        if lv == 3:
            return tuple(int(value[i:i+1], 16)*17 for i in range(0, 3))
        return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))
    else:
        return (0, 0, 0)


# converts all currencies to eur
def currency_conversion(curr):
    if curr == 'GBP':
        x = float(1.19)
    elif curr == 'USD':
        x = float(0.91)
    else:
        x = 1
    return x


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
