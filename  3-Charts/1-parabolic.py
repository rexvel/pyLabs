import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


def parabolic():


    x = np.linspace(-20, 20)

    y1 = 2 * x ** 2

    y2 = 0.5 * x ** 2

    y = x ** 2

    fig = plt.figure()
    plt.rc('axes', edgecolor='red')

    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Romanenko')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # ax.xaxis.set_major_locator(loc)
    # ax.yaxis.set_major_locator(loc)


    plt.plot(x, y, 'r')

    plt.plot(x, y1, 'g')

    plt.plot(x, y2, 'blue')


    ax.set_facecolor('orange')

    fig.patch.set_facecolor('violet')

    plt.grid(color='grey',  linewidth=1, which='major' ,drawstyle="steps")

    plt.show()


parabolic()


