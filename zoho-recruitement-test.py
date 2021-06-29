# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:00:00 2021
: zoho recruitment
"""
import math

msg = "WELCOME"
# msg = "WATER"

#get the middle character
index = math.ceil(len(msg)/2)

#seggreagte left list and right list
left, right =(msg.split(msg[index-1]))

#rejoining string
out = msg[index-1]+ right + left

#printing the pattern
for i in range(1,len(out)+1):
     
    lists = [""]*int(len(out)-i)
    lists.append(out[0:i])
    print(" ".join(lists))
   
    
