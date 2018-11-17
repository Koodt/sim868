#!/usr/bin/python

class someThing(object):
    def __init__(self, port, banner):
        self.port = port
        self.banner = banner

    def somePrint(self):
        print("[+] Checking for " + self.banner + " on port " + str(self.port))
        #[+] Checking for FreeFloat FTP Server on port 21
        print("[+] Checking for %s on port %s" % (self.banner, self.port))
        #[+] Checking for FreeFloat FTP Server on port 21
        print("[+] Checking for {} on port {}".format(self.banner, self.port))
        #[+] Checking for FreeFloat FTP Server on port 21


anotherPrintThing = someThing(port = 22, banner = "FreeFloat SFTP Server")
somePrintThing = someThing(21, "FreeFloat FTP Server")

somePrintThing.somePrint()
anotherPrintThing.somePrint()

services = {'http': 25, 'https': 443, 'ftp': 21, 'sftp': 22, 'smtp': 25,}

print(services.keys())
print(services.items())

somePrintThing = someThing(services['http'], 'http')
somePrintThing.somePrint()
