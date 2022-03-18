import retro
import numpy as np
import cv2
import neat
import pickle

# Once we install our dependencies, we can import them
# Our next step is creating a env for the game to run in

# making a worker class to run the game
class Worker(object):
    def __init__(self, genome, config):
        self.genome = genome
        self.config = config
        
    def work(self):
        
        self.env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
        
        self.env.reset()
        
        ob, _, _, _ = self.env.step(self.env.action_space.sample())
        
        inx = int(ob.shape[0]/8)
        iny = int(ob.shape[1]/8)
        done = False
        
        net = neat.nn.FeedForwardNetwork.create(self.genome, self.config)
        
        fitness = 0
        xpos = 0
        xpos_max = 0
        counter = 0
        imgarray = []
        
        while not done:
            # self.env.render()
            ob = cv2.resize(ob, (inx, iny))
            ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
            ob = np.reshape(ob, (inx, iny))
            
            imgarray = np.ndarray.flatten(ob)
            imgarray = np.interp(imgarray, (0, 254), (-1, +1))
            actions = net.activate(imgarray)
            
            ob, rew, done, info = self.env.step(actions)
            
            xpos = info['x']

            
            if xpos > xpos_max:
                xpos_max = xpos
                counter = 0
                fitness += 1
            else:
                counter += 1
                
            if counter > 250:
                done = True
                
            if xpos == info['screen_x_end'] and xpos > 500:
                fitness += 100000
                done = True
                
        print(fitness)
        return fitness



config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward.txt')