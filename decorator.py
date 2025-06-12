class Action:
    def do(self) -> str:
        return "Doing some action..."


class ActionDecorator(Action):
    def __init__(self, action: Action) -> None:
        self._action = action

    def do(self):
        return self._action.do()


class JumpAction(ActionDecorator):
    def do(self):
        did = super().do()
        return f"{did} and jumping..."


class RunAction(ActionDecorator):
    def do(self):
        did = super().do()
        return f"{did} and running..."


assert Action().do() == "Doing some action..."
assert JumpAction(Action()).do() == "Doing some action... and jumping..."
assert RunAction(Action()).do() == "Doing some action... and running..."
assert (
    RunAction(JumpAction(Action())).do()
    == "Doing some action... and jumping... and running..."
)
