from gym.envs.registration import register

register(
    id='dogfight-v0',
    entry_point='gym_hvl.envs:DogfightEnv',
)
