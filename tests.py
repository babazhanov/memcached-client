import unittest
import memcached


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        self.client = memcached.Client('localhost')
        self.client.connect()
        self.client.set('key1', 'value1')

    def tearDown(self):
        self.client.close()

    def test_set(self):
        res = self.client.set('key2', 'value2')
        self.assertTrue(res)

    def test_get(self):
        value1 = self.client.get('key1')
        self.assertTrue(value1 == 'value1')

    def test_memory_leak(self):
        client = memcached.Client('localhost')
        self.assertTrue(isinstance(client, memcached.Client))

    def test_delete(self):
        self.client.set('key3', 'value3')
        res = self.client.delete('key3')
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
