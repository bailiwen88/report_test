#coding=utf-8
'''
一个测试用例中，测试固件可以不写，但是至少有一个已test开头的函数。
unittest会自动化识别test开头的函数是测试代码，
如果你写的函数不是test开头，
unittest是不会执行这个函数里面的脚本的，这个千万要记住，所有的测试函数都要test开头，
记住是小写的哦
'''
import unittest
import time
from selenium import webdriver

class BaiduSearch(unittest.TestCase):
#继承unittest.TestCase,即相当于利用unittest创建了一个test case，这个test case可以被unittest直接识别
    def setUp(self):
        '''
        测试固件的setup()代码，主要是测试前的准备工作
        :return:
        '''
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        '''
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        '''
        self.driver.quit()

    def test_baidu_search(self):
        '''
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        :return:
        '''
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        print self.driver.title
        try:
            assert 'selenium' in self.driver.title
            print ('test pass')
        except Exception as e:
            print ('test failed',format(e))
if __name__=='__main__':
    unittest.main()
'''
添加unittest.main()是支持在cmd中，cd到这个脚本文件所在的目录后，然后python脚本名称.py执行。
如果不添加这段，在cmd中是无法执行该脚本的
'''

