# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:00:13 2019

@author: Himanshu Kandpal
"""

def about_this_computer():
  print("This computer is running on version Everest Puma")
  print("This is your desktop")

about_this_computer()

#parameterized function

def about_this_computer(nameOfUser):
  print("This computer is running on version Everest Puma")
  print("This is your desktop "+nameOfUser)

about_this_computer("Himanshu")