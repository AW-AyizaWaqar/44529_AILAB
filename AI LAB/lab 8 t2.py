class TrafficLightAgent:
    def __init__(self):
        self.actions = {
            "red": "Stop",
            "yellow": "Slow down",
            "green": "Move"
        }

    def react(self, light_color):
        return self.actions.get(light_color.lower(), "Invalid light color")


agent = TrafficLightAgent()
traffic_lights = ["red", "yellow", "green"]

for light in traffic_lights:
    print(f"Traffic Light: {light.capitalize()} → Action: {agent.react(light)}")
