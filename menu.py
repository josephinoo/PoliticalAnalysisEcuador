class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Header:
    def header(self):
        file=open("HEADER.TXT")
        for line in file:
            print(bcolors.HEADER+line.strip()+bcolors.ENDC)
        file.close()

    