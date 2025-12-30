#!/usr/bin/env python3
"""
Legacy monolithic fire detection system for Hellenic Coast Sentinel.
Processes CCTV and IR camera feeds to detect fire.
This is a simplified placeholder for the legacy system.
"""

import time
import random
import logging
import sys

class LegacyMonitor:
    """Monolithic monitor that handles camera feeds and fire detection."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.camera_sources = []
        self.fire_detected = False
        self.last_alert_time = None
        
    def add_camera_source(self, source_type, source_id):
        """Add a camera source (CCTV or IR)."""
        self.camera_sources.append({
            'type': source_type,
            'id': source_id,
            'active': True
        })
        self.logger.info(f"Added {source_type} camera {source_id}")
    
    def process_camera_feeds(self):
        """Simulate processing camera feeds for fire detection."""
        for camera in self.camera_sources:
            if not camera['active']:
                continue
            # Simulate fire detection logic
            temperature = random.uniform(20.0, 100.0)  # Simulated temperature reading
            smoke_density = random.uniform(0.0, 1.0)   # Simulated smoke density
            
            if temperature > 80.0 and smoke_density > 0.7:
                self.fire_detected = True
                self.last_alert_time = time.time()
                self.logger.warning(f"Fire detected by {camera['type']} camera {camera['id']}!")
                self.send_alert(camera)
                break
    
    def send_alert(self, camera):
        """Send alert to local authorities (placeholder)."""
        alert_msg = (f"ALERT: Fire detected at archaeological site. "
                     f"Source: {camera['type']} camera {camera['id']}. "
                     f"Time: {time.ctime(self.last_alert_time)}")
        print(alert_msg)
        # In real system, this would send SMS, email, etc.
    
    def run(self, interval_seconds=5):
        """Main loop."""
        self.logger.info("Starting legacy fire monitor...")
        try:
            while True:
                self.process_camera_feeds()
                if self.fire_detected:
                    self.logger.error("Fire alert active. System paused.")
                    break
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            self.logger.info("Monitor stopped by user.")

def main():
    logging.basicConfig(level=logging.INFO)
    monitor = LegacyMonitor()
    # Add some dummy camera sources
    monitor.add_camera_source('CCTV', 'cam1')
    monitor.add_camera_source('IR', 'ir1')
    monitor.add_camera_source('CCTV', 'cam2')
    monitor.run()

if __name__ == '__main__':
    main()