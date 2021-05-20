weight = .5
inp = .5
goal_pred = 0.8

for _ in range(20):
    pred = inp * weight
    err = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * inp
    weight = weight - direction_and_amount
    print('Err: ' + str(err) + ' Pred: ' + str(pred))
