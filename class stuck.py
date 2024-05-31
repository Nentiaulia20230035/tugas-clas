class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Laci sudah kosong"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Laci kosong"

# Contoh penggunaan:
stack = Stack()
stack.push("File1")
stack.push("File2")
print("Isi laci:", stack.items)
print("Berkas yang diambil:", stack.pop())
print("Isi laci setelah diambil:", stack.items)