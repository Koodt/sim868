class CliConstructor(object):
    def __init__(self):
        self.cli = ''.lower()

    def initial(self, prompt):
        import sys
        self.prompt = prompt
        while self.cli != 'exit':
            self.cli = input(self.prompt).lower()
            try:
                getattr(self, self.cli)()
            except:
                if self.cli != 'exit':
                    print('Command not found')
        sys.exit('Graceful exit')

    def help(self):
        print('''
        kCLI helper:
        help        -       print this message
        create      -       create config
        add         -       add service to config
        del         -       del service from config
        exit        -       exit from kCLI
        ''')

local_cli = CliConstructor().initial('kCLI:>')
