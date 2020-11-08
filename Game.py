from Agent import Agent
import numpy as np


class Game:
    # Payoff values for the prisoners dilemma
    #              AgB
    #           C       D
    #       C [3,3]   [0,5]
    #  AgA
    #       D [5,0]   [0,0]

    pd_payoffs = np.array([(3, 3), (0, 5), (5, 0), (0, 0)])
    pd_a_labels = ["D", "C"]

    # init for prisoners dilemma specifically
    def __init__(self, agent_a, agent_b):
        # constructor takes in two agents that are meant to be instantiated in the "main"
        self.agent_a = Agent("A", 1, 1, 1, 2, self.pd_a_labels)
        self.agent_b = Agent("B", 1, 1, 1, 2, self.pd_a_labels)

    # after a round is played each players payoff will be used to update their respective q_tables.
    # this function can be copied and modified for other games
    def pd_play_round(self):

        # each agent chooses an action at the start of round
        payoff = None
        action_a = self.agent_a.select_action()
        action_b = self.agent_b.select_action()

        # both cooperate
        if self.agent_a.select_action() == 1 and self.agent_b.select_action() == 1:
            payoff = self.pd_payoffs[0, 0]
        elif self.agent_a.select_action() == 0 and self.agent_b.select_action() == 0:
            payoff = self.pd_payoffs[0, 3]
        # a cooperates, b defects:
        elif self.agent_a.select_action() == 1 and self.agent_b.select_action() == 0:
            payoff = self.pd_payoffs[0, 1]
        # a defects, b cooperates:
        elif self.agent_a.select_action() == 0 and self.agent_b.select_action() == 1:
            payoff = self.pd_payoffs[0, 2]

        payoff_a, payoff_b = payoff
        self.agent_a.update_q_value(action_a, payoff_a)
        self.agent_b.update_q_value(action_b, payoff_b)




