from gym.envs.registration import register

register(
    id='dogfight-v0',
    entry_point='gym_hvl.envs:DogfightEnv',
)

register(
    id='dogfight_discrete-v0',
    entry_point='gym_hvl.envs:DogfightEnv',
)

