import asyncio
import sys
import time
from dataclasses import dataclass
from typing import List, Optional
import pytest

# ==========================================
# Part 1: Implementation
# ==========================================

@dataclass
class Agent:
    id: str
    is_busy: bool = False

@dataclass
class Task:
    id: str
    duration: float

class Scheduler:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
        # Async Event acts as a signal for resource availability
        self.resource_available = asyncio.Event()
        # Initially, resources are available
        self.resource_available.set()

    def _get_free_agent(self) -> Optional[Agent]:
        for agent in self.agents:
            if not agent.is_busy:
                return agent
        return None

    async def assign_task(self, task: Task) -> str:
        """
        Smart blocking:
        Waits for an agent to become available without busy-waiting.
        """
        while True:
            agent = self._get_free_agent()
            if agent:
                # Acquire Lock/Resource
                agent.is_busy = True
                
                # If no more agents are free, clear the signal
                if not self._get_free_agent():
                    self.resource_available.clear()
                
                try:
                    # Simulate Task Execution (IO Bound)
                    await asyncio.sleep(task.duration)
                    return f"Task {task.id} completed by {agent.id}"
                finally:
                    # Release Lock/Resource
                    agent.is_busy = False
                    # Signal that a resource is now free
                    self.resource_available.set()
            else:
                # Efficiently wait for signal
                await self.resource_available.wait()

# ==========================================
# Part 2: Tests
# ==========================================

@pytest.mark.asyncio
async def test_basic_assignment():
    agents = [Agent(id="A1")]
    scheduler = Scheduler(agents)
    task = Task(id="T1", duration=0.01)
    
    result = await scheduler.assign_task(task)
    assert "completed by A1" in result

@pytest.mark.asyncio
async def test_concurrency_blocking():
    """
    Critical Test:
    With 1 agent and 2 tasks, the total time must be additive (Sequential).
    This proves the second task waited for the first.
    """
    agents = [Agent(id="A1")]
    scheduler = Scheduler(agents)
    
    t1 = Task(id="1", duration=0.1)
    t2 = Task(id="2", duration=0.1)
    
    start_time = time.time()
    
    # Run both "concurrently"
    results = await asyncio.gather(
        scheduler.assign_task(t1),
        scheduler.assign_task(t2)
    )
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Should be approx 0.2s (0.1 + 0.1), NOT 0.1s
    assert total_time >= 0.2
    assert not agents[0].is_busy

@pytest.mark.asyncio
async def test_parallel_execution():
    """
    With 2 agents and 2 tasks, the total time should be max(t1, t2) (Parallel).
    """
    agents = [Agent(id="A1"), Agent(id="A2")]
    scheduler = Scheduler(agents)
    
    t1 = Task(id="1", duration=0.1)
    t2 = Task(id="2", duration=0.1)
    
    start_time = time.time()
    await asyncio.gather(scheduler.assign_task(t1), scheduler.assign_task(t2))
    total_time = time.time() - start_time
    
    # Should be approx 0.1s, definitely less than 0.2s
    assert total_time < 0.15

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))