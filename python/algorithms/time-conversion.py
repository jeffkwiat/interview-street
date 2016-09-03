#!/bin/python3

import sys
import unittest

class TimeConversion:

    def convert_time(self, time):
        hh = time[0:2]
        mm = time[3:5]
        ss = time[6:8]
        ampm = time[-2:]

        if ampm == 'AM':
            if hh == '12':
                hh = '00'
                
        elif ampm == 'PM':
            if int(hh) < 12:
                hh = int(hh) + 12
            
        print('%s:%s:%s' % (hh, mm, ss))
        return '%s:%s:%s' % (hh, mm, ss)


class TestTimeConversion(unittest.TestCase):

    def setUp(self):
        self.converter = TimeConversion()
        
    def test_conversion(self):
        self.assertEqual(self.converter.convert_time('12:00:00AM'), '00:00:00')
        self.assertEqual(self.converter.convert_time('12:00:00PM'), '12:00:00')
        self.assertEqual(self.converter.convert_time('12:54:11AM'), '00:54:11')
        self.assertEqual(self.converter.convert_time('02:30:45PM'), '14:30:45')


if __name__ == '__main__':
    unittest.main()