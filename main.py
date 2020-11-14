from Agent import Agent
from Game_Runner import GameRunner
from Utilities import Util

chicken_pt = [
    # s,s    s,d
    [6, 6], [2, 7],
    # d,s    d,d
    [7, 2], [0, 0]
]
agent_a = Agent(name="A", debug=True)
agent_b = Agent(name="B", debug=True)
pd_payoff_table = [
    # c,c    c,d
    [3, 3], [0, 5],
    # d,c    d,d
    [5, 0], [0, 0]
]

if __name__ == '__main__':

    prisoners_dilemma = GameRunner(agent_a=agent_a, agent_b=agent_b, payoff_table=pd_payoff_table)
    util = Util(prisoners_dilemma)
    for i in range(1000):
        print("")
        print("--------------------- Iteration", i, "-----------------------")
        prisoners_dilemma.pd_play_round()

    print("Writing data to csv")
    util.write_to_csv()
    print("Data successfully written to csv")
