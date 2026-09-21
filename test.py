from __future__ import annotations


# ---------------------------------------------------------------------------
# Challenge 1 — Balanced Brackets
# ---------------------------------------------------------------------------

def is_balanced(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    openers = set(pairs.values())
    stack = []
    for ch in s:
        if ch in openers:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


# ---------------------------------------------------------------------------
# Challenge 2 — Two Sum via Hash Map
# ---------------------------------------------------------------------------

def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return (seen[complement], i)
        seen[x] = i
    raise ValueError("no valid pair found")


# ---------------------------------------------------------------------------
# Challenge 3 — Reverse a Linked List
# ---------------------------------------------------------------------------

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Node | None) -> Node | None:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_list_recursive(head: Node | None) -> Node | None:
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def list_to_python(head: Node | None) -> list:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def python_to_list(values: list) -> Node | None:
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


# ---------------------------------------------------------------------------
# Challenge 4 — Queue Using Two Stacks
# ---------------------------------------------------------------------------

class QueueFromStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x) -> None:
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()


# ---------------------------------------------------------------------------
# Challenge 5 — Detect a Cycle (Floyd's algorithm)
# ---------------------------------------------------------------------------

def has_cycle(head: Node | None) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def cycle_start(head: Node | None) -> Node | None:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            pointer = head
            while pointer is not slow:
                pointer = pointer.next
                slow = slow.next
            return pointer
    return None


# ---------------------------------------------------------------------------
# Challenge 6 — Min-Stack in O(1)
# ---------------------------------------------------------------------------

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x) -> None:
        self.stack.append(x)
        current_min = x if not self.min_stack else min(x, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("get_min from empty stack")
        return self.min_stack[-1]


# ---------------------------------------------------------------------------
# Challenge 7 — Implement a Dynamic Array
# ---------------------------------------------------------------------------

class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, x) -> None:
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = x
        self.size += 1

    def _resize(self, new_capacity: int) -> None:
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get(self, i: int):
        if i < 0 or i >= self.size:
            raise IndexError("index out of range")
        return self.array[i]

    def set(self, i: int, x) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("index out of range")
        self.array[i] = x

    def __len__(self) -> int:
        return self.size


# ---------------------------------------------------------------------------
# Challenge 8 — Validate a Binary Search Tree
# ---------------------------------------------------------------------------

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    def helper(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float('-inf'), float('inf'))


# ---------------------------------------------------------------------------
# Challenge 9 — First & Last Position
# ---------------------------------------------------------------------------

def search_range(nums: list[int], target: int) -> tuple[int, int]:
    def find_bound(is_first: bool) -> int:
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                if is_first:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    first = find_bound(True)
    if first == -1:
        return (-1, -1)
    last = find_bound(False)
    return (first, last)


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Challenge 1
    assert is_balanced("(a[b]{c})") is True
    assert is_balanced("([)]") is False
    assert is_balanced("((") is False
    assert is_balanced("") is True
    assert is_balanced(")") is False

    # Challenge 2
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([-3, 4, 3, 90], 0) == (0, 2)

    # Challenge 3
    assert list_to_python(reverse_list(python_to_list([1, 2, 3]))) == [3, 2, 1]
    assert reverse_list(None) is None
    assert list_to_python(reverse_list(Node(5))) == [5]
    assert list_to_python(reverse_list_recursive(python_to_list([1, 2, 3, 4]))) == [4, 3, 2, 1]

    # Challenge 4
    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    try:
        q.dequeue()
        assert False, "expected IndexError"
    except IndexError:
        pass

    # Challenge 5
    a, b, c = Node(1), Node(2), Node(3)
    a.next, b.next, c.next = b, c, a
    assert has_cycle(a) is True
    assert cycle_start(a) is a
    straight = python_to_list([1, 2, 3, 4, 5])
    assert has_cycle(straight) is False
    assert has_cycle(None) is False
    self_loop = Node(1)
    self_loop.next = self_loop
    assert has_cycle(self_loop) is True

    # Challenge 6
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    assert ms.get_min() == 2
    ms.pop()
    assert ms.get_min() == 3
    assert ms.top() == 5
    empty_ms = MinStack()
    try:
        empty_ms.pop()
        assert False, "expected IndexError"
    except IndexError:
        pass

    # Challenge 7
    da = DynamicArray()
    for v in [10, 20, 30, 40]:
        da.append(v)
    assert len(da) == 4
    assert da.get(0) == 10
    assert da.get(3) == 40
    da.set(1, 99)
    assert da.get(1) == 99
    try:
        da.get(10)
        assert False, "expected IndexError"
    except IndexError:
        pass

    # Challenge 8
    valid_bst = TreeNode(5, TreeNode(3), TreeNode(8))
    assert is_valid_bst(valid_bst) is True

    invalid_bst = TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(4), TreeNode(9)))
    assert is_valid_bst(invalid_bst) is False

    assert is_valid_bst(None) is True
    assert is_valid_bst(TreeNode(1)) is True

    # Challenge 9
    assert search_range([5, 7, 7, 8, 8, 8, 10], 8) == (3, 5)
    assert search_range([5, 7, 7, 8, 8, 8, 10], 6) == (-1, -1)
    assert search_range([1], 1) == (0, 0)

    print("All tests passed.")
