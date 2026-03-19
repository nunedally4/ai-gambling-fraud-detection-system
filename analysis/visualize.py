import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/bets.csv")
plt.scatter(data["bet_amount"], data["time_between_bets"])

plt.xlabel("Bet Amount")
plt.ylabel("Time Between bets")
plt.title("Betting Behavior Analysis")

plt.show()
plt.savefig("images/graph.png")