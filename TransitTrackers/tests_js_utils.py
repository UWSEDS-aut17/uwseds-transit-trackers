import unittest
import js_utils
import geopandas as gpd

x = r"../Data/zips_sea/shp.shp"
grid = gpd.read_file(x)


class js_test(unittest.TestCase):

    def test_js_code(self):
        # Test for java script code generator function
        # The result of this function is a string and length of it is a
        # function of input
        # So here we test if the output matches the input

        n = 9  # this can be any number
        rn = range(0, n)
        code = js_utils.js_code(rn)
        if n > 10:
            m = 70 * 10 + (n - 10) * 73 + (n - 1) * 5 + 88
        if n <= 10:
            m = 70 * n + (n - 1) * 5 + 88
        self.assertEqual(len(code), m)

    def test_income_classifier(self):
        # Test the function that adds income bins to the data
        # Here we test if the bin column is added to the data

        gr = js_utils.income_classifier(grid)
        self.assertEqual(list(gr)[-1], 'bin')


if __name__ == '__main__':
    unittest.main()
