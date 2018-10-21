from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
#getting the f-measure
def f_measure(kernel, X, y):

  true_positive = 0
  false_positive = 0
  true_negative = 0
  false_negative = 0

  for i in range(len(X)):
    prediction = svcLinearKernel.predict([X[i]])
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

#loading the cleaned csv in for parsing
def load_data():
  data = []
  with open("cleaned_chronic_kidney_disease_data.csv", 'r') as csv:
      lines = csv.read().split('\n')
      for i, l in enumerate(lines):
          currentValue = []
          for a in l.split(',')[:25]:
              currentValue.append(float(a))
          data.append(currentValue)
  return data

data = load_data()

xTraining = [d[:len(d)-2] for d in data[:int(len(data) * .8)]]
xTesting = [d[:len(d)-2] for d in data[int(len(data) * 0.2):]]
yTraining = [d[len(d)-1] for d in data[:int(len(data) * .8)]]
yTesting = np.array([d[len(d)-1] for d in data[int(len(data) * 0.2):]])

svcLinearKernel = SVC(kernel='linear')
svcLinearKernel .fit(xTraining, yTraining)
print("SVC Linear Kernel TRAINING f-measure: " + str(f_measure(svcLinearKernel, xTraining, yTraining)))
print("SVC Linear Kernel TEST f-measure: " + str(f_measure(svcLinearKernel, xTesting, yTesting))+ '\n \n')

svcLinearKernel = SVC(kernel='rbf')
svcLinearKernel.fit(xTraining, yTraining)
print("SVC RBF TRAINING f-measure: " + str(f_measure(svcLinearKernel, xTraining, yTraining)))
print("SVC RBF TEST f-measure: " + str(f_measure(svcLinearKernel, xTesting, yTesting)) + '\n \n')

svcLinearKernel = RandomForestClassifier()
svcLinearKernel.fit(xTraining, yTraining)
print("Random Forest TRAINING f-measure: ", f_measure(svcLinearKernel, xTraining, yTraining))
print("Random Forest TEST f-measure: ", f_measure(svcLinearKernel, xTesting, yTesting))

