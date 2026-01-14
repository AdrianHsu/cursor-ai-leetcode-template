import time
from threading import Lock

class HitCounter:
    def __init__(self):
        self.window_size = 300
        self.circular_buffer = [[0, 0] for _ in range(self.window_size)]
        self.lock = Lock()

    def hit(self, ts: int) -> None:
        mod = ts % self.window_size
        with self.lock:
            if self.circular_buffer[mod][0] == ts:
                self.circular_buffer[mod][1] += 1
            else:
                self.circular_buffer[mod] = [ts, 1]

    def getHits(self, ts: int) -> int:
        prevTime = ts - self.window_size
        total = 0
        with self.lock:
            for t1, v in self.circular_buffer:
                if t1 > prevTime:
                    total += v
        return total

import threading
import time
import unittest

class TestHitCounter(unittest.TestCase):
    def test_basic_hits(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.getHits(4), 3)
        
    def test_window_expiry(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        self.assertEqual(counter.getHits(301), 1) 
        self.assertEqual(counter.getHits(302), 0)

    def test_concurrency(self):
        counter = HitCounter()
        num_threads = 10
        hits_per_thread = 1000
        current_ts = 100

        def worker():
            for _ in range(hits_per_thread):
                counter.hit(current_ts)

        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=worker)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        expected = num_threads * hits_per_thread
        self.assertEqual(counter.getHits(current_ts), expected)
        print(f"\nConcurrency Test Passed: Expected {expected}, Got {counter.getHits(current_ts)}")

if __name__ == '__main__':
    unittest.main()