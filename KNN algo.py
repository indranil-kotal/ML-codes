from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier(n_neighbors=5)
# Training data
X_train = [[-2.62484591 , 8.71318243],[ 3.53354386 , 0.77696306],
[-3.6601912 , 9.38998415],
[ 4.73163961 ,-0.01439923],[ 4.6040528 , 3.53781334],
[-4.23411546 , 8.4519986 ],[-0.92998481 , 9.78172086],
[ 4.97114227 , 2.94871481]]
y_train = [ 0, 1, 0, 1, 1, 0, 0, 1]
knn.fit(X_train, y_train)
# Test data
X_test = [[2.604052, 3.451998], [4.7769, 5.971142],[ 4.60405282 , 3.53781334],[-
5.62484591 , 6.71318243]]
y_test = [1 , 1 , 1 , 1]
predictions = knn.predict(X_test)
print(predictions)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
