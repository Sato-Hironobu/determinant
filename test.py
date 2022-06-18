import unittest
from determinant import determinant

class TestDeterminantValue(unittest.TestCase):

    def test_2_dim(self):
        test_cases = [
            ([[1,2],
              [3,4]], -2),
            ([[3,2],
              [5,4]],  2),
        ]
        for matrix, det in test_cases:
            self.assertEqual(determinant(matrix), det)

    def test_3_dim(self):
        test_cases = [
            ([[1,3,2],
              [5,4,6],
              [8,9,7]], 39),
        ]
        for matrix, det in test_cases:
            self.assertEqual(determinant(matrix), det)    

    def test_4_dim(self):
        test_cases = [
            ([[ 3, 9,-4,12],
              [ 0, 1, 8, 4],
              [ 0, 0,-1, 7],
              [ 0, 0, 0,10]], -30),
            ([[-1, 1, 6, 8],
              [ 9, 1, 0, 9],
              [ 2, 0, 0, 4],
              [ 0, 0, 0, 3]], -36),
            ([[ 7, 0, 7, 6],
              [ 3, 8, 3, 5],
              [ 1, 9, 1, 2],
              [ 2, 4, 2, 1]], 0),
            ([[ 3, 4, 6, 2],
              [ 2, 4, 9, 3],
              [ 4, 1,-3,-1],
              [ 3, 1, 3, 1]], 0),
            ([[ 2, 0, 5, 2],
              [ 9, 0, 7, 2],
              [ 1, 0, 4, 3],
              [ 3, 0, 3, 0]], 0),
            ([[ 3, 1, 5, 2],
              [ 0, 1, 2, 1],
              [ 0, 1, 1, 1],
              [ 0, 0, 2, 1]], -3),
        ]
        for matrix, det in test_cases:
            self.assertEqual(determinant(matrix), det)

if __name__ == "__main__":
    unittest.main()