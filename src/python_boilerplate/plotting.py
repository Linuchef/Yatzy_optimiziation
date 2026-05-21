import matplotlib.pyplot as plt 
from typing import Dict

def plot_histogram(score_values : list[int]) -> None:

    n = len(score_values)

    plt.hist(score_values, color = 'skyblue', edgecolor = 'black', bins = 40)

    plt.xlabel("score")
    plt.ylabel("Frequency")
    plt.title(f'Histogram of {n} simulations of forced yatzy')
    plt.show()

def category_distribution_plot(
        dic : Dict[int, float],
        title : str,
        same_face : bool = False) -> None:

    x = list(dic.keys())
    y = list(dic.values())

    plt.bar(x, y, width=0.5)
    plt.grid(axis='y', alpha=0.3)

    if same_face:
        plt.xlabel("Number of Matching Dice")
    else:
        plt.xlabel("Score")
    plt.ylabel("Probability")
    plt.title(title)
    plt.xticks(x)

    plt.tight_layout()
    plt.show()
