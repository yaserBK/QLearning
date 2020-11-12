from Agent import Agent
import numpy as np
import csv

debug = False


class GameRunner:
    round_count = 0
    # stores round data to write to csv
    agent_a_payoffs = []
    agent_b_payoffs = []
    agent_a_action = []
    agent_b_action = []
    agent_a_rand = [] # yes, no
    agent_b_rand = [] # yes, no
    # Payoff values for the prisoners dilemma
    #              AgB
    #           C       D
    #       C [3,3]   [0,5]
    #  AgA
    #       D [5,0]   [0,0]

    pd_payoffs = np.array([(3, 3), (0, 5), (5, 0), (0, 0)])
    pd_a_labels = np.array(["D", "C"])
    pd_actions = np.array([0, 1])
    num_episodes = 1000
    alpha_decay_rate = 0.9
    epsilon_decay_rate = 0.9

    # init for prisoners dilemma specifically
    def __init__(self, agent_a, agent_b):
        # constructor takes in two agents that are meant to be instantiated in the "main"
        # agent constructor takes: agent name, alpha, gamma, epsilon, num_actions, action_labels.
        self.agent_a = agent_a
        self.agent_b = agent_b
        # to write to csv
        with open("agent_a.csv", 'w', newline='') as f:
            self.the_writer_a = csv.writer(f)
        with open("agent_b.csv", 'w', newline='') as g:
            self.the_writer_b = csv.writer(g)

    # after a round is played each players payoff will be used to update their respective q_tables.
    # this function can be copied and modified for other games
    def pd_play_round(self):
        # each agent chooses an action at the start of round
        payoff = None
        action_a = self.agent_a.select_action()
        print("ACTION SELECTED IN GAME BY A: ", action_a)
        action_b = self.agent_b.select_action()
        print("ACTION SELECTED IN GAME BY B: ", action_b)

        # both cooperate
        payoff_a = 0
        payoff_b = 0
        if action_a == 1 and action_b == 1:
            payoff_a = 3
            payoff_b = 3
        elif action_a == 0 and action_b == 0:
            payoff_a = 0
            payoff_b = 0
        # a cooperates, b defects:
        elif action_a == 1 and action_b == 0:
            payoff_a = 0
            payoff_b = 5
        # a defects, b cooperates:
        elif action_a == 0 and action_b == 1:
            payoff_a = 5
            payoff_b = 0

        with open("agent_a.csv", 'w', newline='') as f:
            self.the_writer_a = csv.writer(f)
            self.the_writer_a.writerow([payoff_a])
        # payoff_a, payoff_b = payoff
        self.agent_a.update_q_value(action_a, payoff_a)
        print("Payoff A: ", payoff_a)
        print(self.agent_a.q_table)
        self.agent_b.update_q_value(action_b, payoff_b)
        print("Payoff B: ", payoff_b)
        print(self.agent_b.q_table)
        self.round_count += 1
