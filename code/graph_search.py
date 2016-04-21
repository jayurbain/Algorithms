# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:07:33 2016

@author: jayurbain
"""
import sys

class Vertex:
    def __init__(self,num):
        self.id = num
        self.adj = []
        self.color = 'white'
        self.dist = sys.maxint
        self.pred = None
        self.disc = 0
        self.fin = 0
        self.cost = {}

    def addNeighbor(self,nbr,cost=0):
        self.adj.append(nbr)
        self.cost[nbr] = cost
    
    def __str__(self):
        return  str(self.id) + ":color " + self.color + \
                ":dist " + str(self.dist) + \
                ":pred [" + str(self.pred)+ "]\n"

    def getCost(self,nbr):
        return self.cost[nbr]
        
    def setCost(self,nbr,cost):
        self.cost[nbr] = cost

    def setColor(self,color):
        self.color = color

    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime

    def setFinish(self,ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin 

    def getDiscovery(self):
        return self.disc 

    def getPred(self):
        return self.pred 

    def getDistance(self):
        return self.dist 

    def getColor(self):
        return self.color 

    def getAdj(self):
        return self.adj 

    def getId(self):
        return self.id
    

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
 
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n] 
        else:
            return None
            
    def has_key(self,n):
        if n in self.vertList:
            return self.vertList.has_key(n)
        else:
            return None

    def addEdge(self,f,t,c=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],c)
        print 'addEdge', f, t

    def getVertices(self):
        return self.vertList.values()
        
    def __iter__(self):
        return self.vertList.intervalues()

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[0:4].lower()
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


#from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue      

def bfs(g,s):
    #s = g.getVertex(vertKey)
    s.setDistance(0)
    s.setPred(None)
    s.setColor('gray')
    Q = Queue()
    Q.enqueue(s)
    while (Q.size() > 0): 
        w = Q.dequeue()
        for v in w.getAdj():
            print v.id
            if(v.getColor() == 'white'):
                v.setColor('gray')
                v.setDistance(w.getDistance() + 1)
                v.setPred(w)
                Q.enqueue(v)
        w.setColor('black')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

g = buildGraph('fourletterwords.txt')
# graph sanity test
print '# vertices: ', g.numVertices
print g.getVertex('sage')
#print for v in g.getVertex('lord').getAdj(): print v

# bfs
bfs(g, g.getVertex('lord'))
print '****'
traverse(g.getVertex('sage'))




