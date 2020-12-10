import numpy as np

debug = False

# This class runs games
# it takes in the following:
# -> agent_a
# -> agent_b
# -> A payoff table in the following format:
#         [[1,1], [1,0]
#          [0,1], [0,0]]
#     where 0 and 1 are the moves available to
#     agent_a and agent_b in symmetric 2-player games
#
# it then runs the game and stores the following bits of data:
# -> (agent_a, agent_b) actions and payoffs
# -> (agent_a, agent_b) whether actions made at random or greedily


class GameRunner:
    num_episodes = 10000
    # payoff at end of each round:
    agent_a_payoffs = []
    agent_b_payoffs = []
    # action selected by agent:
    agent_a_action = []
    agent_b_action = []
    # greedy or at random?:
    agent_a_rg = []
    agent_b_rg = []

    round_count = 0  # incremented at end of round
    # holds number of times 0 or 1 was chosen by agent a or b
    a_one_count = 0
    b_one_count = 0
    a_zero_count = 0
    b_zero_count = 0

    # I might be storing too much redundant data, but it saves me the pain of having to work with pandas.
    # Probabilities of actions over time t.
    a_zero_prob = []
    b_zero_prob = []

    a_one_prob = []
    b_one_prob = []

    # were initially meant to number of times each agent selected.
    # agent_a_one = []
    # agent_a_zero = []
    # agent_b_one = []
    # agent_b_zero = []

    # payoff tables should be entered in the following format of payoffs
    # where X and Y are the moves available to agents a and b
    # aX,bX,aY,bY in each of the indexes represent the payoffs for each agent in a specific move pair.
    default_payoff_table = [["aX", "bX"], ["aY", "bY"],
                            ["aY", "bX"], ["aY", "bY"]]

    # Payoff table for the prisoners dilemma:

    #              AgB
    #           C       D
    #       C [3,3]   [0,5]
    #  AgA
    #       D [5,0]   [0,0]

    # pd_payoffs = np.array([(3, 3), (0, 5), (5, 0), (0, 0)])
    # pd_a_labels = np.array(["D", "C"])
    # pd_actions = np.array([0, 1])
    # alpha_decay_rate = 0.9
    # epsilon_decay_rate = 0.9

    # init for prisoners dilemma specifically
    def __init__(self, agent_a, agent_b, payoff_table):
        # constructor takes in two agents that are meant to be instantiated in the "main"
        # agent constructor takes: agent name, alpha, gamma, epsilon, num_actions, action_labels.
        self.agent_a = agent_a
        self.agent_b = agent_b
        self.payoff_table = np.array(payoff_table)

    def play_episodes(self, num_episodes, decay_alpha_a=False, decay_alpha_b=False, decay_point_a=num_episodes/2, decay_point_b=num_episodes/2):
        for i in range(num_episodes):
            self.pd_play_round()

            if i >= decay_point_a:
                if decay_alpha_a is True:
                    self.agent_a.decay_alpha()
            if i >= decay_point_b:
                if decay_alpha_b is True:
                    self.agent_b.decay_alpha()

    # after a round is played each players payoff will be used to update their respective q_tables.
    # this function can be copied and modified for other games
    def pd_play_round(self):
        #self.round_count += 1
        # each agent chooses an action at the start of round
        payoff = None
        action_a = self.agent_a.select_action(sm=True)
        action_b = self.agent_b.select_action(sm=True)
        if debug:
            print("ACTION SELECTED IN GAME BY A: ", action_a)
            print("ACTION SELECTED IN GAME BY B: ", action_b)

        # both cooperate
        payoff_a = 0
        payoff_b = 0
        if action_a == 1 and action_b == 1:  # -> a.x, b.x
            payoff_a = self.payoff_table[0, 0]
            payoff_b = self.payoff_table[0, 1]
        elif action_a == 1 and action_b == 0:  # -> a.x, b.y
            payoff_a = self.payoff_table[1, 0]
            payoff_b = self.payoff_table[1, 1]
        # a cooperates, b defects:
        elif action_a == 0 and action_b == 1:  # -> a.y, b.x
            payoff_a = self.payoff_table[2, 0]
            payoff_b = self.payoff_table[2, 1]
        # a defects, b cooperates:
        elif action_a == 0 and action_b == 0:  # -> a.y, b.y
            payoff_a = self.payoff_table[3, 0]
            payoff_b = self.payoff_table[3, 1]

        self.agent_a.update_q_value(action_a, payoff_a)
        self.agent_b.update_q_value(action_b, payoff_b)

        if debug:
            print("Payoff A: ", payoff_a)
            print(self.agent_a.q_table)
            print("Payoff B: ", payoff_b)
            print(self.agent_b.q_table)
            print("ROUND CONT ", self.round_count)

        self.round_count += 1

        self.store_round(action_a=action_a, payoff_a=payoff_a, action_b=action_b, payoff_b=payoff_b,
                         rg_a=self.agent_a.rg, rg_b=self.agent_b.rg)

    def store_round(self, action_a, payoff_a, action_b, payoff_b, rg_a, rg_b):

        self.agent_a_action.append(action_a)
        self.agent_b_action.append(action_b)

        self.agent_a_payoffs.append(payoff_a)
        self.agent_b_payoffs.append(payoff_b)


        if action_a == 0:
            self.a_zero_count += 1
        elif action_a == 1:
            self.a_one_count += 1

        self.a_one_prob.append(round(self.a_one_count/self.round_count, 2))
        self.a_zero_prob.append(round((self.round_count - self.a_one_count)/self.round_count, 2))

        if action_b == 0:
            self.b_zero_count += 1
        else:
            self.b_one_count += 1

        self.b_one_prob.append(round((self.round_count-self.b_zero_count) / self.round_count, 2))
        self.b_zero_prob.append(round(self.b_zero_count / self.round_count, 2))

        self.agent_a_rg.append(rg_a)
        self.agent_b_rg.append(rg_b)
