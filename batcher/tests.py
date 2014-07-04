from mock import Mock, call
from nose.tools import assert_equal

from batcher import batcher


def test_that_batcher_correctly_batches():
    process_items = Mock(return_value=None)

    with batcher(process_items, batch_size=5) as b:
        for i in range(10):
            b.push(i)

    assert_equal(2, process_items.call_count)
    assert_equal([
        call([0, 1, 2, 3, 4]),
        call([5, 6, 7, 8, 9])],
        process_items.call_args_list)
