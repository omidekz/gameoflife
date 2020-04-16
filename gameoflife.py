import json
from time import sleep
from random import random
import os

# methods
def draw(world):
	os.system('clear')
	for line in world:
		for i in line:
			print (live_cell if i else dead_cell, end='')
		print ()

def generation(world):
	new_world = []
	for y in range(height):
		line = []
		for x in range(width):
			lives = -1 if world[y][x] else 0
			for ty in range(y-1, y+2):
				"""if not 0 <= ty < height:
					continue"""
				for tx in range(x-1, x+2):
					"""if not 0 <= tx < width:
						continue"""
					if world[(ty+height) % height][(tx+width)%width]:
						lives += 1
			line.append(lives == 3 or (world[y][x] and lives == 2))
		new_world.append(line)
	return new_world
# main
if __name__ == '__main__':
	# load configs
	configs = json.load(open('./configs.json', 'r'))
	# read configs from file
	live_cell = configs['live_cell']
	dead_cell = configs['dead_cell']
	generation_sec = configs['generation_sec']
	width = configs['width']
	height = configs['height']
	live_pos = configs['live_possibility']
	# create the world, in world 0 is dead and 1 is live
	world = [[1 if random() < live_pos else 0 for _ in range(width)] for _ in range(height)]
	while True:
		draw(world)
		world = generation(world)
		sleep(generation_sec)
