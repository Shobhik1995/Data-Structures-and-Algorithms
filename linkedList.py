#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 19:24:13 2017

@author: shobhik
"""

class node:
    def __init__(self):
        self.data=None
        self.next=None
        
    def getData(self):
        return self.data
    
    def setData(self,data):
        self.data=data
    
    def hasNext(self):
        return self.next != None
    
    def setNext(self,later):
        self.next=later
    
    def getNext(self):
        return self.next
        
        


class linkedList :
    def __init__(self):
        self.head=node()
        
    
    def printList(self):
        current=self.head
        while (current.hasNext()):
            print(current.data)
            current=current.getNext()
        print (current.getData())    
    
    def addEnd(self,data):
        if(self.head.getData() == None):
            self.head.setData(data)
        current=self.head
        while(current.hasNext()):
            current=current.getNext()
        nn=node()
        nn.setData(data)
        current.setNext(nn)

    def addHead(self,data):
        if(self.head.getData() == None):
            self.head.setData(data)
        nn=node()
        nn.setData(data)
        nn.setNext(self.head)
        self.head=nn            
        
    def addPos(self,pos,data):
        if(pos == 0):
            self.addHead(data)
            return

        current=self.head
        for i in range(1,pos):
            if(not current.hasNext()):
                print ("The list is shorter than you thought! such a position doesn't exist")
            current=current.getNext()
        nn=node()
        nn.setData(data)
        nn.setNext(current.getNext())
        current.setNext(nn)

    def remData(self,data):
        current=self.head
        while(current.hasNext()):
            if(current.getNext().getData() == data):
                current.setNext(current.getNext().getNext())
                current=current.getNext()
                del current
                return
            current=current.getNext()    
        print("looks like the given data is not in the list")        

    def searchList(self,data):
        current=self.head
        while(current.hasNext()):
            if(current.getData() == data ):
                print("found it!, returning a pointer to it")
                return current
            else:
                current=current.getNext()
        if(current.getData() == data ):
            print("found it!, returning a pointer to it")
            return current
        print("couldn' find the data you are looking for")
                
            
                

       
#print ("hello world")


ll=linkedList()
print("Initializing the head of the linked list to 10")
ll.head.setData(10)
ll.printList()
print ("Inserting 12 at the end of the list")
ll.addEnd(12)
ll.printList()
print ("Inserting 32 at the end of the list")
ll.addEnd(32)
ll.printList()
print ("Inserting 100 at the head of the list")
ll.addHead(100)
ll.printList()
print ("Inserting 65 at end of the list")
ll.addEnd(65)
ll.printList()
print ("Inserting 16 at index three")
ll.addPos(3,16)
ll.printList()
print("Inserting 7 at index zero")
ll.addPos(0,7)
ll.printList()
print("Deleting 12")
ll.remData(12)
ll.printList()
print("Searching for 65 ")
pointer=ll.searchList(65)
print(pointer)
print("Searching for 1000")
pointer=ll.searchList(1000)        
    
     
    
