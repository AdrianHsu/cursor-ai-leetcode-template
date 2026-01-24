import sys
import time
from collections import deque
from typing import Dict, Callable
import pytest

# ==========================================
# Part 1: Implementation
# ==========================================

class TelemetryStore:
    def __init__(self, window_size: int = 100, clock_fn: Callable[[], float] = time.time):
        """
        Dependency Injection Pattern:
        Injecting `clock_fn` allows us to test time-dependent logic deterministically.
        """
        self._data = deque(maxlen=window_size)
        self.clock = clock_fn
    
    def add_reading(self, value: float):
        self._data.append((self.clock(), value))
    
    def get_average(self, seconds_lookback: int) -> Dict[str, float]:
        """Calculates moving average for the past X seconds."""
        now = self.clock()
        cutoff = now - seconds_lookback
        
        relevant_values = []
        
        # Optimization: Iterate backwards because data is time-sorted.
        # Break early once we hit old data.
        for ts, val in reversed(self._data):
            if ts < cutoff:
                break
            relevant_values.append(val)
            
        count = len(relevant_values)
        if count == 0:
            return {"average": 0.0, "count": 0}
            
        return {
            "average": sum(relevant_values) / count,
            "count": count
        }

# ==========================================
# Part 2: Tests
# ==========================================

# Mock Clock for deterministic testing
class MockClock:
    def __init__(self):
        self.current_time = 1000.0
    def __call__(self):
        return self.current_time
    def advance(self, seconds):
        self.current_time += seconds

def test_sliding_window_logic():
    clock = MockClock()
    store = TelemetryStore(window_size=10, clock_fn=clock)
    
    # T=1000: Add 10
    store.add_reading(10.0)
    
    # T=1030: Add 20
    clock.advance(30)
    store.add_reading(20.0)
    
    # T=1060: Add 30
    clock.advance(30) 
    store.add_reading(30.0)
    
    # Now is 1060. Lookback 40s -> Cutoff is 1020.
    # Included: 30.0 (at 1060), 20.0 (at 1030)
    # Excluded: 10.0 (at 1000)
    stats = store.get_average(seconds_lookback=40)
    
    assert stats["count"] == 2
    assert stats["average"] == 25.0

def test_empty_store():
    store = TelemetryStore()
    stats = store.get_average(60)
    assert stats["average"] == 0.0
    assert stats["count"] == 0

def test_deque_overflow():
    """Ensure memory safety by respecting window_size."""
    store = TelemetryStore(window_size=3)
    for i in range(5):
        store.add_reading(i)
    
    # Should only keep the last 3: [2, 3, 4]
    assert len(store._data) == 3
    # Verify the oldest value is 2
    assert store._data[0][1] == 2

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))