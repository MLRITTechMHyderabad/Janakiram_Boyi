import json
import logging
from submarine_authorization import LaunchAuthorizationSystem

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Warhead:
    def __init__(self, warhead_id, type, yield_kt):
        self.warhead_id = warhead_id
        self.type = type
        self.yield_kt = yield_kt

    def get_info(self):
        return f"Warhead {self.warhead_id}: Type {self.type}, Yield {self.yield_kt}kt"

class Submarine:
    def __init__(self, name, warhead_data):
        self.name = name
        self.warheads = [Warhead(**w) for w in warhead_data]
        self.failed_attempts = 0

    def authorize_launch(self, auth_code):
        logging.info(f"Authorizing launch for {self.name}...")

        if LaunchAuthorizationSystem.validate_code(auth_code):
            logging.info(f"Launch authorized for {self.name}. Preparing to launch SLBM...")
            if self.warheads:
                warhead = self.warheads[0]
                logging.info(f"Missile launched carrying {warhead.get_info()}")
            else:
                logging.warning("No warheads available for launch.")
            self.failed_attempts = 0
        else:
            self.failed_attempts += 1
            logging.error("Launch Authorization Failed! Access Denied.")
            if self.failed_attempts >= 3:
                logging.critical("SECURITY BREACH! Initiating self-destruct protocol...")

# Simulated warhead data in JSON format
warhead_json = '''
[
    {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
    {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]
'''

warhead_data = json.loads(warhead_json)
submarine = Submarine("USS Trident", warhead_data)

# Test with invalid codes
submarine.authorize_launch("INVALID-123")
submarine.authorize_launch("WRONG-CODE-999")
submarine.authorize_launch("FAIL-CODE-000")

# Test with a valid code
submarine.authorize_launch("AUTH-XYZ123-4567-SECURE")
