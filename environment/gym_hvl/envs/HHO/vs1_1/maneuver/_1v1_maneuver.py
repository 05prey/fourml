import gym

class ManeuverDogfightEnv(gym.Env):
  

  def __init__(self):
    print("init method of environment")
  
  def step(self, action):
    print("step method of environment")
  
  def reset(self):
    print("reset method of environment")
  
