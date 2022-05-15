from string import ascii_uppercase
import numpy as np
import pandas as pd
import os
import random
from Sim import *
from Agent_MCQ import *

def main_MCQ():
    env = Simulator()
    agent = agent_MCQ()
    files = pd.read_csv("./data/factory_order_train.csv")
    episode = 1000

    for epi in range(episode):
        done = False
        s = env.reset()
        while not done:

