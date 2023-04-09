class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookie_count = 0

    def __str__(self):
        return "🍪" * self._cookie_count

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        if self._cookie_count + n > self._capacity:
            raise ValueError("Capacity exceeded")
        self._cookie_count += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        if self._cookie_count - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._cookie_count -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookie_count


Jar()

