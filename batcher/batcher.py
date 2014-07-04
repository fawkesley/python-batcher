#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals

import logging

from contextlib import contextmanager


logger = logging.getLogger('paulfurley.batcher')


__all__ = ['batcher']


@contextmanager
def batcher(callback, batch_size=2000):
    """
    Collect up items and send all at once to ``callable`` in a single batch.
    ```
    def process_items(items):
        pass
    with batcher(process_item, batch_size=2000) as b:
        for i in range(10):
            b.push(i)
    ```
    """
    processor = BatchProcessor(callback, batch_size)
    try:
        yield processor
    finally:
        processor.flush()


class BatchProcessor(object):
    """
    You can push items here and they'll be stored in a queue. When batch_size
    items have been pushed, the given callback is called with the list of
    items and the queue is cleared.

    Note: You must call flush() to process the final items: this is not done
    automatically (yet)
    """
    def __init__(self, callback, batch_size):
        self.queue = []
        self.callback = callback
        self.batch_size = batch_size

    def push(self, row):
        self.queue.append(row)
        if len(self.queue) >= self.batch_size:
            self.flush()

    def flush(self):
        if not len(self.queue):
            return
        logger.debug("Flushing batch of {} items".format(len(self.queue)))
        self.callback(self.queue)
        self.queue = []
