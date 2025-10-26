try:
    import week3_answers as week3
except ImportError:
    import week3

import unittest

class TestTimeout(Exception):
    pass


# LL Class
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def convert_array_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for item in arr[1:]:
        cur.next_node = Node(item)
        cur = cur.next_node
    return head

def convert_ll_to_array(head):
    arr = []
    cur = head
    while cur is not None:
        arr.append(cur.data)
        cur = cur.next_node
    return arr


class TestItemInLL(unittest.TestCase):
    def test_item_in_ll(self):
        head = convert_array_to_ll([1, 2, 3, 4, 5])
        self.assertTrue(week3.is_item_in_ll(head, 3))

    def test_item_not_in_ll(self):
        head = convert_array_to_ll([1, 2, 3, 4, 5])
        self.assertFalse(week3.is_item_in_ll(head, 6))

    def test_empty_ll(self):
        head = convert_array_to_ll([])
        self.assertFalse(week3.is_item_in_ll(head, 6))


class TestReverseLL(unittest.TestCase):
    def test_reverse_ll(self):
        head = convert_array_to_ll([1, 2, 3, 4, 5])
        head = week3.reverse_ll(head)
        self.assertListEqual(convert_ll_to_array(head), [5, 4, 3, 2, 1])

    def test_reverse_ll_empty(self):
        head = convert_array_to_ll([])
        head = week3.reverse_ll(head)
        self.assertListEqual(convert_ll_to_array(head), [])

    def test_reverse_ll_one(self):
        head = convert_array_to_ll([1])
        head = week3.reverse_ll(head)
        self.assertListEqual(convert_ll_to_array(head), [1])


class TestInterleaveLLs(unittest.TestCase):
    def test_interleave_lls(self):
        head1 = convert_array_to_ll([1, 2, 3])
        head2 = convert_array_to_ll([4, 5, 6])
        head = week3.interleave_lls(head1, head2)
        self.assertListEqual(convert_ll_to_array(head), [1, 4, 2, 5, 3, 6])

    def test_interleave_lls_one(self):
        head1 = convert_array_to_ll([1])
        head2 = convert_array_to_ll([2])
        head = week3.interleave_lls(head1, head2)
        self.assertListEqual(convert_ll_to_array(head), [1, 2])


class TestRemoveItem(unittest.TestCase):
    def test_remove_item(self):
        head = convert_array_to_ll([1, 2, 3, 2, 4])
        head = week3.remove_item(head, 2)
        self.assertListEqual(convert_ll_to_array(head), [1, 3, 4])


class TestRemoveIndex(unittest.TestCase):
    def test_remove_index(self):
        head = convert_array_to_ll([1, 2, 3, 2, 4])
        head = week3.remove_index(head, 2)
        self.assertListEqual(convert_ll_to_array(head), [1, 2, 2, 4])

class TestRemoveHead(unittest.TestCase):
    def test_remove_head(self):
        head = convert_array_to_ll([1, 2, 3, 2, 4])
        head = week3.remove_head(head)
        self.assertListEqual(convert_ll_to_array(head), [2, 3, 2, 4])

    def test_remove_head_size1(self):
        head = convert_array_to_ll([1])
        head = week3.remove_head(head)
        self.assertListEqual(convert_ll_to_array(head), [])

    def test_remove_head_size2(self):
        head = convert_array_to_ll([1, 2])
        head = week3.remove_head(head)
        self.assertListEqual(convert_ll_to_array(head), [2])


class TestRemoveTail(unittest.TestCase):
    def test_remove_tail(self):
        head = convert_array_to_ll([1, 2, 3, 2, 4])
        head = week3.remove_tail(head)
        self.assertListEqual(convert_ll_to_array(head), [1, 2, 3, 2])

    def test_remove_tail_size1(self):
        head = convert_array_to_ll([1])
        head = week3.remove_tail(head)
        self.assertListEqual(convert_ll_to_array(head), [])

    def test_remove_tail_size2(self):
        head = convert_array_to_ll([1, 2])
        head = week3.remove_tail(head)
        self.assertListEqual(convert_ll_to_array(head), [1])


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_dups(self):
        head = convert_array_to_ll([1, 2, 2, 3, 2, 3, 5])
        head = week3.remove_duplicates(head)
        self.assertListEqual(convert_ll_to_array(head), [1, 2, 3, 5])

    def test_remove_dups_empty(self):
        head = convert_array_to_ll([])
        head = week3.remove_duplicates(head)
        self.assertListEqual(convert_ll_to_array(head), [])

    def test_remove_dups_one(self):
        head = convert_array_to_ll([1])
        head = week3.remove_duplicates(head)
        self.assertListEqual(convert_ll_to_array(head), [1])

    def test_remove_dups_two(self):
        head = convert_array_to_ll([1, 2])
        head = week3.remove_duplicates(head)
        self.assertListEqual(convert_ll_to_array(head), [1, 2])

    def test_remove_dups_two_dups(self):
        head = convert_array_to_ll([1, 1])
        head = week3.remove_duplicates(head)
        self.assertListEqual(convert_ll_to_array(head), [1])

