import numpy as np
import random


# all the functions in the Agent class are designed around
# the problem (prisoners dilemma) being stateless
# a few functions will need tweaking for problems with states.


class Agent:
    debug = True
    alpha = float(0.1)
    gamma = 0.5
    epsilon = 0.1
    # 0 == defect, 1 == cooperate
    action_labels = ["D", "C"]
    num_actions = 2

    # init method
    def __init__(self, name):
        self.name = name
        self.q_table = np.zeros((1, self.num_actions))  # can be modified later for problems with multiple states.

    # method to return 1 for cooperate and 2 for defect
    def ol_select_action(self):
        # selected_action = None  # declaring variable to be returned later
        random_value = random.random()
        if self.debug:
            print("Agent", self.name, ": selecting action, epsilon =", self.epsilon, "random Value =", random_value)

        if random_value < self.epsilon:
            selected_action = self.select_random_action()
            if self.debug:
                print("Agent", self.name, ": selected action", self.action_labels[selected_action], "at random")
        else:
            selected_action = self.get_max_valued_action()
            print("Agent", self.name, ": selected action", self.action_labels[selected_action], "greedily")
        return selected_action

    def select_action(self):
        random_value = random.random()
        if self.debug:
            print("Agent", self.name, ": selecting action, epsilon =", self.epsilon, "random Value =", random_value)

        if random_value < self.epsilon:
            selected_action = self.select_random_action()
            print("Agent", self.name, ": selected action", self.action_labels[selected_action], "at random")
        else:
            selected_action = self.get_max_valued_action()
            print("Agent", self.name, ": selected action", self.action_labels[selected_action], "greedily")
        return selected_action

    # function to return a random action
    # called in the select_action() function
    def select_random_action(self):
        return int(random.random() * self.num_actions)

    def get_max_valued_action(self):
        if self.q_table[0, 0] > self.q_table[0, 1]:
            return 0
        elif self.q_table[0, 0] < self.q_table[0, 1]:
            return 1
        else:
            return int(random.random()*self.num_actions)

    def enable_debugging(self):
        self.debug = True

    # function used in update_q_value()
    def get_max_q_value(self):
        index = self.get_max_valued_action()
        return self.q_table[0, index]

    def update_q_value(self, selected_action, reward):
        old_q = self.q_table[0, selected_action]
        max_q = self.get_max_q_value()
        new_q = old_q + self.alpha * (reward + self.gamma * max_q - old_q)
        self.q_table[0, selected_action] = new_q
