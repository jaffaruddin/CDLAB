# KNN
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size = .25, random_state = 42)
clf = KNeighborsClassifier()
clf.fit(X_train, Y_train)
print(f"Accuracy = {clf.score(X_test, Y_test)}")
print("Predicted Data : ")
prediction = clf.predict(X_test)
print(prediction)
print("Test data : ")
print(Y_test)
diff = prediction - Y_test
print("Result is ")
print(diff)
print(f"Total no of samples misclassified = {sum(abs(diff))}")

-> o/p: 
Accuracy = 1.0
Predicted Data : 
[1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1
 0]
Test data : 
[1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1
 0]
Result is 
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0]
Total no of samples misclassified = 0
