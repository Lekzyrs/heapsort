class Heapsort:
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.array[left] > self.array[largest]:
            largest = left

        if right < n and self.array[right] > self.array[largest]:
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(n, largest)

    def build_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(self.size, i)

    def sort(self):
        self.build_heap()
        for i in range(self.size - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)

    def get_sorted_array(self):
        return self.array

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Исходный массив:")
    print(array)

    sorter = Heapsort(array)
    sorter.sort()

    print("\nОтсортированный массив:")
    print(sorter.get_sorted_array())
