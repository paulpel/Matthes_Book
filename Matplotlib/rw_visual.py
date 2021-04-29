import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #dane
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #wyświetlanie
    plt.style.use('classic')
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8, forward=True)

    number_points = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=number_points, cmap=plt.cm.Blues, edgecolor='none', s=15)
    start = ax.scatter(0, 0, c='green', edgecolors='none', s=50)
    end = ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    ax.legend((start, end), ('Start', 'Finish'), scatterpoints=1, loc='upper right')

    #ukrycie osi
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    mng = fig.canvas.manager
    plt.show()

    keep_running = 'y' #input('Keep running? (y/n)').lower()
    if keep_running == 'n':
        break
