from Agent import Agent
from Game_Runner import GameRunner
from Utilities import Util

# payoff tables for different games:

chicken_pt = [  # Chicken
    # s,s    s,d
    [6, 6], [2, 7],
    # d,s    d,d
    [7, 2], [0, 0]
]

prisoners_dilemma_pt = [  # Prisoners Dilemma
    # c,c    c,d
    [3, 3], [0, 5],
    # d,c    d,d
    [5, 0], [0, 0]
]

if __name__ == '__main__':

    #initialising agents a and b:
    agent_a = Agent(name="A", debug=True)
    agent_b = Agent(name="B", debug=False)

    # initialising game with agents and a choice of static payoff table:
    game1 = GameRunner(agent_a=agent_a, agent_b=agent_b, payoff_table=chicken_pt)

    # Playing 1000oo episodes without decaying epsilon:
    game1.play_episodes(10000, decay_alpha_a=False, decay_alpha_b=False)

    util = Util(game1)
    # writing game data to csv:
    print("Writing data to csv")
    util.write_choices_to_csv()
    #util.write_both_to_csv()
    print("Data successfully written to csv")
