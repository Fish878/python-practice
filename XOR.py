# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:26:47 2021

@author: user
"""

import sys
class Crypt:
    def __init__(self,key):
       self.key= key
    def encrypt(self, msg):
        key= list(self.key)
        msgList= list(msg)
        msgLen=len(msgList)
        cipherText = ['']*msgLen
        for i in range(msgLen):
            cipherText[i]= chr(ord(msgList[i])+int(key))
        return ''.join(cipherText)
    def decrypt(self,msg):
        key= list(self.key)
        msgList= list(msg)
        msgLen=len(msgList)
        cipherText = ['']*msgLen
        for i in range(msgLen):
            cipherText[i]= chr(ord(msgList[i])+int(key))
        return ''.join(cipherText)
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv)>2:
        if sys.argv[1]=='-e':
            c= Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3]))
        elif sys.argv[1]=='-d':
            c = Crypt(sys.argv[2])
            print(c.decrypt(sys.argv[3]))