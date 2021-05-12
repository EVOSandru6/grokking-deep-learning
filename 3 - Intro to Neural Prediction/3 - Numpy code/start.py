import numpy as np

def neural_network(inputs, weights):
    pred = inputs.dot(weights)
    return pred

weights = np.array([.2, .3, 0])

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([.65, .8, .8, .9])
nfans = np.array([1.2, 1.3, .5, 1])

input = np.array([toes[0], wlrec[0], nfans[0]])

pred = neural_network(input, weights)

print(pred)