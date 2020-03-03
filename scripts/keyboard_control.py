"""
Use this script to control the env with your keyboard.
For this script to work, you need to have the PyGame window in focus.

See/modify `char_to_action` to set the key-to-action mapping.
"""
import sys
import gym

import numpy as np
from multiworld.envs.mujoco.sawyer_xyz.sawyer_door_hook import SawyerDoorHookEnv

from multiworld.envs.mujoco.sawyer_xyz.sawyer_pick_and_place import \
    SawyerPickAndPlaceEnv
from multiworld.envs.mujoco.sawyer_xyz.sawyer_push_and_reach_env import \
    SawyerPushAndReachXYEnv, SawyerPushAndReachXYZEnv
from multiworld.envs.mujoco.sawyer_xyz.sawyer_push_and_reach_env_two_pucks import (
    SawyerPushAndReachXYDoublePuckEnv,
    SawyerPushAndReachXYZDoublePuckEnv,
)

import pygame
from pygame.locals import QUIT, KEYDOWN

from multiworld.envs.mujoco.sawyer_xyz.sawyer_reach import SawyerReachXYEnv, \
    SawyerReachXYZEnv

pygame.init()
screen = pygame.display.set_mode((400, 300))


char_to_action = {
    'w': np.array([0, -1, 0, 0]),
    'a': np.array([1, 0, 0, 0]),
    's': np.array([0, 1, 0, 0]),
    'd': np.array([-1, 0, 0, 0]),
    'q': np.array([1, -1, 0, 0]),
    'e': np.array([-1, -1, 0, 0]),
    'z': np.array([1, 1, 0, 0]),
    'c': np.array([-1, 1, 0, 0]),
    'k': np.array([0, 0, 1, 0]),
    'j': np.array([0, 0, -1, 0]),
    'h': 'close',
    'l': 'open',
    'x': 'toggle',
    'r': 'reset',
    'p': 'put obj in hand',
    'g': 'goal',
}


import gym
import multiworld
multiworld.register_all_envs()
import pygame
# env = gym.make('SawyerPushAndReachEnvEasy-v0')
# env = SawyerPushAndReachXYEnv(
#     goal_low=(-0.15, 0.4, 0.02, -.1, .5),
#     goal_high=(0.15, 0.75, 0.02, .1, .7),
#     puck_low=(-.3, .25),
#     puck_high=(.3, .9),
#     hand_low=(-0.15, 0.4, 0.05),
#     hand_high=(0.15, .75, 0.3),
#     norm_order=2,
#     xml_path='sawyer_xyz/sawyer_push_puck_small_arena.xml',
#     reward_type='state_distance',
#     reset_free=False,
# )
# env = SawyerReachXYEnv()

# env = gym.make('SawyerPushDebugCCRIG-v2')
# env = gym.make('SawyerPushDebugCCRIGSlowPhysics-v2')
env = gym.make('SawyerPushDebugCCRIG-v3')
# env = gym.make('SawyerPushDebugLEAP-v1')


# env_type = 'push_ccrig'
env_type = 'push_leap'

# if env_type == 'push_ccrig':
#     from multiworld.envs.mujoco.sawyer_xyz.sawyer_push_ccrig import SawyerMultiobjectEnv
#     from multiworld.envs.mujoco.cameras import sawyer_init_camera_zoomed_in, sawyer_pusher_camera_upright_v2
#     x_var = 0.2
#     x_low = -x_var
#     x_high = x_var
#     y_low = 0.5
#     y_high = 0.7
#     t = 0.05
#
#     env_kwargs = dict(
#         fixed_start=True,
#         fixed_colors=False,
#         reward_type="dense",
#         num_objects=1,
#         object_meshes=None,
#         num_scene_objects=[1],
#         maxlen=0.1,
#         action_repeat=1,
#         # puck_goal_low=(x_low + 0.01, y_low + 0.01),
#         # puck_goal_high=(x_high - 0.01, y_high - 0.01),
#         hand_goal_low=(x_low + 3*t, y_low + t),
#         hand_goal_high=(x_high - 3*t, y_high -t),
#         mocap_low=(x_low + 2*t, y_low , 0.0),
#         mocap_high=(x_high - 2*t, y_high, 0.5),
#         object_low=(x_low + 0.01, y_low + 0.01, 0.02),
#         object_high=(x_high - 0.01, y_high - 0.01, 0.02),
#         use_textures=False,
#
#         puck_goal_low=(x_low + 2*t, y_low),
#         puck_goal_high=(x_high - 2*t, y_high),
#     )
#     # env = SawyerMultiobjectEnv(**env_kwargs)
#     env = gym.make('SawyerPushDebugCCRIG-v0')
# elif env_type == 'push_leap':
#     from multiworld.envs.mujoco.sawyer_xyz.sawyer_push_leap import SawyerPushAndReachXYEnv
#     env_kwargs = dict(
#         # hand_low=(-0.20, 0.50),
#         # hand_high=(0.20, 0.70),
#         # puck_low=(-0.20, 0.50),
#         # puck_high=(0.20, 0.70),
#         # fix_reset=0.075,
#         # sample_realistic_goals=True,
#         # reward_type='state_distance',
#         # invisible_boundary_wall=True,
#
#         hand_low=(-0.10, 0.50),
#         hand_high=(0.10, 0.70),
#         puck_low=(-0.20, 0.50),
#         puck_high=(0.20, 0.70),
#         goal_low=(-0.05, 0.55, -0.20, 0.50),
#         goal_high=(0.05, 0.65, 0.20, 0.70),
#         fix_reset=True,
#         fixed_reset=(0.0, 0.4, 0.0, 0.6),
#         sample_realistic_goals=False,
#         reward_type='hand_and_puck_distance',
#         invisible_boundary_wall=True,
#     )
#     # env = SawyerPushAndReachXYEnv(**env_kwargs)
#     env = gym.make('SawyerPushDebugLEAP-v0')

NDIM = env.action_space.low.size
lock_action = False
obs = env.reset()
action = np.zeros(10)
while True:
    done = False
    if not lock_action:
        action[:3] = 0
    for event in pygame.event.get():
        event_happened = True
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            char = event.dict['key']
            new_action = char_to_action.get(chr(char), None)
            # print(new_action)
            if new_action == 'toggle':
                lock_action = not lock_action
            elif new_action == 'reset':
                done = True
            elif new_action == 'goal':
                ob = env.reset()
                env.set_to_goal({"state_desired_goal": ob["state_desired_goal"]})
            elif new_action == 'close':
                action[3] = 1
            elif new_action == 'open':
                action[3] = -1
            elif new_action == 'put obj in hand':
                print("putting obj in hand")
                env.put_obj_in_hand()
                action[3] = 1
            elif new_action is not None:
                action[:3] = new_action[:3]
            else:
                action = np.zeros(3)
            if action.any():
                env.step(action[:2])
    if done:
        obs = env.reset()
    env.render()
