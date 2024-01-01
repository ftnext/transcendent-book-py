from typing import Protocol


class Mail:
    ...


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


if __name__ == "__main__":
    worker = JobWorker(RealMailer())
    worker.process()
