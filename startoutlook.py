__author__ = 'liwenchang'
 #-*- coding:utf-8 -*-
import os
import time
import win32api, win32pdhutil, win32con, win32com.client
import win32pdh, string


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
        os.system('taskkill /F /IM OUTLOOK.EXE')
        os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.EXE")
    else:
        os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.EXE")





#os.system('taskkill /F /IM OUTLOOK.EXE')
#os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.EXE")

'''
# ***********************************************************************
# ***********************************************************************
def GetProcessID( name ):
    object = "Process"
    items, instances = win32pdh.EnumObjectItems(None,None,object, win32pdh.PERF_DETAIL_WIZARD)
    val = None
    if name in instances :
        hq = win32pdh.OpenQuery()
        hcs = []
        item = "ID Process"
        path = win32pdh.MakeCounterPath( (None,object,name, None, 0, item) )
        hcs.append(win32pdh.AddCounter(hq, path))
        win32pdh.CollectQueryData(hq)
        time.sleep(0.01)
        win32pdh.CollectQueryData(hq)
        for hc in hcs:
            type, val = win32pdh.GetFormattedCounterValue(hc, win32pdh.PDH_FMT_LONG)
            win32pdh.RemoveCounter(hc)
            win32pdh.CloseQuery(hq)
            return val
# ***********************************************************************


# ***********************************************************************
# ***********************************************************************
def Kill_Process ( name ) :
    pid = GetProcessID (name)
    print pid
    if pid:
        print "exist"
        Kill_Process_pid(pid)
    else:
        print "not this proccess"
# ***********************************************************************
'''


'''
#THIS IS SLOW !!
def Kill_Process ( process ) :
    #get process id's for the given process name
    pids = win32pdhutil.FindPerformanceAttributesByName ( process )
    for p in pids:
        handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, p) #get process handle
    win32api.TerminateProcess(handle,0) #kill by handle
    win32api.CloseHandle(handle) #close api

'''

# ***********************************************************************
# ***********************************************************************


'''
def Kill_Process ( process_name ) :
    #get process id's for the given process name
    pids = win32pdhutil.FindPerformanceAttributesByName ( 'OUTLOOK.EXE' )
    print pids
    for p in pids:
        handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, p) #get process handle
#    win32api.TerminateProcess(handle,0) #kill by handle
#    win32api.CloseHandle(handle) #close api
'''


'''
import os
command = 'taskkill /F /IM QQ.exe'
os.system(command)
'''




'''



# ***********************************************************************
# ***********************************************************************
if __name__ == "__main__":
    a = GetAllProcesses()
    print a

    process = 'alg'# process name
    Kill_Process ( process )






os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.EXE")
'''
