import unittest

from tools.HTMLTestReportCN import HTMLTestRunner
# 定义测试套件
suite=unittest.defaultTestLoader.discover("./scripts")

# 获取报告储存文件流  并  实例化HtmlTestrunner  调用run
with open("./report/report.html","wb",) as f:
    HTMLTestRunner(stream=f).run(suite)