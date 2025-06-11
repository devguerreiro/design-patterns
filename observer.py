from typing import List


class Subscriber:
    def notify(self) -> str:
        raise NotImplementedError("Must be implemented")


class YouTubeChannel:
    def __init__(self) -> None:
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def _notify_subscribers(self):
        notifications: List[str] = []
        for subscriber in self._subscribers:
            notifications.append(subscriber.notify())
        return notifications

    def upload_video(self):
        return self._notify_subscribers()


class Account(Subscriber):
    def __init__(self, username: str) -> None:
        self._username = username

    def notify(self):
        return f"{self._username} was notified!"


channel = YouTubeChannel()

john_doe = Account("John Doe")
everyman = Account("Everyman")

channel.subscribe(john_doe)
channel.subscribe(everyman)

assert channel.upload_video() == [
    "John Doe was notified!",
    "Everyman was notified!",
]

channel.unsubscribe(everyman)

assert channel.upload_video() == ["John Doe was notified!"]
