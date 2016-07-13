# converts all currencies to eur
def currency_conversion(curr):
    if curr == 'GBP':
        x = float(1.19)
    elif curr == 'USD':
        x = float(0.91)
    else:
        x = 1
    return x
