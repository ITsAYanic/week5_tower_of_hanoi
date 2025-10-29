def check_which_pillar(object, pillar):
    '''Allowed values: p1, p2, p3'''
    match pillar:
        case "p1":
            return object.pillar1
        case "p2":
            return object.pillar2
        case "p3":
            return object.pillar3
        case _:
            raise ValueError(f'this is your code, why are you typing in { pillar }? (Allowed: p1, p2, p3)')