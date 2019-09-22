from comsys import component

comp1 = component.fromFile("Nodes1.cm")
comp2 = component.fromFile("Nodes2.cm")

union = comp1.union(comp2)
union.name = "union_comp"   #Change the name
                            #(defualt name will be union)
print(union.collector)
#union.writeComponent("union_comp.cm")