from Agent import Agent
from Game_Runner import GameRunner
from Utilities import Util

if __name__ == '__main__':

    agent_a = Agent(name="A", debug=True)
    agent_b = Agent(name="B", debug=True)
    prisoners_dilemma = GameRunner(agent_a=agent_a, agent_b=agent_b)
    util = Util(prisoners_dilemma)
    for i in range(1000):
        print("")
        print("--------------------- Iteration", i, "-----------------------")
        prisoners_dilemma.pd_play_round()

    print("Writing data to csv")
    util.write_to_csv()
    print("Data successfully written to csv")
