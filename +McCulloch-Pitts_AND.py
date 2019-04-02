
# coding: utf-8

# In[ ]:

#make prediction with weights
def predict(row,weights):
	activation = 0.0
	for i in range(len(row)-1):
		activation += weights[i] * row[i]
	return 1.0 if activation >= 2.0 else 0.0

#test predictions
dataset = [[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
weights = [1,1]
for row in dataset:
	prediction = predict(row,weights)
	print("Expected=%d,Predicted=%d" %(row[-1],prediction))
  

