from functions.check_which_pillar import check_which_pillar
from functions.check_if_pillar_is_compatible import check_if_pillar_is_compatible

def move_plate(self, old_pillar, new_pillar):
    old_pillar = check_which_pillar(object, old_pillar)
    new_pillar = check_which_pillar(object, new_pillar)
    if check_if_pillar_is_compatible(old_pillar, new_pillar):
        plate = old_pillar.pop()
        new_pillar.append(plate)
    else:
        print("You can only stack smaller plates onto bigger plates")
