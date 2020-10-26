import gym

class DogfightEnv(gym.Env):
  

  def __init__(self):
    print("init method of DISCRETE environment")
  
  def step(self, action):
    print("step method of DISCRETE environment")
  
  def reset(self):
    print("reset method of DISCRETE environment")
