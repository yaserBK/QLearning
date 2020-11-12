from Agent import Agent
from Game_Runner import GameRunner

if __name__ == '__main__':

    agent_a = Agent(name="A", debug=True)
    agent_b = Agent(name="B", debug=True)

    game = GameRunner(agent_a=agent_a, agent_b=agent_b)
    for i in range(1000):
        print("")
        print("--------------------- Iteration", i, "-----------------------")
        game.pd_play_round()
        print("__________------______------______")
        print()
