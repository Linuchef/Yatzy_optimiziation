import matplotlib.pyplot as plt 

def plot_histogram(score_values : list[int]) -> None:

    n = len(score_values)

    plt.hist(score_values, color = 'skyblue', edgecolor = 'black')

    plt.xlabel("score")
    plt.ylabel("Frequency")
    plt.title(f'Histogram of {n} simulations of forced yatzy')
    plt.show()