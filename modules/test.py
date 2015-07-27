import wmi
def run(**args):
    print "[*] In test module."
    
    return str(wmi.WMI().Win32_LogicalDisk())
