import random
import numpy as np
from Sim import *
import copy

class Agent_MCQ():

    def __init__(self):
        self.eps = 0.9
        self.alpha = 0.01
        self.target = Simulator.local_target[0]
        self.Q_table_name_lst = Simulator.inds.append("T") #T는 맨처음 위치, 여러 개의 Q_Table들을 만들 계획
        self.Q_tables = []
        for Q_table_name in self.Q_table_name_lst:
            globals()["Q_table_{}".format(Q_table_name)] = np.zeros((Simulator.height, Simulator.width, 4))  # Q_table_%name 변수를 선언해서 3차원 0으로 이루어진 numpyarray를 넣음
            self.Q_tables.append(globals()["Q_table_{}".format(Q_table_name)])  # 리스트에 넣어줌. (딕셔너리로 이름:넘파이어레이, 방식으로 넣고싶은데 잘모르겠다. Structure array를 써보고 싶은데 잘 모르겠음)
        self.Q_table = self.Q_tables[self.Q_table_name_lst.index(self.target)]


    def select_random_action(self):
        coin = random.random()
        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action = 2
        else:
            action = 3
        return action

    def select_action_epsgreedy(self, cur_x, cur_y, target):
        epscoin = random.random()
        if epscoin < self.eps:
            action = self.select_random_action()
        else:
            action_value = self.Q_tables[self.Q_table_name_lst.index(target)][cur_x, cur_y, :]
            action = np.argmax(action_value)
        return action

    def update_table(self, cur_x, cur_y, history):
        target = Simulator.local_target[0]
        Q_table = self.Q_tables[self.Q_table_name_lst.index(target)]
        cum_reward = 0
        for transition in history[::-1]:
            s, a, r, s_prime = transition
            self.q_table[cur_x, cur_y, a] = self.q_table[cur_x, cur_y, a] + self.alpha * (cum_reward - self.q_table[cur_x, cur_y, a])
            cum_reward = cum_reward + r

    def anneal_eps(self):
        self.eps -= 0.03
        self.eps = max(self.eps, 0.1)



