# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 04:03:54 2021

@author: abhis
"""

import matplotlib.pyplot as plt
 
# line 1 points
x1 = ["Dynamic Power","Critical Path","Area","PPA"]
y1 = [96.21, 97.13, 97.70, 97.16]
# plotting the line 1 points
plt.plot(x1, y1, label = "Neural Network")
 
# line 2 points
x2 = ["Dynamic Power","Critical Path","Area","PPA"]
y2 = [96.40, 96.64, 97.64, 97.43]
# plotting the line 2 points
plt.plot(x2, y2, label = "Decision Tree")


# line 1 points
x3 = ["Dynamic Power","Critical Path","Area","PPA"]
y3 = [96.75, 96.91, 97.16, 97.20]
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



