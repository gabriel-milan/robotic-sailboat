###
#
#   This file shall plot coefficients for the CSV file on "/examples/data" folder
#
###

# Macros
CSV_FILE_PATH = "data/data.csv"

# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Loading data
def load_data (path = CSV_FILE_PATH):
    data = pd.read_csv(path).replace(',', '.', regex=True).apply(pd.to_numeric)
    return data

# Plot the data you want
def plot_this (data, x_label, y_label, color = 'tab:blue', show_grid = True):
    plt.plot(data[x_label], data[y_label], color=color)
    plt.grid(b = show_grid)
    plt.show()
    return

# Plot multiple data sharing X axis
def multiple_plot (data, x_label, y_labels_list, colors_list = ['tab:red', 'tab:green', 'tab:blue']):

    fig, ax0 = plt.subplots()
    plt.grid(b = True, axis = 'x')
    color = 'tab:red'
    ax0.set_xlabel(x_label)
    ax0.set_ylabel(y_labels_list[0], color = colors_list[0])
    ax0.plot(data[x_label], data[y_labels_list[0]], color = colors_list[0])
    ax0.tick_params(axis='y', labelcolor = colors_list[0])

    if (len(y_labels_list) > 1):
        for i in range(1, len(y_labels_list)):
            new_ax = ax0.twinx()
            new_ax.set_ylabel(y_labels_list[i], color = colors_list[i])
            new_ax.plot(data[x_label], data[y_labels_list[i]], color = colors_list[i])
            new_ax.tick_params(axis='y', labelcolor = colors_list[i])

    fig.tight_layout()
    plt.show()

# Find the greatest Y value in data for Y versus X
def max_value (data, x_label, y_label):
    references = {
        'Alpha' : 0,
        'Cl' : 1,
        'Cd' : 2,
        'Cr' : 3
    }
    indexes = data.idxmax()
    return (data[x_label][indexes[references[y_label]]], data[y_label][indexes[references[y_label]]])

if __name__ == '__main__':
    ### Load data with the following line
    # data = load_data()

    ### Do something with the data, examples below
    #
    ### -> Print the max Cl and the corresponding Alpha
    # print (max_value (data, 'Alpha', 'Cl'))
    #
    ### -> Plot Cl and Cr on the same X axis with different scales
    # multiple_plot (data, 'Alpha', ['Cl', 'Cr'])

    print ("Hello stranger!")
    print ("Thanks for checking this out! Please edit this source code in order to achieve what you came for, there are examples on the main block.")