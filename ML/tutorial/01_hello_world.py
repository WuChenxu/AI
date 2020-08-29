from sklearn import tree
# weight  texture label
# 140     smooth  apple
# 130     smooth  apple
# 150     bumpy   orange
# 170     bumpy   orange

# smooth - 1, bumpy - 0 
# apple - 0, orange - 1
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1] 

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
# 150, bumpy
print(clf.predict([[150, 0]]))



