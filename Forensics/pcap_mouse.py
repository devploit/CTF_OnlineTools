#!/usr/bin/python

from PIL import Image, ImageDraw
from subprocess import check_output

print "[*] Extracting data from pcap"
with open('/dev/null') as DN:
    md = [x.strip() for x in check_output(['tshark','-r','captura.pcapng','-Tfields','-e','usb.capdata'],stderr=DN).splitlines()]

x = 500
y = 500

img = Image.new("RGB",(1200,800),"white")
dr = ImageDraw.Draw(img)

print "[*] Drawing you a picture!"
for line in md:
    coords = [j if j<128 else (j-256) for j in [int(k,16) for k in line.split(':')]]
    x += coords[1]
    y += coords[2]
    if coords[0] != 0:
        dr.rectangle(((x - 2, y - 2), (x + 2, y + 2)), fill="black")

img.show()
