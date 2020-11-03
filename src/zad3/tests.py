import unittest
from zad3 import Song

class TestSong(unittest.TestCase):
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def test_print_line_1(self):
        self.assertEqual(self.temp.line(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_print_line_disallow_negative_value(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.line(-1)
    
    def test_print_line_disallow_out_of_range_value(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.line(132)

    def test_print_line_disallow_non_integer_value(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.line("14")

    def test_print_betweenLines_2_4(self):
        self.assertEqual(self.temp.betweenLines(2, 4), ['On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.', 'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'])

    def test_print_betweenLines_disallow_negative_values(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.betweenLines(-1, -4)
        
    @unittest.skip('not implemented')
    def test_print_betweenLines_disallow_empty_values(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.betweenLines(3)

    @unittest.skip('not implemented')
    def test_print_betweenLines_disallow_first_value_being_bigger_than_second(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.betweenLines(7, 2)

    @unittest.skip('not implemented')
    def test_print_betweenLines_disallow_non_integer_values(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.betweenLines("3", 9)

    @unittest.skip('not implemented')
    def test_print_betweenLines_disallow_out_of_range_values(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.betweenLines(7, 16)

    @unittest.skip('not implemented')
    def test_print_wholeSong(self):
        self.assertEqual(self.temp.wholeSong(), ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.', 'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.', 'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.', 'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'])

    def setUp(self):
        self.temp = Song()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp
    
    def tearDown(self):
        self.temp = None 

if __name__ == '__main__':
    unittest.main()