import numpy as np
import random


# QLearning agent built around stateless problems

# todo: add alpha and epsilon decay





class Agent:
    alpha = 0.1
    gamma = 0.9
    epsilon = 0.1
    # 0 == defect, 1 == cooperate
    action_labels = ["0", "1"]  # defect, cooperate or Y, X
    num_actions = 2

    # init method
    def __init__(self, name, debug=False):
        self.name = name
        self.debug = debug
        self.rg = "random"  # notes whether a move was randomly selected or selected greedily
        # self.action_labels = action_labels
        # self.num_actions = num_actions
        self.q_table = np.zeros((1, self.num_actions))  # can be modified later for problems with multiple states.

    def set_alpha(self, alpha):
        self.alpha = alpha

    def set_gamma(self, gamma):
        self.gamma = gamma

    def set_epsilon(self, epsilon):
        self.epsilon = epsilon

    def select_action(self, sm=True):
        if sm:
            self.select_action_softmax()
        else:
            self.select_action_epsilon_greedy()




    def select_action_epsilon_greedy(self):
        random_value = random.random()
        if self.debug:
            print("Agent", self.name, ": selecting action, epsilon =", self.epsilon, "random Value =", random_value)

        if random_value < self.epsilon:
            selected_action = self.select_random_action()
            self.rg = "random"
            if self.debug:
                print("Agent", self.name, ": selected action", self.action_labels[selected_action], "at random")
                print("QTABLE: ")
                print(self.q_table)
                print("Softmax Values: ")
                print(self.soft_max(self.q_table))
        else:
            selected_action = self.get_max_valued_action()
            self.rg = "greedy"
            if self.debug:
                print("Agent", self.name, ": selected action", self.action_labels[selected_action], "greedily")
        return selected_action

    def select_random_action(self):
        return int(random.random() * self.num_actions)

    def get_max_valued_action(self):
        if self.q_table[0, 0] > self.q_table[0, 1]:
            return 0
        elif self.q_table[0, 0] < self.q_table[0, 1]:
            return 1
        else:
            return int(random.random() * self.num_actions)

    def enable_debugging(self):
        self.debug = True

    def get_max_q_value(self):
        index = self.get_max_valued_action()
        return self.q_table[0, index]

    def update_q_value(self, selected_action, reward):
        old_q = self.q_table[0, selected_action]
        max_q = self.get_max_q_value()
        new_q = old_q + self.alpha * (reward + self.gamma * max_q - old_q)
        self.q_table[0, selected_action] = new_q

    def decay_alpha(self):
        self.alpha *= 0.999

    def normalise_probabilities(self, q_table):
        soft_qs = (np.exp(q_table.T) / np.sum(np.exp(q_table), axis=1)).T
        return soft_qs

    def select_action_softmax(self):
        normalised_probabilities = self.normalise_probabilities(self.q_table)

        trigger = random.random()  # lands on a specific point on the scale to determine which action to take

        scale = []
        total = 0  # used to define each marker in "bar"

        for i in normalised_probabilities:
            total += i
            scale.append(total)  # adding each point to the "scale"

        scale = np.array(scale)

        if trigger <= scale[0,0]:
            return 0

        else:
            for i in range(1, len(scale)-1):
                if trigger <= scale[0,i]:
                    return i








