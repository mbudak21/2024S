import array

class bitVector(): # V1
    # A bit vector list that holds binary values which represent the presence of a number in the universe
    def __init__(self, u):
        self.u = u
        self.vector = array.array('b', [0] * u)
        print("Created vector of size: ", u)

    def insert(self, x):
        self.vector[x] = 1

    def delete(self, x):
        self.vector[x] = 0

    def successor(self, x):
        for i in range(x+1, self.u):
            if self.vector[i] == 1:
                return i
        return None

a = bitVector(16)
a.insert(7)
a.insert(9)
print(a.successor(7))
