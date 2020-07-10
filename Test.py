import math
import os

import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression



def foo():
    y = 25*math.pi
    print("y is ", y)
    y = 2**400
    print("y is ", y)
    print("cwd is ", os.getcwd())
    df = pd.read_excel('ENB2012_data.xlsx')
    print(df.head())

    plt.hist(df.X1)
    plt.show()

    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()
    # for x in range(6):
    #     print("x is", x, "Hello world")

if __name__ == "__main__":
    x = 5
    y = "John"
    print(y+x)
    # foo()