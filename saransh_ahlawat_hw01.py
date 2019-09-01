# Author: Saransh Ahlawat (10444938)

import unittest

def classify_triangle(a, b, c):
    result = list()
    if not((isinstance(a, int) or isinstance(a, float)) and a > 0):
        notify_invalid_input()
        result.append("NotATriangle")
        return result
    if not((isinstance(b, int) or isinstance(b, float)) and b > 0):
        notify_invalid_input()
        result.append("NotATriangle")
        return result
    if not((isinstance(c, int) or isinstance(c, float)) and c > 0):
        notify_invalid_input()
        result.append("NotATriangle")
        return result

    if not (a < b + c and b < a + c and c < a + b):
        result.append("NotATriangle")
        return result
    
    if a == b and b == c:
        print("Equilateral")
        result.append("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
        result.append("Isosceles")
    elif a != b and b != c and a != c:
        print("Scalene")
        result.append("Scalene")

    longest_side = get_longest_side(a, b ,c)
    if longest_side == a:
        if a * a == b * b + c * c:
            print("The triangle is also a right angled triangle.")
            result.append("Right triangle")
    elif longest_side == b:
        if b * b == a * a + c * c:
            print("The triangle is also a right angled triangle.")
            result.append("Right triangle")
    else:
        if c * c == a * a + b * b:
            print("The triangle is also a right angled triangle.")
            result.append("Right triangle")

    return result


def notify_invalid_input():
    print(f"Please add numeric dimensions.")

def get_longest_side(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c



class saransh_ahlawat_hw01(unittest.TestCase):
    def test_classify_triangle(self):         
        self.assertEqual(classify_triangle(3, 5, 4), ["Scalene", "Right triangle"])
        self.assertEqual(classify_triangle(4, 3, 5), ["Scalene", "Right triangle"])
        self.assertEqual(classify_triangle(3, 4, 5), ["Scalene", "Right triangle"])
        self.assertEqual(classify_triangle(3, 2, 3.61), ["Scalene"])
        self.assertEqual(classify_triangle(3, 5, 5), ["Isosceles"])
        self.assertEqual(classify_triangle(0, 5, 4), ["NotATriangle"])
        self.assertEqual(classify_triangle(3, 5, ''), ["NotATriangle"])
        self.assertEqual(classify_triangle(3, 5, 20), ["NotATriangle"])
        self.assertEqual(classify_triangle('', '', '20'), ["NotATriangle"])
        self.assertEqual(classify_triangle(3, 5, '20'), ["NotATriangle"])
        self.assertEqual(classify_triangle('test', 'whatever', 'test1'), ["NotATriangle"])
        self.assertEqual(classify_triangle('', '', ''), ["NotATriangle"])
        self.assertEqual(classify_triangle(20, 3, 4), ["NotATriangle"])


def main():
    unittest.main(exit=False, verbosity=2)


if __name__ == '__main__':
    main()