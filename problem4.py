from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from DataHandler import load_data


def f_measure(predictor, X, y):

  true_positive = 0
  false_positive = 0
  true_negative = 0
  false_negative = 0

  for i in range(len(X)):
    prediction = clf.predict([X[i]])
    if y[i] == 1:
      if prediction == 1:
        true_positive += 1
      else:
        false_positive += 1
    elif y[i] == 0:
      if prediction == 0:
        true_negative += 1
      else:
        false_negative += 1

  precision = true_positive / (true_positive + false_positive)
  recall = true_positive / (true_positive + false_negative)

  return (2 * precision * recall) / (precision + recall)


data = load_data()

train_X = [d[:24] for d in data[:int(len(data) * .8)]]
train_y = [d[24] for d in data[:int(len(data) * .8)]]

test_X = [d[:24] for d in data[int(len(data) * 0.2):]]
test_y = [d[24] for d in data[int(len(data) * 0.2):]]

clf = SVC(kernel='linear')
clf.fit(train_X, train_y)

print("SVC linear training set f-measure: ", f_measure(clf, train_X, train_y))
print("SVC linear test set f-measure: ", f_measure(clf, test_X, test_y))


clf = SVC(kernel='rbf')
clf.fit(train_X, train_y)

print("SVC rbf training set f-measure: ", f_measure(clf, train_X, train_y))
print("SVC rbf test set f-measure: ", f_measure(clf, test_X, test_y))


clf = RandomForestClassifier()
clf.fit(train_X, train_y)

print("Random Forest training set f-measure: ", f_measure(clf, train_X, train_y))
print("Random Forest test set f-measure: ", f_measure(clf, test_X, test_y))

