def w_sum(inputs, weights):
    assert (len(weights) == len(weights))
    output = 0
    for i in range(len(inputs)):
        output += input[i] * weights[i]
    return output

def neural_network(inputs, weights):
    pred = w_sum(inputs, weights)
    return pred

weights = [.2, .3, 0]

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [.65, .8, .8, .9]
nfans = [1.2, 1.3, .5, 1]

input = [toes[0], wlrec[0], nfans[0]]

pred = neural_network(input, weights)

print(pred)