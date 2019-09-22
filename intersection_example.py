from comsys import component

comp1 = component.fromFile("Nodes1.cm")
comp2 = component.fromFile("Nodes2.cm")

intersection = comp1.intersection(comp2)
intersection.name = "intersection_comp"   #Change the name
                            #(defualt name will be intersection)
print(intersection.collector)
intersection.writeComponent("intersection_comp.cm")