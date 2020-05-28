# ncsf
Nmap Clock-Skew Fix

This is a tool to take the clock-skew from an Nmap xml output, then sync the localtime from the target to your Kali machine.

This may be need if the clock-skew could effect some stuff, and it is important to have the time sync'd.

You can get the clock-skew time when you run the safe scripts option:
nmap -sC <host> -oA scan

This will create a .nmap, .gnmap and a .xml files.

So to sync you machine to the target, just type:

ncsf.py -f scan.xml


