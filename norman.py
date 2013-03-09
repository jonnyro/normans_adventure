import sys, pygame
pygame.init()
 
size = width, height = 800,600
normanspeed = [0, 2]
worldspeed = [-2,0]
cloudspeed = [-1.25,0]



black = 255, 255, 255
screen = pygame.display.set_mode(size)
 
norman = pygame.image.load("images/norman.png")
normanrect = norman.get_rect()

rock = pygame.image.load("images/rock.png")
rockrect = rock.get_rect()

willow = pygame.image.load("images/tree.png")
willowrect = willow.get_rect()

hay_bale = pygame.image.load("images/hay_bale.png")
hay_balerect = hay_bale.get_rect()

sun = pygame.image.load("images/sun.png")
sunrect = sun.get_rect()

cloud = pygame.image.load("images/cloud.png")
cloudrect = cloud.get_rect()



def reset_cloud_coordinates():
	#initialize cloud
	cloudrect.left = 480+800
	cloudrect.top = 50

def reset_world_coordinates():
	#initialize tree
	willowrect.left = 480 + 800
	willowrect.top = 200
	
	

	

	#initialize rock
	rockrect.bottom = 485
	rockrect.left = 480 + 800

	#initialize hay bale
	hay_balerect.left = 300 + 800
	hay_balerect.bottom = 485

	#initialize the sun
	sunrect.top = 0
	sunrect.left = 0

	#initialize norman
	normanrect.left = 0
	normanrect.bottom = 475

	
reset_world_coordinates()
reset_cloud_coordinates()
	
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	normanrect = normanrect.move(normanspeed)
		
	
	
	rockrect = rockrect.move(worldspeed)
	willowrect = willowrect.move(worldspeed)
	hay_balerect = hay_balerect.move(worldspeed)
	cloudrect = cloudrect.move(cloudspeed)
	
	if (willowrect.right < 0):
		reset_world_coordinates()
	
	if (cloudrect.right < 0):
		reset_cloud_coordinates()
	
	if normanrect.left < 0 or normanrect.right > width:
		normanspeed[0] = -normanspeed[0]
	if normanrect.top < 240 or normanrect.bottom > 480:
		normanspeed[1] = -normanspeed[1]

	screen.fill(black)

	screen.blit(rock, rockrect)

	screen.blit(willow, willowrect)

	screen.blit(hay_bale, hay_balerect)

	screen.blit(sun, sunrect)
	
	screen.blit(cloud, cloudrect)
	

	screen.blit(norman, normanrect)

	
	
	pygame.display.flip()
