__author__ = 'liwenchang'

 #-*- coding:utf-8 -*-
import os, win32com.client


def check_exsit(process_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        #print '%s is exists' % process_name
        return bool(True)
    else:
        #print '%s is not exists' % process_name
        return bool(False)



if __name__ == '__main__':
    process='OUTLOOK.EXE'

    if check_exsit(process):
        os.popen('taskkill /F /IM OUTLOOK.EXE')
        os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.EXE")
    else:
        os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.EXE")
