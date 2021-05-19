def neural_network(inp, weight):
    return inp * weight


weight = .1

number_of_toes = [8.5]
win_or_lose_binary = [1]

inp = number_of_toes[0]
expected = win_or_lose_binary[0]

lr = 0.01
p_up = neural_network(inp,weight+lr)
e_up = (p_up - expected) ** 2
print(e_up)

print(err)
