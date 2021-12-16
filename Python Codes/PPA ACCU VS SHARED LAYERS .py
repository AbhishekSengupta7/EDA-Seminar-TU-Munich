import matplotlib.pyplot as plt
 
# line 1 points
x1 = [1,2,3,4,5]
y1 = [93, 94.3, 95.2, 95.2, 94.9]
# plotting the line 1 points
plt.plot(x1, y1, label = "Training samples : 200")
 
# line 2 points
x2 = [1,2,3,4,5]
y2 = [94.3, 94.5, 94.4, 95.5, 95.2]
# plotting the line 2 points
plt.plot(x2, y2, label = "Training samples : 100")



# line 1 points
x3 = [1,2,3,4,5]
y3 = [94.7, 95.2, 95.7, 96.1, 96.4]
# plotting the line 1 points
plt.plot(x3, y3, label = "Training samples : 50")
 
# line 2 points
x4 = [1,2,3,4,5]
y4 = [95.2, 95.4, 95.9, 96.5, 97.16]
# plotting the line 2 points
plt.plot(x4, y4, label = "Training samples : 20")
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