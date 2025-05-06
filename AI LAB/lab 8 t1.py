import random

class Environment:
    def __init__(self):
        self.rooms = {
            "A": random.randint(0, 1),
            "B": random.randint(0, 1),
            "C": random.randint(0, 1),
            "D": random.randint(0, 1),
        }

    def display_environment(self):
        print(f"Current Environment: {self.rooms}")

class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment

    def clean(self):
        for room in self.environment.rooms:
            if self.environment.rooms[room] == 1:  # If dirty
                print(f"Cleaning room {room}")
                self.environment.rooms[room] = 0  # Clean room
            else:
                print(f"Room {room} is already clean.")

# Initialize environment and agent
env = Environment()
env.display_environment()

agent = VacuumAgent(env)
agent.clean()

env.display_environment()
