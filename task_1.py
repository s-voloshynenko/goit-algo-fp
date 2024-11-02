class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування злиттям
    def merge_sort(self):
        if not self.head or not self.head.next:
            return

        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)

        return self.sorted_merge(left, right)

    def get_middle(self, head):
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Об'єднання двох відсортованих однозв'язних списків в один відсортований список
def merge_sorted_lists(llist1, llist2):
    item1 = llist1.head
    item2 = llist2.head

    head_start = Node()
    tail = head_start

    while item1 and item2:
        if item1.data <= item2.data:
            tail.next = item1
            item1 = item1.next
        else:
            tail.next = item2
            item2 = item2.next
        tail = tail.next

    if item1:
        tail.next = item1
    elif item2:
        tail.next = item2

    merged_list = LinkedList()
    merged_list.head = head_start.next
    return merged_list

llist = LinkedList()
llist.insert_at_end(5)
llist.insert_at_end(20)
llist.insert_at_end(10)
llist.insert_at_end(15)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

# Реверс
print("Реверснутий список:")
llist.reverse()
llist.print_list()

# Сортування злиттям
print("Відсортований список:")
llist.merge_sort()
llist.print_list()

# Злиття двох списків
llist2 = LinkedList()
llist2.insert_at_end(23)
llist2.insert_at_end(8)
llist2.insert_at_end(13)
llist2.insert_at_end(16)
llist2.insert_at_end(30)

print("Відсортований 2й список:")
llist2.merge_sort()
llist2.print_list()

print("Результат злиття в один список:")
merge_sorted_lists(llist, llist2).print_list()
