import numpy as np
import random


# all the functions in the Agent class are designed around
# the problem (prisoners dilemma) being stateless
# a few functions will need tweaking for problems with states.


class Agent:
    debug = False

    # init method
    def __init__(self, name, alpha, gamma, epsilon, num_actions, action_labels):
        self.name = name  # name of the agent
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # probability of random action/exploration
        self.num_actions = num_actions  # the number of available actions in the environment
        self.action_labels = action_labels  # labels/names of all available actions
        # initialises q_values
        self.q_table = np.zeros((1, num_actions))  # can be modified later for problems with multiple states.

    # method to return 1 for cooperate and 2 for defect
    def select_action(self):
        # selected_action = None  # declaring variable to be returned later
        random_value = random.random()
        if self.debug:
            print("Agent", self.name, ": selecting action, epsilon =", self.epsilon, "random Value =", random_value)

        if random_value < self.epsilon:
            selected_action = self.select_random_action()
            if self.debug:
                print("Agent", self.name, ": selected action", selected_action, "at random")
        else:
            selected_action = self.get_max_valued_action()
            print("Agent", self.name, ": selected action", selected_action, "greedily")
        return selected_action

    # function to return a random action
    # called in the select_action() function
    def select_random_action(self):
        return int(random.random() * self.num_actions)

    # function to return a max valued action
    # called in the select_action() function
    def get_max_valued_action(self):
        # since the q_table here only has a single dimension the row (as there is only state 0)
        # is returned
        max_index_column = np.argmax(self.q_table, 0)
        # the following code can be uncommented for use in problems with states
        # max_index_row = np.argmax(self.q_table, 1) # (___, 1) returns row position of element
        # return (max_index_row, max_index_column)
        return max_index_column

    def enable_debugging(self):
        self.debug = True

    def get_max_q_value(self):
        index = self.get_max_valued_action()
        return self.q_table[0, index]

    def update_q_value(self, selected_action, reward):
        old_Q = self.q_table[0, selected_action]
        max_q = self.get_max_q_value()
        new_q = float(old_Q + self.alpha * (reward + self.gamma * max_q - old_Q))
        self.q_table[0, selected_action] = new_q
