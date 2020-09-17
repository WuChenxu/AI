# https://scikit-learn.org/stable/modules/tree.html
# import dataset
# train a classifier
# predict label for new flower
# visualize the tree
#### import dataset ####
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])
for i in range(len(iris.target)):
    print("Example %d: label %s, feature_names %s" %(i, iris.target[i], iris.data[i]))


#### train a classifier ####
#### test data
##### examples used to "test" the classifier's accurancy
##### not part of the training data
import numpy as np
test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

from sklearn import tree 

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)
print(test_target)
print(clf.predict(test_data))

## viz
# import graphviz # conda install python-graphviz
# dot_data = tree.export_graphviz(clf, out_file=None) 
# graph = graphviz.Source(dot_data) 
# graph.render("iris") 
# dot_data = tree.export_graphviz(clf, out_file=None, 
#                      feature_names=iris.feature_names,  
#                      class_names=iris.target_names,  
#                      filled=True, rounded=True,  
#                      special_characters=True)  
# graph = graphviz.Source(dot_data)  
# graph 

# export text 
from sklearn.tree import export_text
r = export_text(clf, feature_names=iris['feature_names'])
print(r)