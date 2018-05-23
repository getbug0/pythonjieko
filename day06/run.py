import unittest
import HTMLTestRunner_cn

case_a = 'D:\\pythonjieko\\day06'
dec = unittest.defaultTestLoader.discover(start_dir=case_a,
                                          pattern="test*.py",
                                          top_level_dir=None)
re = 'D:\\pythonjieko\\day06\\pr\\cs.html'
f = open(re,'wb')
r = HTMLTestRunner_cn.HTMLTestRunner(stream=f,
                                     title="测试用例标题",
                                     description='详情',
                                     retry=1,
                                     verbosity=2)
r.run(dec)
