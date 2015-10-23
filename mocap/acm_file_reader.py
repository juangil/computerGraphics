import urllib
url = ("http://mocap.cs.cmu.edu/subjects/10/10_06.amc")
urllib.urlretrieve(url, '10_06.amc')

amc_file = open('10_06.amc', 'r')


cont = 0
read_frames = False
print 'Reading header...'
for mline in amc_file:
    if(mline == ":DEGREES\r\n" and read_frames == False):
        read_frames = True
        print 'now reading frames'
    else if(read_frames):
        

print 'reading frame by frame...'
amc_file.close()
