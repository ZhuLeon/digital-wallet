# Leon Zhu
import os

with open("batch_payment.csv", encoding="utf-8") as batchfile:
    print(batchfile.readline())
    tempstring=batchfile.readline()
    print(tempstring)
    print(tempstring.split(", ")[1])
    print(tempstring.split(", ")[2])
    print(batchfile.readline())

    graph = dict()
    graph['A']=['B']
    graph['A']=graph['A']+['C']
    print(graph['A'])
