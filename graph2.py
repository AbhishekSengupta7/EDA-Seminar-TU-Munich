# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 04:03:54 2021

@author: abhis
"""

import matplotlib.pyplot as plt
 
# line 1 points
x1 = ["Dynamic Power","Critical Path","Area","PPA"]
y1 = [97.21, 98.13, 98.70, 98.16]
# plotting the line 1 points
plt.plot(x1, y1, label = "Neural Network")
 
# line 2 points
x2 = ["Dynamic Power","Critical Path","Area","PPA"]
y2 = [97.40, 97.64, 98.64, 98.43]
# plotting the line 2 points
plt.plot(x2, y2, label = "Decision Tree")


# line 1 points
x3 = ["Dynamic Power","Critical Path","Area","PPA"]
y3 = [97.75, 97.91, 98.16, 98.20]
# plotting the line 1 points
plt.plot(x3, y3, label = "Gradient Boost Regressor")
 



plt.xlabel('Accuracy parameters')
# naming the y axis
plt.ylabel('Prediction Accuracy (in %)')
# giving a title to my graph
plt.title('Prediction Accuracy vs Accuracy parameters')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()



