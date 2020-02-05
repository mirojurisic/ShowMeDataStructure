import sys
from collections import deque
import copy


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<>", level))
                continue
            visit_order.append((node, level))
            if node.left:
                q.enq((node.left, level + 1))
            else:
                q.enq((None, level + 1))

            if node.right:
                q.enq((node.right, level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.code = None

    def __str__(self):
        return " " + self.char + " " + str(self.freq) + " " + str(self.code)


def merge_nodes(n1, n2):
    above = Node("PP", n1.freq + n2.freq)
    above.left = n1
    above.right = n2
    return above


def build_nodes(data):
    nodes_list = []
    for d in data.items():
        nodes_list.append(Node(d[0], d[1]))
    return nodes_list


def get_frequency(data):
    frequency = {}
    for c in data:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    return frequency


def building_tree(data):
    while len(data) > 1:
        n = merge_nodes(data[0], data[1])
        data.pop(0)
        data.pop(0)
        data.append(n)
        data = sorted(data, key=lambda x: x.freq)
    return data[0]


def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    return False


def building_table(tree):
    q = Queue()
    code = ""
    visit_order = {}
    node = tree.root
    node.code = code
    q.enq(node)
    while len(q) > 0:
        node = q.deq()
        if node is None:
            continue
        if node.right is None and node.right is None:
            visit_order[node.char] = node.code
        if node.left:
            if len(node.code) > 0:
                loc_left = copy.deepcopy(node.code)
                loc_left += "1"
            else:
                loc_left = "1"
            node.left.code = loc_left
            q.enq(node.left)
        if node.right:
            if len(node.code) > 0:
                loc_right = copy.deepcopy(node.code)
                loc_right += "0"
            else:
                loc_right = "0"
            node.right.code = loc_right
            q.enq(node.right)
    return visit_order


def encode(data, table):
    # encode_data = ""
    encode_data = []
    for d in data:
        encode_data.append(table[d])
    return encode_data


def huffman_encoding(data):
    frequency = get_frequency(data)
    frequency = build_nodes(frequency)
    frequency = sorted(frequency, key=lambda x: x.freq)
    tree = Tree()
    tree.root = building_tree(frequency)
    table = building_table(tree)
    encode_data = encode(data, table)
    return encode_data, table


def huffman_decoding(table, data):
    original = ""
    for g in data:
        original += table[g]
    return original


def swap_key_value(param):
    swapped = {}
    keys = param.keys()
    for k in keys:
        swapped[param[k]] = k
    return swapped


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "We are the champions of the world and the space and planet earth"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, coding_table = huffman_encoding(a_great_sentence)
    decoding_table = swap_key_value(coding_table)
    combined = ""
    for c in encoded_data:
        combined += c
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(combined, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(decoding_table, encoded_data)
    print("The decoded of the data is: " + decoded_data)
