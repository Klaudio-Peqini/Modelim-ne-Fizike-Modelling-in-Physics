
import matplotlib.pyplot as plt

def plot_sir(t, S, I, R):
    plt.figure()
    plt.plot(t, S, label="S")
    plt.plot(t, I, label="I")
    plt.plot(t, R, label="R")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Population fraction")
    plt.title("SIR Epidemic Dynamics")
    plt.show()
