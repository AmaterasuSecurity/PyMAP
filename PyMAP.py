import nmap
import pyfiglet
import subprocess

subprocess.call('clear', shell=True)

ascii_banner = pyfiglet.figlet_format("PyMAP")
print(ascii_banner)

# input for ports to scan
p = input()

# input for target host
t = input()

# start nmap port scanner
n = nmap.PortScanner()

# iterates range
for i in range(p+1):

    # target being scanned
    res = n.scan(t,str(1))

    # results of the scan
    res = res['n'][t]['tcp'][i]['state']

    print(f'port {i} is {res}.')