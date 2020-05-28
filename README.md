# ncsf
Nmap Clock-Skew Fix

This is a tool to take the clock-skew from an Nmap xml output, then sync the localtime from the target to your Kali machine.

This may be needed if the clock-skew could effect some stuff, and it is important to have the time sync'd. I wrote this overly complicate script as some boxes from HackTheBox does not play nicely with me if my Kali machine is not timed sync. So now I have a quick way to sync both together.

You can get the clock-skew time when you run the safe scripts option:
nmap -sC <host> -oA scan

This will create a .nmap, .gnmap and a .xml files.

So to sync you machine to the target, just type:

python ncsf.py -f scan.xml


