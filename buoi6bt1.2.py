# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:36:49 2024

@author: Student
"""

chuoi="dai hoc quoc gia, khu pho 6, P.linh trung, Q.thu duc, Tp.hcm"
sub_trings = chuoi.replace('P. ','').replace('Q. ','').replace('Tp. ','').split(', ')
for s in sub_trings:
    print(s)
    
