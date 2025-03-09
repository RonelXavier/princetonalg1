
class QuickUnion:
    def __init__(self, n):
        self.id = list(range(0,n+1))
    def root(self,i):
        # chaser to chase parent pointers until root is reached
        while i != self.id[i]:
            i = self.id[i]
        return i
    def find(self,q,p):
        return self.root(p) == self.root(q)

    def union(self,q,p):
        # Replace components containing two objects with their union.
        self.id[self.root(p)] = self.root(q)

        

myuf = QuickUnion(10)
myuf.union(3,7)
myuf.union(7,5)
print(myuf.find(3,7))
print(myuf.find(5,3))
print(myuf.find(7,7))
print(myuf.id)