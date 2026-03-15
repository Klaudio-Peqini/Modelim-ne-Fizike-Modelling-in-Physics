
import matplotlib.pyplot as plt

def plot_traffic(history):
    plt.figure()
    plt.imshow(history, aspect='auto')
    plt.xlabel("Road Position")
    plt.ylabel("Time")
    plt.title("Traffic Simulation")
    plt.show()
