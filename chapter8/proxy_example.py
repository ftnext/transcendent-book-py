import logging
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Mail:
    address: str = "DEFAULT ADDRESS"


class MailerInterface(Protocol):
    def send(self, mail: Mail) -> None:
        ...


class JobWorker:
    def __init__(self, mailer: MailerInterface) -> None:
        self.mailer = mailer

    def process(self) -> None:
        print("ジョブの処理")

        report_mail = Mail()
        self.mailer.send(report_mail)

        print("後処理")


class RealMailer:
    def send(self, mail: Mail) -> None:
        print("メール送信")


class LoggingInterface(Protocol):
    def info(self, message: str) -> None:
        ...


class LoggingMailerProxy:
    def __init__(
        self, target: MailerInterface, logger: LoggingInterface
    ) -> None:
        self.target = target
        self.logger = logger

    def send(self, mail: Mail) -> None:
        self.logger.info(f"Before send {mail.address}")
        self.target.send(mail)
        self.logger.info(f"After send {mail.address}")


class StdlibLogger:
    def __init__(self) -> None:
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        self.logger = logger

    def info(self, message: str) -> None:
        self.logger.info(message)


if __name__ == "__main__":
    worker = JobWorker(RealMailer())
    worker.process()
    print()

    other_worker = JobWorker(LoggingMailerProxy(RealMailer(), StdlibLogger()))
    other_worker.process()
