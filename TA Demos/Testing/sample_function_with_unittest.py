import unittest



def generate_triangle(height: int) -> str:    
    assert height >= 0, "Negative height is not allowed."
    triangle = '\n'.join('*' * (i + 1) for i in range(height))
    return triangle

class TestTriangle(unittest.TestCase):
    def test_generate_negative_height_triangle(self):
        self.assertRaises(AssertionError, generate_triangle, -1)

    def test_generate_positive_height_triangle(self):
        result = generate_triangle(5)
        self.assertEqual(result, '*\n**\n***\n****\n*****')

if __name__ == '__main__':
    unittest.main()


