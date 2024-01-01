from __future__ import annotations

import logging
from collections.abc import Callable
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


def enable_mail_logging(
    func: Callable[[RealMailer, Mail], None]
) -> Callable[[RealMailer, Mail], None]:
    # Pythonのdecoratorという文法でもできることを示すドラフト実装
    # TODO mypyに怒られたのでRealMailer型にしたが、これでいい？ もしかしてジェネリック型の出番？
    # TODO もしproductionに持っていくならloggerの生成・設定を一度だけにしたい
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    def wrapper(mailer: RealMailer, mail: Mail) -> None:
        logger.info(f"Before send {mail.address}")
        func(mailer, mail)
        logger.info(f"After send {mail.address}")

    return wrapper


class RealMailer:
    @enable_mail_logging
    def send(self, mail: Mail) -> None:
        print("メール送信")


if __name__ == "__main__":
    worker = JobWorker(RealMailer())
    worker.process()
