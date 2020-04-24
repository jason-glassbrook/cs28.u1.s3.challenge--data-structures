class BinarySearchTree:

    ########################################
    # PROPERTIES
    ########################################

    @property
    def left(self):

        return self._left

    @left.setter
    def left(self, left):

        self._left = left
        return

    @left.deleter
    def left(self):

        self._left = None
        return

    @property
    def right(self):

        return self._right

    @right.setter
    def right(self, right):

        self._right = right
        return

    @right.deleter
    def right(self):

        self._right = None
        return

    ########################################
    # EXTERNAL
    ########################################

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

        return

    def __len__(self):

        return 1 + self._len_or(self.left) + self._len_or(self.right)

    def insert(
        self,
        new_value,
        on_eq=None,
        on_lt=None,
        on_gt=None,
        on_else=None,
    ):

        self_value = self.value
        kwargs = dict(
            on_eq=on_eq,
            on_lt=on_lt,
            on_gt=on_gt,
            on_else=on_else,
        )

        if new_value == self_value:

            if callable(on_eq):
                on_eq(new_value, self_value)

            raise Exception("DuplicateValueError")

        elif new_value < self_value:

            if callable(on_lt):
                on_eq(new_value, self_value)

            if self._has_left_BST():
                self.left.insert(new_value, **kwargs)

            else:
                self.left = BinarySearchTree(new_value, **kwargs)

        elif new_value > self_value:

            if callable(on_gt):
                on_eq(new_value, self_value)

            if self._has_right_BST():
                self.right.insert(new_value, **kwargs)

            else:
                self.right = BinarySearchTree(new_value, **kwargs)

        else:

            if callable(on_else):
                on_eq(new_value, self_value)

            raise Exception("NotComparableError")

        return

    def contains(self, target_value):

        if target_value == self.value:
            return True

        elif target_value < self.value and self._has_left_BST():
            return self.left.contains(target_value)

        elif target_value > self.value and self._has_right_BST():
            return self.right.contains(target_value)

        else:
            return False

    ########################################
    # TRAVERSAL METHODS
    ########################################

    # "pre-order, rightward"
    def apply_DFT_NLR(self, fun):

        fun(self.value)

        if self._has_left_BST():
            self.left.apply_DFT_NLR(fun)

        if self._has_right_BST():
            self.right.apply_DFT_NLR(fun)

        return

    # "pre-order, leftward"
    def apply_DFT_NRL(self, fun):

        fun(self.value)

        if self._has_right_BST():
            self.right.apply_DFT_NRL(fun)

        if self._has_left_BST():
            self.left.apply_DFT_NRL(fun)

        return

    # "in-order rightward"
    def apply_DFT_LNR(self, fun):

        if self._has_left_BST():
            self.left.apply_DFT_LNR(fun)

        fun(self.value)

        if self._has_right_BST():
            self.right.apply_DFT_LNR(fun)

        return

    # "in-order, leftward"
    def apply_DFT_RNL(self, fun):

        if self._has_right_BST():
            self.right.apply_DFT_RNL(fun)

        fun(self.value)

        if self._has_left_BST():
            self.left.apply_DFT_RNL(fun)

        return

    # "post-order, rightward"
    def apply_DFT_LRN(self, fun):

        if self._has_left_BST():
            self.left.apply_DFT_LRN(fun)

        if self._has_right_BST():
            self.right.apply_DFT_LRN(fun)

        fun(self.value)

        return

    # "post-order, leftward"
    def apply_DFT_RLN(self, fun):

        if self._has_right_BST():
            self.right.apply_DFT_RLN(fun)

        if self._has_left_BST():
            self.left.apply_DFT_RLN(fun)

        fun(self.value)

        return

    ########################################
    # INTERNAL
    ########################################

    @staticmethod
    def _len_or(thing, default=0):

        try:
            return len(thing)

        except TypeError:
            return default

    def _has_left_BST(self):

        return isinstance(self.left, BinarySearchTree)

    def _has_right_BST(self):

        return isinstance(self.right, BinarySearchTree)

    ########################################
