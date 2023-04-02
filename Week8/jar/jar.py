class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Cannot hold fewer than zero cookies")
        if size > self.capacity:
            raise ValueError("Too many Cookies")
        self._size = size


def main():
    jar = Jar()
    print(f"Start with an empty jar {jar}")
    jar.deposit(5)
    print(f"Now if we add five cookies {jar}")
    jar.withdraw(4)
    print(f"But if we ate four of them all we have left is {jar}")


if __name__ == "__main__":
    main()
