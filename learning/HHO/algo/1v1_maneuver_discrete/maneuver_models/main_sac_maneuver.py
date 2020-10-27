import gym
import gym_hvl

env = gym.make('dogfight_maneuver-v0')

env.reset()

episodes = 5
for e in range(episodes):
        
    action = [0,0,0]
    env.step(action)


