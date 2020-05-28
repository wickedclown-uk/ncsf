import xml.etree.ElementTree as ET
import re
import datetime
import subprocess
import argparse

time = ''
nmap = ''




def NmapSkew(n):
    for i in root.iter('script'):
        dic = i.attrib
        out = str(i.attrib)
        if 'clock-skew' in out:
            time0 = (dic["output"])
            if 'h' not in time0:
                time = '0h'+time0
            else:
                time = time0
    
    return time


def NegativeSkew(n):
         
    n = n.replace('-','')
    n = n.replace('h',':')
    n = n.replace('m',':')
    n = n.replace('s','')
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print ("Current time of local machine: "+current_time)
    h, m, s = n.split(':')
    sec = datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()

    t2 = datetime.datetime.now() + datetime.timedelta(seconds=-int(sec))
    new_time = t2.strftime("%H:%M:%S")
    print ("New time: "+new_time)
    subprocess.call(['date','+%T','-s',new_time])

def PostiveSkew(n):
    n = n.replace('h',':')
    n = n.replace('m',':')
    n = n.replace('s','')

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print ("Current time of local machine: "+current_time)
    h, m, s = n.split(':')
    sec = datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()
    t2 = datetime.datetime.now() + datetime.timedelta(seconds=int(sec))
    new_time = t2.strftime("%H:%M:%S")
    print ("New time: "+new_time)
    subprocess.call(['date','+%T','-s',new_time])

parser = argparse.ArgumentParser(description='Nmap clock-skew corrector')
parser.add_argument("-f", help="Select you nmap .xml file")
args = parser.parse_args()

nmap = args.f

tree = ET.parse(nmap)
root = tree.getroot()

print ('Clock-Skew :'+NmapSkew(time))
if '-' in NmapSkew(time):
    NegativeSkew(NmapSkew(time))
    
else:
    PostiveSkew(NmapSkew(time))