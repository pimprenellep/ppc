# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

variables=dict()
variables={}
variables["x1"]=[2]
variables["x2"]=[1]
contraintes=[[("x1","x2"),[(1,2),(2,1)]]]
instance=dict()
instance={}
#instance["x2"]=2
#0: faux, 1: vérifié 2: incomplet

def checkConstraint(constraint,instance):
    var1=constraint[0][0]
    var2=constraint[0][1]
    if var1 in instance.keys() and var2 in instance.keys():
        for j in constraint[1]:
            if j[0]==instance[var1] and j[1]==instance[var2]:
                return(1)
        return(0)
    else:
        return(2)
        

print(checkConstraint(contraintes[0],instance))

def backTrack(instance,contraintes,n):
    complet=True
    for c in contraintes:
        ch=checkConstraint(c,instance)
        if ch==0:
            return(False)
        if ch==2:
            complet=False
    if complet==True:
        print(instance)
        return(True)
    varAj=""
    for x in variables.keys():
        if not(x in instance.keys()):
            varAj=x
            instance[varAj]=[]
            break
    for y in variables[varAj]:
        print(varAj,"varAj")
        print(y,"y")
        instance[varAj].append(y)
        if backTrack(instance,contraintes,n):
            return(True)
    return(False)

print(backTrack(instance,contraintes,0))

print(instance,"instance1")

print(backTrack(instance,contraintes,0))
print(instance,"instance2")
