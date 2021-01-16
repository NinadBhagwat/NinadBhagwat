9# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:45:13 2021

@author: NINAD
"""
import string
import random

p1 = string.ascii_letters
p2 = string.ascii_lowercase
p3 = string.ascii_uppercase
p4 = string.digits

pass_len = int(input("Enter The Password Length: \n"))
pw = []
pw.extend(list(p1))
pw.extend(list(p2))
pw.extend(list(p3))
pw.extend(list(p4))

random.shuffle(pw)
print("".join(pw[0:pass_len]))

