from gym.envs.registration import register

register(
    id='dogfight-v0',
    entry_point='gym_hvl.envs.HHO.vs1_1.maneuver:DogfightEnv',
)

register(
    id='dogfight_discrete-v0',
    entry_point='gym_hvl.envs.HHO.vs1_1.discrete:DiscreteDogfightEnv',
)

