class component:
    def __init__(self, cname, ctype, collector):
        self.name = cname
        self.type = ctype
        self.collector = collector
    
    @classmethod
    def fromFile(cls,file):
        list1 = cls._readCompFile(file)
        return cls(list1[0], list1[1], list1[2])

    @classmethod
    def _NewComponent(cls, name, typ, collector):
        return cls(name, typ, collector)

    def _readCompFile(file):
        
        collector = []
        with open(file,'r') as source:
            for line in source:
                if "comp" in line.lower():
                    arr = line.split(",")
                    cname = arr[1]
                    ctype = arr[2]
                elif "(" in line:
                    pass
                else:
                    arr = line.split()
                    collector.extend(list(map(int,arr)))
        return [cname, ctype, collector]
    
    def union(self, comp2):
        if self.type == comp2.type:
            name = "union"
            union = list(set().union(self.collector, comp2.collector))
            return self._NewComponent(name, self.type, union)
            
        else: 
            raise TypeError("The type of collectors should be same.")
    
    def intersection(self, comp2): 
        
        if self.type == comp2.type:
            name = "intersection"
            intersection = list(set(self.collector) & set(comp2.collector))
            return self._NewComponent(name, self.type, intersection)
        else: 
            raise TypeError("The type of collectors should be same.")
    
    def writeComponent(self, file):
        
        lineElem = ["COMP", self.name, self.type, str(len(self.collector))]
        firstline = ",".join(elem for elem in lineElem)
        secondline = "(8I10)"
        with open(file, "w") as file:
            file.write("{}\n".format(firstline))
            file.write("{}\n".format(secondline))
            i = 0
            while i < len(nodes):
                a = self.collector[i:i+8]
                formatted = ' '.join(['{0: >10}'.format(word) for word in a])
                file.write("{}\n".format(formatted))
                i += 8
