def w_sum(i_vector, weights):
    assert (len(i_vector) == len(weights))
    out = 0
    for i in range(len(i_vector)):
        out += i_vector[i] * weights[i]
    return out


def vect_mat_mul(i_vector, w_matrix):
    assert (len(i_vector) == len(w_matrix))
    out = [0, 0, 0]
    for i in range(len(i_vector)):
        out[i] = w_sum(i_vector, w_matrix[i])
    return out

def neural_network(i_vector, w_matrix):
    pred = vect_mat_mul(i_vector, w_matrix)
    return pred


# toes %win #fans
weights = [
    [0.1, 0.1, -0.3],  # hurt?
    [0.1, 0.2, 0.0],  # win?
    [0.0, 1.3, 0.1]  # sad?
]

# This dataset is the current
# status at the beginning of
# each game for the first 4 games
# in a season.

# toes = current number of toes
# wlrec = current games won (percent)
# nfans = fan count (in millions)

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# Input corresponds to every entry
# for the first game of the season.

input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(input, weights)

print(pred)
