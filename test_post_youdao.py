import unittest

class postyoudaotsst(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        #import time
        #t=time.time()
        #ts=str(int(round(t*1000)))
        #print(ts)
        get_ts=mock.Mock(reture_value='1584841718016')
        self.assertEqual('1584841718016',get_ts())
    def test_get_salt(self):
        get_salt=mock.Mock(reture_value='15848417180161')
        self.assertEqual('15848417180161',get_salt())

    def test_get_sign(self):
        self.assertEqual('039b6c51c66ba62540119833ad93d999',get_sign())


if __name__=='__main__':
    unittest.main()

