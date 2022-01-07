# Multi-Agent Systems, Machine-Learning and Game-Theory

This repository contains code built to facilitate the play of 2-player Single-Objective Normal Form Games (such as Chicken or the Prisoners Dilemma) by Q-Learning Agents.



New 2-action NFG payoff tables can be added to "main.py" as matrices
The following snippet shows the payoff matrix for the game of chicken in a layout compatible with this program - 

```
chicken_payoffs = [  
    [6, 6], [2, 8],
    [8, 2], [0, 0]
]

```

![image](https://user-images.githubusercontent.com/59183705/148554370-92a34500-0ff7-4ce5-a29a-2c1434e82eaa.png)
| Payoff table for the game of Chicken |

Agent and game settings can also be altered from within the "main.py" file.




