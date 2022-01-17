import matplotlib.pyplot as plt
 
# line 1 points
# x1 = [0,100,200,300,400]
# y1 = [80.4,86.3,91.4,95.7,97.4]
# # plotting the line 1 points
# plt.plot(x1, y1, label = "Training samples : 20")
 
# line 2 points
x2 = [0,20,40,60,80,100,120,140,160,180,200]
y2 = [84.3, 90.4,95.3,96.7,96.98,97.04,97.16,97.10,97.04,96.9,97.74]
# plotting the line 2 points
plt.plot(x2, y2, label = "Neural Network")

x1 = [0,20,40,60,80,100,120,140,160,180,200]
y1 = [86.64, 94.14,95.35,96.44,96.98,97.04,97.16,97.25,97.43,97.42,97.40]
# plotting the line 2 points
plt.plot(x1, y1, label = "Decision Tree")


x3 = [0,20,40,60,80,100,120,140,160,180,200]
y3 = [87.64, 96.14,96.35,96.44,96.98,97.04,97.16,97.25,97.43,97.42,98.03]
# plotting the line 2 points
plt.plot(x3, y3, label = "Gradient Boost Regressor")
# # line 1 points
# x3 = [0,100,200,300,400]
# y3 = [95.7, 96.2, 96.7, 97.1, 97.4]
# # plotting the line 1 points
# plt.plot(x3, y3, label = "Training samples : 100")
 

plt.xlabel('Training Samples')
# naming the y axis
plt.ylabel('PPA Prediction Accuracy (in %)')
# giving a title to my graph
plt.title('PPA Prediction Accuracy vs Training Samples')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()