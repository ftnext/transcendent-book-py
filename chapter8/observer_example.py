import json
import logging
from collections import defaultdict
from collections.abc import Callable, Mapping
from typing import Any, Protocol

ObserverType = Callable[[Any], None]


class ObservableInterface(Protocol):
    def add_observer(self, event_key: str, observer: ObserverType) -> None:
        ...


class NotifiableTrait:
    def __init__(self) -> None:
        self.observers: Mapping[str, list[ObserverType]] = defaultdict(list)

    def add_observer(self, event_key: str, observer: ObserverType) -> None:
        self.observers[event_key].append(observer)

    def notify(self, event_key: str, data: Any) -> None:
        event_observers = self.observers[event_key]
        for observer in event_observers:
            observer(data)


class DataStore(NotifiableTrait):  # ObservableInterfaceを実装している
    EVENT_SAVE = "save"
    EVENT_LOAD = "load"

    def save(self, data: Any) -> None:
        print("データを保存")

        self.notify(self.EVENT_SAVE, data)

    def load(self) -> Any:
        print("データ読み込み")
        data = {"dummy_data": 108}

        self.notify(self.EVENT_LOAD, data)
        return data


class LoggerInterface(Protocol):
    def info(self, message: str) -> None:
        ...


class LoggingObserver:
    def __init__(self, logger: LoggerInterface) -> None:
        self.logger = logger

    def watch(self, target: ObservableInterface, event_key: str) -> None:
        def func(data):
            self.logger.info(f"{event_key}.{json.dumps(data)}")

        target.add_observer(event_key, func)


class StdlibLogger:
    def __init__(self) -> None:
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        self.logger = logger

    def info(self, message: str) -> None:
        self.logger.info(message)


if __name__ == "__main__":
    data_store = DataStore()

    observer = LoggingObserver(StdlibLogger())
    observer.watch(data_store, DataStore.EVENT_SAVE)
    observer.watch(data_store, DataStore.EVENT_LOAD)

    data = data_store.load()
    data["foo"] = "bar"
    data_store.save(data)
