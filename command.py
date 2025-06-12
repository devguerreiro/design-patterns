class Light:
    def turn_on(self):
        return "Light is on!"

    def turn_off(self):
        return "Light is off!"


class Command:
    def execute(self) -> str:
        raise NotImplementedError("Must be implemented!")


class TurnLightOn(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> str:
        return self._light.turn_on()


class TurnLightOff(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> str:
        return self._light.turn_off()


class RemoteControl:
    def send_command(self, command: Command):
        return command.execute()


light = Light()
turn_light_on = TurnLightOn(light)
turn_light_off = TurnLightOff(light)

remote_control = RemoteControl()

assert remote_control.send_command(turn_light_on) == "Light is on!"
assert remote_control.send_command(turn_light_off) == "Light is off!"
