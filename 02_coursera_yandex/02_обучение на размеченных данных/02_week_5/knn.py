from numpy.linalg import norm


def distance(v1, v2):
    sub = v1 - v2
    return norm(sub)


def get_knn_index(ar, v, k=5):

    distance_list = []

    for i in range(0, len(ar)):
        distance_list.append([i, distance(ar[i], v)])

    distance_list.sort(key=lambda x: x[1])

    return list(map(lambda x: x[0], distance_list[0:k]))


def get_1nn_index(ar, v):
    dist = distance(ar[0], v)

    min_dist, min_dist_ind = dist, 0

    for i in range(1, len(ar)):
        dist = distance(ar[i], v)
        if dist < min_dist:
            min_dist, min_dist_ind = dist, i

    return min_dist_ind


def get_1nn_predict(X, y, v):
    ind = get_1nn_index(X, v)
    return y[ind]


class NeighborClassifier():
    def __init__(self, X, y) -> None:
        super()
        self.X = X
        self.y = y

    def predict(self, X_test):
        res = []
        for xi in X_test:
            res.append(get_1nn_predict(self.X, self.y, xi))

        return res