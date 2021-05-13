def ele_mul(input, weights):
    out = [0, 0, 0]
    for i in range(len(weights)):
        out[i] = weights[i] * input
    return out

def neural_network(input, weights):
    pred = ele_mul(input, weights)
    return pred

weights = [0.3, 0.2, 0.9]
wlrec = [0.65, 0.8, 0.8, 0.9]

input = wlrec[0]

pred = neural_network(input, weights)

print(pred)