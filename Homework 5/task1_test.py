import unittest

from task1_func import post_item
from task1_func import get_item
from task1_func import get_list
from task1_func import put_fields
from task1_func import del_item


class TestRoles(unittest.TestCase):
    def test1_post(self):
        res, role_id = post_item(base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles',
                                 data={'name': 'Hero 1', 'type': 'Supernatural', 'level': 5, 'book': 104})
        self.__class__.role_id = role_id
        self.assertEqual(str(res), '<Response [201]>')

    def test2_item(self):
        res = get_item(self.__class__.role_id, base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles')
        exp_res = {'id': self.__class__.role_id, 'name': 'Hero 1', 'type': 'Supernatural', 'level': 5, 'book': 104}
        self.assertEqual(res, exp_res)

    def test3_item_in_list(self):
        res = get_list(base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles')
        exp_res = "'id': "+str(self.__class__.role_id)+','
        self.assertIn(exp_res, str(res))

    def test4_put(self):
        res = put_fields(self.__class__.role_id, base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles',
                         data={'name': 'Hero Changed', 'level': 6})
        self.assertEqual(str(res), '<Response [200]>')

    def test5_item(self):
        res = get_item(self.__class__.role_id, base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles')
        exp_res = {'id': self.__class__.role_id, 'name': 'Hero Changed', 'type': 'Supernatural', 'level': 6,
                   'book': 104}
        self.assertEqual(res, exp_res)

    def test6_item_in_list(self):
        res = get_list(base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles')
        exp_res = {'id': self.__class__.role_id, 'name': 'Hero Changed', 'type': 'Supernatural', 'level': 6,
                   'book': 104}
        self.assertIn(exp_res, res)

    def test7_delete(self):
        res = del_item(self.__class__.role_id, base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles')
        self.assertEqual(str(res), '<Response [204]>')
        res = get_item(self.__class__.role_id, base_url='http://pulse-rest-testing.herokuapp.com', part_url='/roles')
        self.assertEqual(str(res), "{'detail': 'Not found.'}")


if __name__ == '__main__':
    unittest.main()
