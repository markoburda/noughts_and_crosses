from Trees_easy.linked_binary_tree import LinkedBinaryTree

class GameTree(LinkedBinaryTree):
    def __init__(self, root):
        super().__init__(root)

    def add(self, move):
        if self.get_root_val() is None:
            self.set_root_val(move)
        else:
            if self.left_child is None:
                self.add(move)
            else:
                pass