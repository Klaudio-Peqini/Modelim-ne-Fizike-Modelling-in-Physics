
import matplotlib.pyplot as plt

def phase_plot(x, y, xlabel="x", ylabel="y", title="Phase Plot"):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
