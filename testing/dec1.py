def decorator(function):
    def change_color(argument):
        argument = '\033[95m' +  argument
        function(argument)
    return change_color

def default_output(argument):
    print(argument + ' output')

default_output('Default')

@decorator
default_output(argument)

default_output('Default')
