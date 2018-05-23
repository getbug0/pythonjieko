import unittest
import HTMLTestRunner_cn
import os
# case_a = 'D:\\pythonjieko\\day06'

case_a = os.path.dirname(os.path.realpath(__file__))
dec = unittest.defaultTestLoader.discover(start_dir=case_a,
                                          pattern="test*.py",
                                          top_level_dir=None)
# re = 'D:\\pythonjieko\\day06\\pr\\cs.html'
re = os.path.join(case_a,"report",'cs.html')
f = open(re,'wb')
r = HTMLTestRunner_cn.HTMLTestRunner(stream=f,
                                     title="测试用例标题",
                                     description='详情',
                                     retry=1, #失败的用例重跑一次
                                     verbosity=2)#用例的注释
r.run(dec)
f.close()
# #当前真实路径
# curPath=os.path.realpath(__file__)
# print(curPath)
# #当前文件的目录路径
# filepath = os.path.dirname(curPath)
# print(filepath)
# reportPath = os.path.join(filepath,'pr')
# print(reportPath)
#
# cs_html = os.path.join(filepath,'pr','cs.html')
#
# # cs_html = os.path.join(reportPath,'cs.html')
# print(cs_html)