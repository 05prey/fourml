from gym.envs.registration import register

register(
    id='hho_1v1_maneuver-v0',
    entry_point='gym_hvl.envs.HHO.vs1_1.maneuver:SimEnv',
)

register(
    id='hho_1v1_discrete-v0',
    entry_point='gym_hvl.envs.HHO.vs1_1.discrete:SimEnv',
)

