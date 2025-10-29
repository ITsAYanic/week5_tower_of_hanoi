def check_if_pillar_is_compatible(value1, value2):
    if not value1:
        return False
    if not value2:
        return True
    return value2[-1] > value1[-1]