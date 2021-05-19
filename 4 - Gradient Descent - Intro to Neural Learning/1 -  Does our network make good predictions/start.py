knob_weight = .5
inp = .5
goal_pred = .8

pred = knob_weight * inp
err = (pred - goal_pred) ** 2
print(err)
