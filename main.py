from Agent import Agent
from Game_Runner import GameRunner
from Utilities import Util

chicken_pt = [
    # s,s    s,d
    [6, 6], [2, 7],
    # d,s    d,d
    [7, 2], [0, 0]
]

prisoners_dilemma_pt = [
    # c,c    c,d
    [3, 3], [0, 5],
    # d,c    d,d
    [5, 0], [0, 0]
]

if __name__ == '__main__':

    agent_a = Agent(name="A", debug=False)
    agent_b = Agent(name="B", debug=False)

    game1 = GameRunner(agent_a=agent_a, agent_b=agent_b, payoff_table=chicken_pt)

    util = Util(game1)

    # iterations = 20000
    # for i in range(iterations):
    #     print("")
    #     print("--------------------- Iteration", i+1, "of", iterations, "-----------------------")
    #
    #     prisoners_dilemma.pd_play_round()

    game1.play_episodes(10000, decay_alpha_a=False, decay_alpha_b=False)



    print("Writing data to csv")
    #util.write_both_to_csv()
    util.write_choices_to_csv()
    print("Data successfully written to csv")
