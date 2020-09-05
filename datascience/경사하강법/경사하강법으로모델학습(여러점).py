from typing import List
from datascience.mathematics.vector import vector_mean #fixme 이전 글 참고
from datascience.경사하강법.경사하강법으로모델학습 import linear_gradient #fixme 이전 글 참고
from datascience.경사하강법.최저점구하기 import gradient_step #fixme 이전 글 참고

import random

Vector = List[float]
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]

#fixme Start with random values for slope and intercept
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

for epoch in range(5000):
    #fixme Compute the mean of the gradients
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
    #fixme Take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)


slope, intercept = theta
assert 19.9 < slope < 20.1, "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept shuld be about 5"




