import unittest
from exercises.decorators import memoize, rovarsprak
from mock import Mock


class MemoizeDecoratorTest(unittest.TestCase):

    def test_memoize(self):
        dummy_fn = Mock(name='dummy_fn')
        dummy_fn.return_value = 'spam'

        wrapped = memoize(dummy_fn)

        # Första anrop ger call count == 1
        self.assertEqual(wrapped(3), 'spam')
        self.assertEqual(dummy_fn.call_count, 1)
        # Andra anrop ger inget ytterligare call - cachen användes!
        self.assertEqual(wrapped(3), 'spam')
        self.assertEqual(dummy_fn.call_count, 1)

        # Nästa anrop ger ökning av call count.
        self.assertEqual(wrapped(7), 'spam')
        self.assertEqual(dummy_fn.call_count, 2)

class RovarsprakDecoratorTest(unittest.TestCase):

    def test_rovarsprak(self):
        @rovarsprak
        def test_fun():
            return 'testord'

        self.assertEqual(test_fun(), 'totesostotorordod')
