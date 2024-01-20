from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name
        self.parent: Branch | None = None

    @abstractmethod
    def __str__(self) -> str:
        ...

    def attach(self, node: Node) -> None:
        raise NotImplementedError

    @abstractmethod
    def pprint(self, prefix: str = "") -> None:
        ...


class Branch(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.subnodes: list[Node] = []

    def __str__(self) -> str:
        return f"Branch({self.name!r})"

    def attach(self, node: Node) -> None:
        if node.parent is not None:  # 親は1つ
            raise ValueError("%s is already attached", node)

        self.subnodes.append(node)
        node.parent = self

    def pprint(self, prefix: str = "") -> None:
        """
        >>> branch = Branch("b")
        >>> leaf = Leaf("l")
        >>> branch.attach(leaf)
        >>> branch.pprint()
        Branch('b')
         Leaf('l')

        >>> parent_branch = Branch("p")
        >>> child_branch = Branch("c")
        >>> leaf1 = Leaf("l1")
        >>> leaf2 = Leaf("l2")
        >>> parent_branch.attach(child_branch)
        >>> child_branch.attach(leaf1)
        >>> parent_branch.attach(leaf2)
        >>> parent_branch.pprint()
        Branch('p')
         Branch('c')
          Leaf('l1')
         Leaf('l2')
        """
        print(f"{prefix}{self}")
        for subnode in self.subnodes:
            subnode.pprint(prefix + " ")


class Leaf(Node):
    def __str__(self) -> str:
        return f"Leaf({self.name!r})"

    def pprint(self, prefix: str = "") -> None:
        print(f"{prefix}{self}")


if __name__ == "__main__":
    root_branch = Branch("root")
    branch1 = Branch("branch1")
    branch2 = Branch("branch2")
    node1 = Leaf("node1")
    node2 = Leaf("node2")
    node3 = Leaf("node3")

    branch2.attach(node3)
    branch1.attach(branch2)
    branch1.attach(node2)
    root_branch.attach(branch1)
    root_branch.attach(node1)

    root_branch.pprint()

"""
Branch('root')
 Branch('branch1')
  Branch('branch2')
   Leaf('node3')
  Leaf('node2')
 Leaf('node1')
"""
