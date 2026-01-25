import asyncio
import sys
from enum import Enum
from typing import Dict
from pydantic import BaseModel
import pytest

# No Pydantic version:

# # --- Global State (In a real app, this could be passed as an argument) ---
# DEVICE_STATES = {}
# EVENT_QUEUE = asyncio.Queue()

# # --- Logic Functions ---

# def determine_status(temperature, battery_level):
#     """Pure logic function using primitive types."""
#     if temperature > 80.0:
#         return "ERROR"
#     elif battery_level < 0.1:
#         return "OFFLINE"
#     return "ONLINE"

# async def process_event(event):
#     """Updates the global state based on the event dictionary."""
#     device_id = event["device_id"]
#     new_status = determine_status(event["temperature"], event["battery_level"])
    
#     # Update global state
#     DEVICE_STATES[device_id] = new_status
#     print(f"  [Logic] {device_id} is now {new_status}")

# async def worker():
#     """The consumer loop."""
#     print("🚀 Worker started...")
#     while True:
#         # get() pops the dict from the queue
#         event = await EVENT_QUEUE.get()
        
#         await process_event(event)
        
#         # Mark as done so queue.join() works
#         EVENT_QUEUE.task_done()

# ==========================================
# Part 1: Implementation
# ==========================================

class DeviceStatus(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    ERROR = "ERROR"

class SensorEvent(BaseModel):
    device_id: str
    temperature: float
    battery_level: float

class ControlPlane:
    def __init__(self):
        # In-memory state storage (simulating Redis)
        self.device_states: Dict[str, DeviceStatus] = {}
        # Async queue for buffering high-throughput events
        self.queue: asyncio.Queue[SensorEvent] = asyncio.Queue()
        self.running = False

    async def ingest_event(self, event: SensorEvent):
        """Public API: Non-blocking ingestion point."""
        await self.queue.put(event)

    async def process_event(self, event: SensorEvent) -> DeviceStatus:
        """Core Business Logic: Pure function style state determination."""
        # 1. Determine target state based on rules
        if event.temperature > 80.0:
            new_status = DeviceStatus.ERROR
        elif event.battery_level < 0.1:
            new_status = DeviceStatus.OFFLINE
        else:
            new_status = DeviceStatus.ONLINE

        # 2. State transition & Side effects (e.g., logging/alerting)
        current_status = self.device_states.get(event.device_id)
        
        if current_status != new_status:
            # print(f"State Change [{event.device_id}]: {current_status} -> {new_status}")
            self.device_states[event.device_id] = new_status
            
        return new_status

    async def start_worker(self):
        """Background Consumer Loop."""
        self.running = True
        while self.running:
            try:
                # wait_for allows us to periodically check self.running or handle timeouts
                event = await asyncio.wait_for(self.queue.get(), timeout=0.1)
                await self.process_event(event)
                self.queue.task_done()
            except asyncio.TimeoutError:
                continue

# ==========================================
# Part 2: Tests
# ==========================================

@pytest.mark.asyncio
async def test_normal_transition():
    cp = ControlPlane()
    event = SensorEvent(device_id="drone_1", temperature=50.0, battery_level=0.9)
    
    status = await cp.process_event(event)
    
    assert status == DeviceStatus.ONLINE
    assert cp.device_states["drone_1"] == DeviceStatus.ONLINE

@pytest.mark.asyncio
async def test_overheating_logic():
    cp = ControlPlane()
    # Simulate overheating
    event = SensorEvent(device_id="drone_1", temperature=95.0, battery_level=0.9)
    
    status = await cp.process_event(event)
    
    assert status == DeviceStatus.ERROR
    assert cp.device_states["drone_1"] == DeviceStatus.ERROR

@pytest.mark.asyncio
async def test_worker_processing():
    """Integration Test: Ensures the queue and worker loop function correctly."""
    cp = ControlPlane()
    
    # Start worker in background task
    worker_task = asyncio.create_task(cp.start_worker())
    
    # Send event via public API
    await cp.ingest_event(SensorEvent(device_id="drone_2", temperature=20.0, battery_level=0.05))
    
    # Yield control to allow worker to process
    await asyncio.sleep(0.2)
    
    # Verify side effect happened
    assert cp.device_states["drone_2"] == DeviceStatus.OFFLINE
    
    # Teardown
    cp.running = False
    await worker_task

if __name__ == "__main__":
    # Allows running this file directly: `python control_plane.py`
    sys.exit(pytest.main([__file__]))