import retro
import numpy as np
import cv2
import neat
import pickle

# Once we install our dependencies, we can import them
# Our next step is creating a env for the game to run in

env = retro.make(game = "SonicTheHedgehog-Genesis", state = "GreenHillZone.Act1")

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward.txt')