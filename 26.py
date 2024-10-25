import heapq

# Хаффман модны зангилааны ангилал
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Heap-д ашиглагдах зориулалтаар харьцуулалтын операторыг тодорхойлно
    def __lt__(self, other):
        return self.freq < other.freq

# Хаффман код үүсгэх функц
def huffman_code(frequencies):
    # Heap үүсгэх
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Модны бүтэц үүсгэх
    while len(heap) > 1:
        # Хамгийн бага хоёр элементийг авна
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # Тэдгээрийг нэгтгэн шинэ зангилаа үүсгэнэ
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        # Шинэ зангилааг heap-д буцаан нэмнэ
        heapq.heappush(heap, merged)

    # Үүссэн модны үндэсийг авна
    root = heap[0]

    # Тэмдэгтүүдийн кодыг хадгалах dictionary үүсгэх
    huffman_codes = {}

    # Кодыг модноос гаргаж авах функц
    def generate_codes(node, current_code):
        if node is None:
            return

        # Тэмдэгт бүхий зангилаа бол кодыг хадгална
        if node.char is not None:
            huffman_codes[node.char] = current_code
            return

        # Зүүн мөчрийг 0 гэж тэмдэглэж гарна
        generate_codes(node.left, current_code + "0")
        # Баруун мөчрийг 1 гэж тэмдэглэж гарна
        generate_codes(node.right, current_code + "1")

    # Модноос кодыг гаргаж авахыг эхлүүлнэ
    generate_codes(root, "")

    return huffman_codes

# Жишээ өгөгдөл
frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}

# Хаффман кодыг үүсгэх
codes = huffman_code(frequencies)

# Үр дүнг хэвлэх
print("Тэмдэгтүүдийн Хаффман код:")
for char, code in codes.items():
    print(f"{char}: {code}")
