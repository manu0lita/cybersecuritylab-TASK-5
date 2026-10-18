from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
out = Path(__file__).resolve().parents[1] / 'diagrams' / 'network_diagram.png'
W,H=1500,850
im=Image.new('RGB',(W,H),'#f5f8fc')
d=ImageDraw.Draw(im)
try:
    title=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',42)
    head=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',25)
    body=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
    small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
except OSError:
    title=head=body=small=ImageFont.load_default()
d.text((70,45),'DVWA Capstone - Lab Architecture',font=title,fill='#12233f')
d.text((72,105),'Local-only test flow | schematic - verify actual environment before recording',font=body,fill='#4c5d78')

def box(x,y,w,h,title_text,lines,fill='#ffffff',stroke='#4a7db6'):
    d.rounded_rectangle((x,y,x+w,y+h),radius=22,fill=fill,outline=stroke,width=4)
    d.text((x+22,y+20),title_text,font=head,fill='#18345b')
    yy=y+66
    for line in lines:
        d.text((x+22,yy),line,font=body,fill='#25364d'); yy+=31

def arrow(a,b,color='#3d6fa8'):
    d.line((a[0],a[1],b[0],b[1]),fill=color,width=5)
    import math
    ang=math.atan2(b[1]-a[1],b[0]-a[0]); L=18
    p1=(b[0]-L*math.cos(ang-math.pi/6),b[1]-L*math.sin(ang-math.pi/6))
    p2=(b[0]-L*math.cos(ang+math.pi/6),b[1]-L*math.sin(ang+math.pi/6))
    d.polygon([b,p1,p2],fill=color)

box(75,220,340,190,'Tester / analyst',['Kali Linux VM','Firefox / optional Burp','Authorized operator'],fill='#eaf3ff')
box(565,220,370,190,'Target application',['DVWA web application','http://127.0.0.1:4280','Loopback binding recommended'],fill='#e8f7f1',stroke='#3f9276')
box(1090,190,330,210,'Data & logs',['DVWA database','Web / container logs','Use dummy training data'],fill='#fff4df',stroke='#d29a35')
arrow((415,310),(565,310)); arrow((935,310),(1090,310))
box(350,525,390,190,'Offline detection',['Python log indicator script','Reads a local log file only','Pattern match = triage signal'],fill='#f0ecff',stroke='#8a74c9')
box(835,525,420,190,'Incident response',['Detect and triage','Contain / document remediation','Recover and retest'],fill='#ffeef0',stroke='#c66b79')
arrow((1255,390),(1125,525)); arrow((740,620),(835,620))
d.text((76,790),'Safety: Never expose intentionally vulnerable DVWA to the public Internet. Synthetic logs are not real target evidence.',font=small,fill='#8a3941')
im.save(out)
print(out)
