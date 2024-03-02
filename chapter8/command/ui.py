from common import CommandInterface


class SelectionItem:
    def __init__(self, label: str, command: CommandInterface) -> None:
        self.label = label
        self.command = command


class SelectionUI:
    def __init__(self) -> None:
        self.selection_items: list[SelectionItem] = []

    def register_command(self, label: str, command: CommandInterface) -> None:
        self.selection_items.append(SelectionItem(label, command))

    def help(self) -> str:
        indexed_items: list[str] = []
        for i, item in enumerate(self.selection_items, start=1):
            indexed_items.append(f"{i}: {item.label}")
        return "\n".join(indexed_items)

    def select(self, number: int) -> None:
        command = self.selection_items[number - 1].command
        command.invoke()
