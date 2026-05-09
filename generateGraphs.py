import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


import parseCSV


def generateGraphs(file):
    data = parseCSV.readCSV(file)
    # Process data and generate graphs

    print('Graphs generated successfully')