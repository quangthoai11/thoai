# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:46:04 2024

@author: Student
"""

chuoi = "Đại học quốc gia , Khu phố 6  , P. Linh Trung , Q. Thủ đức, Tp.HCM"
sub_strings = [s.strip() for s in chuoi.split(',')]
for sub_string in sub_strings:
    print(sub_string)   
    
