#!/bin/python3

# from abb_irb140_reacher.robot_env.abb_irb140_servo import ABBIRB140Servo
from abb_irb140_reacher.task_env.abb_irb140_reacher import ABBIRB140ReacherEnv
import gym
import rospy
import sys
from frobs_rl.common import ros_gazebo
from frobs_rl.common import ros_node
from frobs_rl.wrappers.NormalizeActionWrapper import NormalizeActionWrapper
from frobs_rl.wrappers.TimeLimitWrapper import TimeLimitWrapper
from frobs_rl.wrappers.NormalizeObservWrapper import NormalizeObservWrapper

# SB3 Checker
from stable_baselines3.common.env_checker import check_env

if __name__ == '__main__':

    # Kill all processes related to previous runs
    ros_node.ros_kill_all_processes()

    # Launch Gazebo 
    ros_gazebo.launch_Gazebo(paused=True, pub_clock_frequency=100)

    # Start node
    rospy.logwarn("Start")
    rospy.init_node('test_irb140_reacher')

    # Launch the task environment
    env = gym.make('ABBIRB140ReacherEnv-v0')

    #--- Normalize action space
    env = NormalizeActionWrapper(env)

    #--- Normalize observation space
    env = NormalizeObservWrapper(env)

    #--- Set max steps
    env = TimeLimitWrapper(env, max_steps=100)

    env.reset()

    check_env(env, warn=True)
    
    # env.close()
    # sys.exit()