# -*- coding: utf-8 -*-
"""
Created on 03 Dec 2019

@author: tih, sajid pareeth
"""

import pysebal_py3
import pysebal_calib_py3
##### USER INPUTS

##### For Linux SET THE PATH TO INPUT EXCEL SHEET #####
# inputExcel = r"/mnt/d/PySEBAL_dev/docs/InputEXCEL_v3_3_7_LIN.xlsx"
##### For Windows SET THE PATH TO INPUT EXCEL SHEET #####
inputExcel = r"D:\PySEBAL_dev\docs\InputEXCEL_v3_3_7_WIN.xlsx"
MODE = 'RUN' # Set to CALIB initially to compute thresholds/ Set to RUN to finally compute SEBAL
st = 2 # starting row number
en = 2 # ending row number
####### USER INPUTS FINISH HERE

for number in range(st, en + 1):
    try:
        if MODE == 'CALIB':
            print ('starting line num: %d' % number)
            pysebal_calib_py3.SEBALcode(number,inputExcel)
            print ('line num: %d done' % number)
        else:
            print ('starting line num: %d' % number)
            pysebal_py3.SEBALcode(number,inputExcel)
            print ('line num: %d done' % number)       
    except:
        print ('SEBAL did not run line %d fully' % number)
        

