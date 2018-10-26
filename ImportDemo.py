'''
Created on 2018年10月22日

@author: yinyayun
'''

from .DenpendenceDemo import DenpendenceDemo


class ImportDemo():
    def __init__(self):
        self.dp = DenpendenceDemo()

    def zz(self):
        return self.dp.dep()
