import subprocess
import sys

URL = ""
KEY = ""


def getURLKEY():
    global URL
    global KEY
    try:
        URL = sys.argv[1]
        KEY = sys.argv[2]
    except:
        try:
            URL = sys.argv[1]
            KEY = ""
        except:
            URL = "http://ympt.000webhostapp.com"
            KEY = "/?name="


def main():
    getURLKEY()
    
    command = ["xsser", "-u", URL, "-g", KEY]

    p = subprocess.Popen(command, stdout=subprocess.PIPE)

    response_text = p.stdout.read()
    retcode = p.wait()

    if retcode != 0:
        print "something went wrong with the shell execution of the command."
        return 0

    print ''.join(response_text.split("===========================================================================")[7:9])
    


if __name__ == "__main__":
    main()