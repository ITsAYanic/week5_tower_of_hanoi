extends Sprite2D




var is_dragging = false
var pillars = []

func check_if_plate_compatible():
	pass


func _input(event: InputEvent) -> void:

		if event.is_pressed():
			print("pressed yeah")
		else:
			print("nothing is pressed :()")
