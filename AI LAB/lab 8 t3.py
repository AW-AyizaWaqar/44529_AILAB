class AutomaticDoor:
    def __init__(self):
        self.is_night = False
        self.authorized_persons = {"Alice", "Bob"}  # Example authorized persons

    def detect_person(self, person=None):
        if self.is_night and person not in self.authorized_persons:
            return "Door stays closed (Security Mode: Night)"
        elif person or not self.is_night:
            return "Door opens"
        else:
            return "Door stays closed"

# Example usage
door = AutomaticDoor()

# During the day
print(door.detect_person("Alice"))  # Door opens
print(door.detect_person())  # Door opens

# At night with unauthorized person
door.is_night = True
print(door.detect_person("Charlie"))  # Door stays closed

# At night with an authorized person
print(door.detect_person("Bob"))  # Door opens
