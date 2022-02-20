def neural_network(inp, weight):
    return inp * weight


weight = .1
lt = 0.01  # приращение

number_of_toes = [8.5]
win_or_lose_binary = [1]

inp = number_of_toes[0]
expected = win_or_lose_binary[0]

pred = neural_network(inp, weight)

err = (pred - expected) ** 2

print(err)
