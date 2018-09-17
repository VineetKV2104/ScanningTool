import os

def basicScan(ip):
    os.system('nmap '+ip+' -sS')

def osScan(ip):
    os.system('nmap '+ip+' -O')

def TCP(ip):
    os.system('nmap '+ip+' -sT')

def UDP(ip):
    os.system('nmap '+ip+' -sU')

def version(ip):
    os.system('nmap '+ip+' -sV')

def intenseScan(ip):
    os.system('nmap '+ip+' -sT -sU -O -A -sV')



ip=input("Enter target IP: ")
while(1):
    print(" ")
    print("1.Basic Scan 2.OS Scan 3.TCP Port Scan 4.UDP Port Scan 5.Version Detection 6.Intense Scan 7.Exit")
    c=int(input("Enter Choice: "))
    if(c==1):
        basicScan(ip)
    if(c==2):
        osScan(ip)
    if(c==3):
        TCP(ip)
    if(c==4):
        UDP(ip)
    if(c==5):
        version(ip)
    if(c==6):
        intenseScan(ip)
    if(c==7):
        break


