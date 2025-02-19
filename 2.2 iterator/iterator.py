#Napisz klasę, która będzie implementować generator kolejnych n potęg liczby a.
#Użyj metod magicznych __iter__() i __next__(). Liczby n i a powinny być
#parametrami wejściowymi generatora.


class PowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.a ** self.current
        self.current += 1
        return result

gen1 = PowerGenerator(2, 5)
print(list(gen1))

gen2 = PowerGenerator(3, 4)
print(list(gen2))

gen3 = PowerGenerator(5, 3)
print(list(gen3))

def test_power_generator():
    assert list(PowerGenerator(2, 3)) == [1, 2, 4, 8]
    assert list(PowerGenerator(3, 2)) == [1, 3, 9]
    assert list(PowerGenerator(5, 0)) == [1]
    assert list(PowerGenerator(10, 1)) == [1, 10]
    print("All tests passed.")

test_power_generator()
