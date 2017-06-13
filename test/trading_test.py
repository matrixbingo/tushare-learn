# -*- coding:utf-8 -*- 
'''
Created on 2015/3/14
@author: Jimmy Liu
'''
import unittest
import tushare.stock.trading as fd

class Test(unittest.TestCase):

    def set_data(self):
        self.code = '300104'
        self.start = '2017-01-03'
        self.end = '2017-06-07'
        self.year = 2017
        self.quarter = 4
    #
    # def test_get_hist_data(self):
    #     self.set_data()
    #     print(fd.get_hist_data(self.code, self.start, self.end))
    #
    # def test_get_tick_data(self):
    #     self.set_data()
    #     print(fd.get_tick_data(self.code, self.end))
    #
    # def test_get_today_all(self):
    #     print(fd.get_today_all())
    #
    # def test_get_realtime_quotesa(self):
    #     self.set_data()
    #     print(fd.get_realtime_quotes(self.code))
    #
    # def test_get_h_data(self):
    #     self.set_data()
    #     print(fd.get_h_data(self.code, self.start, self.end))
    #
    # def test_get_today_ticks(self):
    #     self.set_data()
    #     print(fd.get_today_ticks(self.code))

    def test_get_k_data(self):
        self.set_data()
        print(fd.get_k_data(self.code, self.start, self.end))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()