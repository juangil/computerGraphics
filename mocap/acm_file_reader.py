import urllib
import numpy as np
url = ("http://mocap.cs.cmu.edu/subjects/10/10_06.amc")
urllib.urlretrieve(url, '10_06.amc')

#url = ("http://mocap.cs.cmu.edu/subjects/10/10.asf")
#urllib.urlretrieve(url, '10.asf')

#asf_file = open('10.asf', 'r')

#asf_file.close()

amc_file = open('10_06.amc', 'r')
cont = 0
read_frames = False
print 'Reading header...'
frame = 0
for mline in amc_file:
    if(mline == ":DEGREES\r\n" and read_frames == False):
        read_frames = True
        print 'now reading frames'
    elif(read_frames):
        params = mline.split(' ')
        if param[0] == str(frame) + '\r\n':
            frame += 1



print 'reading frame by frame...'
amc_file.close()
