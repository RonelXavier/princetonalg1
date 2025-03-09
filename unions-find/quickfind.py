
class UF:
    def __init__(self, n):
        self.id = list(range(0,n+1))

    def find(self,q,p):
        # Check if two objects are in the same component.
        return self.id[p] == self.id[q]

    def union(self,q,p):
        # Replace components containing two objects with their union.
        pid = self.id[p]
        qid = self.id[q]
        for i in self.id:
            if self.id[i] == pid:
                self.id[i] = qid
        

myuf = UF(10)
myuf.union(3,7)
print(myuf.find(3,7))
print(myuf.find(3,9))
print(myuf.id)

