import csv

from Game_Runner import GameRunner


class Util:

    def __init__(self, game):
        self.game = game

    def write_both_to_csv(self):
        fa = open("agent_a.csv", 'w', newline='')
        fb = open("agent_b.csv", 'w', newline='')
        a_writer = csv.writer(fa)
        b_writer = csv.writer(fb)

        a_writer.writerow(["iter_a", "action_a", "payoff_a", "selection_method_a"])
        b_writer.writerow(["iter_b", "action_b", "payoff_b", "selection_method_b"])

        for i in range(len(self.game.agent_b_action)):
            action_a = self.game.agent_a_action[i]
            action_b = self.game.agent_b_action[i]

            payoff_a = self.game.agent_a_payoffs[i]
            payoff_b = self.game.agent_b_payoffs[i]

            rg_a = self.game.agent_a_rg[i]
            rg_b = self.game.agent_b_rg[i]

            a_writer.writerow([(i + 1), action_a, payoff_a, rg_a])
            b_writer.writerow([(i + 1), action_b, payoff_b, rg_b])
        fa.close()
        fb.close()

    def write_choices_to_csv(self):
        fa = open("agent_a_moves.csv", 'w', newline='')
        fb = open("agent_b_moves.csv", 'w', newline='')
        a_writer = csv.writer(fa)
        b_writer = csv.writer(fb)

        a_writer.writerow(["iter_a", "zero_prob_a", "one_prob_a"])
        b_writer.writerow(["iter_b", "zero_prob_b", "one_prob_b"])

        for i in range(len(self.game.a_zero_prob)):
            a_zero = self.game.a_zero_prob[i]
            a_one = self.game.a_one_prob[i]
            b_one = self.game.b_one_prob[i]
            b_zero = self.game.b_zero_prob[i]

            a_writer.writerow([(i + 1), a_zero, a_one])
            b_writer.writerow([(i + 1), b_zero, b_one])
        fa.close()
        fb.close()