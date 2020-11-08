from Agent import Agent
import numpy as np

debug = True


class Game:
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

    # init for prisoners dilemma specifically
    def __init__(self):
        # constructor takes in two agents that are meant to be instantiated in the "main"
        self.agent_a = Agent("A", 0.1, 0.9, 0.1, 2, self.pd_a_labels)
        self.agent_b = Agent("B", 0.1, 0.9, 0.1, 2, self.pd_a_labels)

    # after a round is played each players payoff will be used to update their respective q_tables.
    # this function can be copied and modified for other games
    def pd_play_round(self):
        # each agent chooses an action at the start of round
        payoff = None
        action_a = self.agent_a.select_action()
        print("ACTION SELECTED IN GAME: ", action_a)
        action_b = self.agent_b.select_action()

        # both cooperate
        if action_a == 1 and action_b == 1:
            payoff = self.pd_payoffs[0, 0]
        elif action_a == 0 and action_b == 0:
            payoff = self.pd_payoffs[0, 3]
        # a cooperates, b defects:
        elif action_a == 1 and action_b == 0:
            payoff = self.pd_payoffs[0, 1]
        # a defects, b cooperates:
        elif action_a == 0 and action_b == 1:
            payoff = self.pd_payoffs[0, 2]

        payoff_a, payoff_b = payoff
        self.agent_a.update_q_value(action_a, payoff_a)
        self.agent_b.update_q_value(action_b, payoff_b)