# Binary Tree questions will use the following definition of a Tree:
class BST(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None  # Left child, in a BST every node in the left subtree is less than the current node
        self.right = None  # Right child, in a BST every node in the right subtree is greater than or equal to the current node

def convert_bst_to_array(root):
    """
    Return array where A[1] is the root and A[i*2] is the left child of i and A[i*2+1] is the right child of i
    """
    arr = [None]
    q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            arr.append(None)
        else:
            arr.append(node.data)
            q.append(node.left)
            q.append(node.right)
    return arr


def convert_array_to_bst(arr):
    """
    Convert array to BST where A[1] is the root and A[i*2] is the left child of i and A[i*2+1] is the right child of i
    """
    if not arr:
        return None
    root = BST(arr[1])
    q = [root]
    i = 2
    while i < len(arr):
        node = q.pop(0)
        if arr[i] is not None:
            node.left = BST(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = BST(arr[i])
            q.append(node.right)
        i += 1
    return root

class TestIsTreeBST(unittest.TestCase):
    def test_is_tree_bst(self):
        root = BST(8)
        root.left = BST(4)
        root.right = BST(12)
        root.left.left = BST(3)
        root.left.right = BST(6)
        root.right.left = BST(9)
        root.right.right = BST(15)
        self.assertTrue(week3.is_tree_bst(root))

    def test_is_tree_bst_array(self):
        root = convert_array_to_bst([None, 8, 4, 12, 3, 6, 9, 15])
        self.assertTrue(week3.is_tree_bst(root))

    def test_is_tree_bst_empty(self):
        root = BST(None)
        self.assertTrue(week3.is_tree_bst(root))

    def test_is_tree_bst_one(self):
        root = BST(1)
        self.assertTrue(week3.is_tree_bst(root))

    def test_is_tree_bst_false(self):
        root = convert_array_to_bst([None, 1, 2, 3, 4, 5, 6, 7])
        root.left.data = 10
        self.assertFalse(week3.is_tree_bst(root))

class SearchBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BST(1)
        self.binary_tree.left = BST(2)
        self.binary_tree.right = BST(3)
        self.binary_tree.left.left = BST(4)
        self.binary_tree.left.right = BST(5)
        self.binary_tree.right.left = BST(6)
        self.binary_tree.right.right = BST(7)

    def test_find_in_binary_tree(self):
        self.assertTrue(week3.search_binary_tree(self.binary_tree, 5))
    def test_not_in_binary_tree(self):
        self.assertFalse(week3.search_binary_tree(self.binary_tree, 10))

    def test_find_in_binary_tree_array(self):
        root = convert_array_to_bst([None, 8, 4, 12, 3, 6, 9, 15])
        self.assertTrue(week3.search_binary_tree(root, 9))

    def test_find_in_binary_tree_one(self):
        root = BST(1)
        self.assertTrue(week3.search_binary_tree(root, 1))

    def test_find_in_binary_tree_one_false(self):
        root = BST(1)
        self.assertFalse(week3.search_binary_tree(root, 21))

def balance_tree(items, start=0, end=None):
    if not items:
        return None

    stack = []
    mid = len(items) // 2
    root = BST(items[mid])
    stack.append((root, 0, len(items)))

    while stack:
        node, start, end = stack.pop()
        mid = (start + end) // 2

        if start < mid:
            left_mid = (start + mid) // 2
            node.left = BST(items[left_mid])
            stack.append((node.left, start, mid))

        if mid + 1 < end:
            right_mid = (mid + 1 + end) // 2
            node.right = BST(items[right_mid])
            stack.append((node.right, mid + 1, end))

    return root

class TestSearchBST(unittest.TestCase):
    def test_search_bst(self):
        root = convert_array_to_bst([None, 8, 4, 12, 3, 6, 9, 15])
        self.assertTrue(week3.search_bst(root, 9))

    def test_search_bst_false(self):
        root = convert_array_to_bst([None, 8, 4, 12, 3, 6, 9, 15])
        self.assertFalse(week3.search_bst(root, 10))

    def test_search_bst_one(self):
        root = BST(1)
        self.assertTrue(week3.search_bst(root, 1))

    def test_search_bst_one_false(self):
        root = BST(1)
        self.assertFalse(week3.search_bst(root, 21))

    def test_search_bst_large(self):
        tree = balance_tree(list(range(1, 2**20 + 1)))
        self.assertTrue(week3.search_bst(tree, 500_000))
        self.assertFalse(week3.search_bst(tree, 20_000_001))

class TestInsertBST(unittest.TestCase):
    def test_insert_bst(self):
        root = convert_array_to_bst([None, 8, 4, 12, 3, 6, 9, 15])
        root = week3.insert_bst(root, 5)
        self.assertEqual(root.left.right.left.data, 5)

    def test_insert_bst_left(self):
        root = convert_array_to_bst([None, 10])
        root = week3.insert_bst(root, 5)
        self.assertEqual(root.left.data, 5)

    def test_insert_bst_right(self):
        root = convert_array_to_bst([None, 10])
        root = week3.insert_bst(root, 15)
        self.assertEqual(root.right.data, 15)

    def test_insert_into_middle(self):
        root = convert_array_to_bst([None, 8, 1, 100])
        root = week3.insert_bst(root, 7)
        self.assertEqual(root.left.right.data, 7)


class TestBSTMin(unittest.TestCase):
    def test_bst_min(self):
        root = convert_array_to_bst([None, 8, 4, 12, 3, 6, 9, 15])
        self.assertEqual(week3.bst_min(root), 3)

    def test_bst_min_unbalanced_tree(self):
        root = BST(8)
        root.right = BST(12)
        root.right.right = BST(15)
        self.assertEqual(week3.bst_min(root), 8)


class TestBSTMax(unittest.TestCase):
    def test_bst_max(self):
        root = convert_array_to_bst([None, 8, 4, 12, 3, 6, 9, 15])
        self.assertEqual(week3.bst_max(root), 15)

    def test_bst_max_unbalanced_tree(self):
        root = BST(8)
        root.left = BST(4)
        root.left.left = BST(3)
        self.assertEqual(week3.bst_max(root), 8)

class TestGetNeighbors(unittest.TestCase):
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    def test_get_neighbors(self):
        self.assertListEqual(week3.get_neighbors(self.graph, 1), [2, 3])

    def test_get_neighbors_nonexistent_node(self):
        self.assertListEqual(week3.get_neighbors(self.graph, 5), [])


class TestBFS(unittest.TestCase):
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }

    def test_bfs(self):
        self.assertListEqual(week3.bfs(self.graph, 1), [1, 2, 3, 4])

    def test_bfs_from2(self):
        self.assertListEqual(week3.bfs(self.graph, 2), [2, 1, 4, 3])

    def test_bfs_one_val(self):
        self.assertListEqual(week3.bfs({1: []}, 1), [1])

    def test_bfs_two_neighbors(self):
        self.assertListEqual(week3.bfs({1: [2], 2: [1]}, 1), [1, 2])


class TestPathExists(unittest.TestCase):
    graph = {
        1: [2],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3],
        5: [6],
        6: [5]
    }
    def test_path_exists(self):
        self.assertTrue(week3.path_exists(self.graph, 1, 4))

    def test_path_exists_false(self):
        self.assertFalse(week3.path_exists(self.graph, 1, 5))

    def test_path_exists_self(self):
        self.assertTrue(week3.path_exists(self.graph, 1, 1))

    def test_path_exists_one(self):
        self.assertTrue(week3.path_exists({1: []}, 1, 1))

    def test_path_exists_two_neighbors(self):
        self.assertTrue(week3.path_exists({1: [2], 2: [1]}, 1, 2))

class TestShortestPath(unittest.TestCase):
    graph = {
        1: [2],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3],
        5: [6],
        6: [5]
    }
    def test_shortest_path(self):
        self.assertListEqual(week3.shortest_path(self.graph, 1, 4), [1, 2, 4])

    def test_shortest_path_one_away(self):
        self.assertListEqual(week3.shortest_path(self.graph, 1, 2), [1, 2])

    def test_shortest_path_self(self):
        self.assertListEqual(week3.shortest_path(self.graph, 1, 1), [1])

    def test_no_path(self):
        self.assertListEqual(week3.shortest_path(self.graph, 1, 5), [])

    def test_path_one(self):
        self.assertListEqual(week3.shortest_path({1: []}, 1, 1), [1])

    def test_path_exists_two_neighbors(self):
        self.assertListEqual(week3.shortest_path({1: [2], 2: [1]}, 1, 2), [1, 2])

    def test_large(self):
        graph = {i: [i+1] for i in range(100000)}
        graph[99997].append(100000)
        graph[100000] = [0]
        self.assertListEqual(week3.shortest_path(graph, 0, 100000), list(range(99998)) + [100000])

if __name__ == '__main__':
    unittest.main()