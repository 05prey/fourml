from gym.envs.registration import register

register(
    id='dogfight_maneuver-v0',
    entry_point='gym_hvl.envs.HHO.vs1_1.maneuver:ManeuverDogfightEnv',
)

register(
    id='dogfight_discrete-v0',
    entry_point='gym_hvl.envs.HHO.vs1_1.discrete:DiscreteDogfightEnv',
)

