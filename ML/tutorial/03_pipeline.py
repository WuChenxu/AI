# import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

# seperate train and test dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# choose a classifier
# from sklearn import tree 
# my_classifier = tree.DecisionTreeClassifier()
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

# train
my_classifier.fit(X_train, y_train)

# predict
predictions = my_classifier.predict(X_test)

# evalute the classifier
from sklearn.metrics import accuracy_score
print (accuracy_score(y_test, predictions))