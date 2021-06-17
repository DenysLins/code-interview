class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next


def calculateNthElement(node: Node, i: int):
    current = node
    follower = node

    for i in range(i):
        if (current.next == None):
            return None
        else:
            current = current.next

    while current.next != None:
        current = current.next
        follower = follower.next

    return follower


n1 = Node(0, None)
n2 = Node(3, n1)
n3 = Node(5, n2)
n4 = Node(4, n3)
n5 = Node(1, n4)
list = n5

# list > 1 > 4 > 5 > 3 > 0


def test_get_the_0th_last_element():
    assert calculateNthElement(n5, 0) == n1


def test_get_the_1st_last_element():
    assert calculateNthElement(n5, 1) == n2


def test_get_the_1st_last_element():
    assert calculateNthElement(n5, 2) == n3


def test_get_the_2nd_last_element():
    assert calculateNthElement(n5, 3) == n4


def test_get_the_3rd_last_element():
    assert calculateNthElement(n5, 4) == n5


def test_get_the_4th_last_element():
    assert calculateNthElement(n5, 5) == None
