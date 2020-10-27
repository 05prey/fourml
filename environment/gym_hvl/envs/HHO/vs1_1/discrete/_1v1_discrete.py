import gym

class DiscreteDogfightEnv(gym.Env):
  

  def __init__(self):
    print("DISCRETE")
    print("init method of environment")
    print("output degisimi")
  
  def step(self, action):
    print("DISCRETE")
    print("step method of environment")
  
  def reset(self):
    print("DISCRETE")
    print("reset method of environment")
