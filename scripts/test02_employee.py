import unittest

import api

from api.api_employee import ApiEmployee

from tools.assert_common import assert_common


class TestEmpioyee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 获取ApiEmployee对象
        cls.api=ApiEmployee()


    def test01_post(self,username="ls2468",mobile="12332112345",workNumber="999000"):
        # 调用新增接口
        r=self.api.api_post_employee(username,mobile,workNumber)
        print("新增员工结果为:",r.json())
        # 提取user_id
        api.user_id=r.json().get("data").get("id")
        print("新增员工id为:",api.user_id)
        # 断言
        assert_common(self,r)

        # 查询
    def test02_get(self):
        r = self.api.api_get_employee()
        print("查询员工名称结果为：", r.json())
        # 断言
        assert_common(self, r)
        # 删除
    def test03_delete(self):
        # 调用删除接口
        r = self.api.api_delete_employee(api.user_id)
        print("删除数据结果为：", r.json())
        # 断言
        assert_common(self,r)

    def tese04_deletd(self):
        #调用删除接口
        r=self.api.api_delete_employee(api.user_id)
        print("删除数据结果为:",r.json())
        # 断言
        assert_common(self,r)
