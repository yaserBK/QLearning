import csv

from Game_Runner import GameRunner


class Util:

    def __init__(self, game):
        self.game = game

    def write_to_csv(self):
        fa = open("agent_a.csv", 'w', newline='')
        a_writer = csv.writer(fa)
        a_writer.writerow(["Iteration", "Action", "Payoff", "Selection Method"])

        for i in range(1000):
            action = self.game.agent_a_action[i]
            payoff = self.game.agent_a_payoffs[i]
            rg = self.game.agent_a_rg[i]
            to_write = ([i, action, payoff, rg])
            a_writer.writerow(to_write)
            print("ITERATING")
        fa.close()

        with open("agent_b.csv", 'w', newline='') as fb:
            b_writer = csv.writer(fb)
            b_writer.writerow(["Iteration", "Action", "Payoff", "Selection Method"])

            for i in range(1000):
                action = self.game.agent_b_action[i]
                payoff = self.game.agent_b_payoffs[i]
                rg = self.game.agent_b_rg[i]
                b_writer.writerow([i, action, payoff, rg])
