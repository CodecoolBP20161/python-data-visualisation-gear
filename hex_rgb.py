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
        pass
