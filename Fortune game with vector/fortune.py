import anki_vector                                 #We do our imports
from time import sleep
from random import randint
from PIL import Image
from anki_vector.util import degrees
with anki_vector.Robot() as robot:
	image = Image.open(".\images\m.png")
	screen_data = anki_vector.screen.convert_image_to_screen_data(image)   
	for i in range(0,5):                       #I made a loop as the photo always appears above the eyes but this overrides it... :)
		robot.screen.set_screen_with_image_data(screen_data,0.8)
		sleep(0.5)
	robot.behavior.set_head_angle(degrees(45.0))
	x = input("What do you need to ask to master vector, lost soul? ")
	sleep(2)
	print("Shhh... Master Vector is thinking!")
	robot.behavior.set_lift_height(0.4)
	robot.anim.play_animation("anim_cube_psychic_01", ignore_lift_track = True)
	sleep(2)
	robot.behavior.set_lift_height(0)
	robot.behavior.set_head_angle(degrees(45.0))
	robot.behavior.set_lift_height(0)
	robot.say_text("Pick me and I shall give the answer to you")
	while not robot.status.is_picked_up:   #While vector has not been picked up...
		robot.screen.set_screen_with_image_data(screen_data,0.1)    
	prediction = randint(1,10)
	if prediction == 1:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\yes.png")   # I have used photos to display text on vector's screen
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 2:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\sure.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 3:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\rabsolutely.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 4:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\certainly.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 5:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\rnotsure.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 6:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\rno.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 7:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\forgetit.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 8:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\unsure.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 9:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\noway.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 10:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open(".\\images\\possibly.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	
