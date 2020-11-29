"""fortune03.py
working with vector OS ver 1.6, python 3.7.1
took off text input so you can just "ask" vector a question without typing it.
Of course he is not listening but still better than typing it.  Added some
sound and played around with the sleep timing.  the file format was not working for me
so moved them to main folder.  after doing this noticed the m.png was working in one
of the first few lines, so will probably go back and edit the png locations again.
but for now this is working for me.  
"""
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
		sleep(0.4)
	robot.behavior.set_head_angle(degrees(45.0))
#	x = input("What do you need to ask to master vector, lost soul? ")
	print("What do you need to ask the great master vector, you lost soul?")
	robot.behavior.say_text("What do you need to ask the great master vector, you lost soul?")
	sleep(3)
	print("Shhh... Master Vector is thinking!")
	robot.behavior.say_text("Shhh... Master Vector is thinking!")
	robot.behavior.set_lift_height(0.4)
	robot.anim.play_animation("anim_cube_psychic_01", ignore_lift_track = True)
	sleep(2)
	robot.behavior.set_lift_height(0)
	robot.behavior.set_head_angle(degrees(45.0))
	robot.behavior.set_lift_height(0)
	robot.behavior.say_text("Pick me up and I shall give the answer to you")
	while not robot.status.is_picked_up:   #While vector has not been picked up...
		robot.screen.set_screen_with_image_data(screen_data,0.1)    
	prediction = randint(1,10)
	if prediction == 1:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("yes.png")   # I have used photos to display text on vector's screen
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("yes")
		robot.screen.set_screen_with_image_data(screen_data,4)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 2:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("sure.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("sure")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 3:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("absolutely.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("abolutely")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 4:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("certainly.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 5:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("notsure.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("I'm not sure")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 6:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("no.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("no")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 7:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("forgetit.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("If I were you, I would, forget it.")  
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 8:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("unsure.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("unsure")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 9:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("noway.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("no way, no how")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	if prediction == 10:
		robot.behavior.set_head_angle(degrees(45.0))
		image = Image.open("possibly.png")
		screen_data = anki_vector.screen.convert_image_to_screen_data(image)
		robot.behavior.say_text("possibly")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
		robot.screen.set_screen_with_image_data(screen_data,3)
		sleep(3)
		robot.anim.play_animation("anim_eyepose_happy")
	
