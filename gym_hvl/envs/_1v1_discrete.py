import gym

class DogfightEnv(gym.Env):
  

  def __init__(self):
    print("DISCRETE")
    print("init method of environment")
  
  def step(self, action):
    print("DISCRETE")
    print("step method of environment")
  
  def reset(self):
    print("DISCRETE")
    print("reset method of environment")
