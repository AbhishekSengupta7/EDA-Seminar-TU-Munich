import matplotlib.pyplot as plt
 
# line 1 points
x1 = [1,2,3,4,5]
y1 = [94, 95.3, 96.2, 96.2, 95.9]
# plotting the line 1 points
plt.plot(x1, y1, label = "Training samples : 20")
 
# line 2 points
x2 = [1,2,3,4,5]
y2 = [95.3, 95.5, 96.4, 96.5, 96.2]
# plotting the line 2 points
plt.plot(x2, y2, label = "Training samples : 50")



# line 1 points
x3 = [1,2,3,4,5]
y3 = [95.7, 96.2, 96.7, 97.1, 97.4]
# plotting the line 1 points
plt.plot(x3, y3, label = "Training samples : 100")
 
# line 2 points
x4 = [1,2,3,4,5]
y4 = [96.2, 96.4, 96.9, 97.5, 97.8]
# plotting the line 2 points
plt.plot(x4, y4, label = "Training samples : 200")
# naming the x axis
plt.xlabel('Number of Shared Layers')
# naming the y axis
plt.ylabel('PPA Prediction Accuracy (in %)')
# giving a title to my graph
plt.title('PPA Prediction Accuracy vs Number of Shared Layers')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()