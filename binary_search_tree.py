from typing import Optional


class BSTNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BST:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = BSTNode(value)
            return

        self._insert(self.root, value)

    def _insert(self, root: BSTNode, value: int) -> None:
        if root.value > value:
            if not root.left:
                root.left = BSTNode(value)
                return
            self._insert(root.left, value)

        else:
            if not root.right:
                root.right = BSTNode(value)
                return
            self._insert(root.right, value)

    def traverse_preorder(self) -> list[int]:
        values = []
        self._traverse_preorder(self.root, values)

        return values

    def _traverse_preorder(self, root: Optional[BSTNode], values: list[int]) -> None:
        if not root:
            return

        values.append(root.value)
        self._traverse_preorder(root.left, values)
        self._traverse_preorder(root.right, values)

    def traverse_inorder(self) -> list[int]:
        values = []
        self._traverse_inorder(self.root, values)

        return values

    def _traverse_inorder(self, root: Optional[BSTNode], values: list[int]) -> None:
        if not root:
            return

        self._traverse_inorder(root.left, values)
        values.append(root.value)
        self._traverse_inorder(root.right, values)

    def traverse_postorder(self) -> list[int]:
        values = []
        self._traverse_postorder(self.root, values)

        return values

    def _traverse_postorder(self, root: Optional[BSTNode], values: list[int]) -> None:
        if not root:
            return

        self._traverse_postorder(root.left, values)
        self._traverse_postorder(root.right, values)
        values.append(root.value)

    def search(self, value: int) -> bool:
        return self._search(self.root, value)

    def _search(self, root: Optional[BSTNode], target: int) -> bool:
        if not root:
            return False

        if root.value > target:
            return self._search(root.left, target)

        if root.value < target:
            return self._search(root.right, target)

        return True


if __name__ == "__main__":
    import unittest

    class TestBST(unittest.TestCase):
        def setUp(self) -> None:
            self.bst = BST()
            values = [40, 30, 50, 25, 35, 45, 60]
            for value in values:
                self.bst.insert(value)

        def test_traverse_preorder(self):
            expected = [40, 30, 25, 35, 50, 45, 60]
            self.assertEqual(self.bst.traverse_preorder(), expected)

        def test_traverse_inorder(self):
            expected = [25, 30, 35, 40, 45, 50, 60]
            self.assertEqual(self.bst.traverse_inorder(), expected)

        def test_traverse_postorder(self):
            expected = [25, 35, 30, 45, 60, 50, 40]
            self.assertEqual(self.bst.traverse_postorder(), expected)

        def test_search(self):
            self.assertTrue(self.bst.search(40))
            self.assertTrue(self.bst.search(30))
            self.assertFalse(self.bst.search(100))
            self.assertFalse(self.bst.search(10))

    unittest.main()
