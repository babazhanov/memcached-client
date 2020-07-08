import unittest
import memcached


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        self.con = memcached.connect()
        memcached.set('key1', 'value1')

    def tearDown(self):
        memcached.close(self.con)

    def test_set(self):
        res = memcached.set('key2', 'value2')
        self.assertTrue(res)

    def test_get(self):
        value1 = memcached.get('key1')
        self.assertTrue(value1 == 'value1')

    def test_delete(self):
        res = memcached.delete('key1')
        self.assertTrue(res)

