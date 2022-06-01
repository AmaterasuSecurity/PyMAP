import nmap
import pyfiglet
import subprocess

subprocess.call('clear', shell=True)

ascii_banner = pyfiglet.figlet_format("PyMAPv2")
print(ascii_banner)

nm = nmap.PortScanner()

scan_range = nm.scan(hosts=input())

print (scan_range['scan'])
