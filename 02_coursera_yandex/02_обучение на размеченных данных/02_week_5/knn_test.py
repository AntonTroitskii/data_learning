import unittest

from knn import distance, get_knn_index, get_1nn_index, NeighborClassifier
import numpy as np


class KNN_Test(unittest.TestCase):

    def test_distance(self):

        v1 = np.array([1, 1, 1])
        v2 = np.array([0, 0, 0])

        dist = distance(v1, v2)

        self.assertEqual(dist, np.sqrt(3))

        v1 = np.array([-1, -1, -1])
        v2 = np.array([0, 0, 0])

        dist = distance(v1, v2)

        self.assertEqual(dist, np.sqrt(3))

    def test_get_knn_index(self):
        v1 = np.array([0, 0, 1])
        v2 = np.array([0, 0, 2])
        v3 = np.array([0, 0, 3])
        v4 = np.array([0, 0, 4])
        v5 = np.array([0, 0, 5])

        v_list = [v1, v2, v3, v4, v5]

        vt_1 = np.array([0, 0, 6])
        res1 = get_knn_index(v_list, vt_1, k=1)
        self.assertEqual([4], res1)

        vt_2 = np.array([0, 6, 0])
        res2 = get_knn_index(v_list, vt_2, k=1)
        self.assertEqual([0], res2)

        vt_3 = np.array([0, -4.1, 0])
        res3 = get_knn_index(v_list, vt_3, k=1)
        self.assertEqual([0], res3)
    
    def test_get_1nn_index(self):
        
        v1 = np.array([0, 0, 1])
        v2 = np.array([0, 0, 2])
        v3 = np.array([0, 0, 3])
        v4 = np.array([0, 0, 4])
        v5 = np.array([0, 0, 5])

        v_list = [v1, v2, v3, v4, v5]

        vt_1 = np.array([0, 0, 6])
        res1 = get_1nn_index(v_list, vt_1)
        self.assertEqual(4, res1)

        vt_2 = np.array([0, 6, 0])
        res2 = get_1nn_index(v_list, vt_2)
        self.assertEqual(0, res2)

        vt_3 = np.array([0, -4.1, 0])
        res3 = get_1nn_index(v_list, vt_3)
        self.assertEqual(0, res3)


    def test_get_1nn_predictd(self):
    
        v1 = np.array([0, 0, 1])
        v2 = np.array([0, 0, 2])
        v3 = np.array([0, 0, 3])
        v4 = np.array([0, 0, 4])
        v5 = np.array([0, 0, 5])

        X_train = [v1, v2, v3, v4, v5]
        y_list = [0, 1, 0, 1, 1]

        nn_clf = NeighborClassifier(X_train, y_list)

        vt_1 = np.array([0, 0, 6])
        vt_2 = np.array([0, 6, 0])
        vt_3 = np.array([0, -4.1, 0])

        X_test = [vt_1, vt_2, vt_3]

        res1 = nn_clf.predict(X_test)

        self.assertEqual([1, 0, 0], res1)

if __name__ == '__main__':
    unittest.main()
