import unittest
from common import HTMLTestRunner_cn

#用例的路径
casepath="E:\pythonlizi\web_auto\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casepath,pattern=rule)
print(discover)

#报告的路径
reportpath=r"E:\pythonlizi\web_auto\report\\" + "report.html"

fp=open(reportpath,"wb")

runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="测试的标题")
runner.run(discover)

fp.close()