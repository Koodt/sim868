def first_decorator(function):
    def change_output(argument):
        argument = 'Custom'
        function(argument)
    return change_output

def second_decorator(function):
    def change_color(argument):
        argument = '\033[92m' +  argument
        function(argument)
    return change_color

def third_decorator(function):
    def change_color(argument):
        argument = '\033[95m' +  argument
        function(argument)
    return change_color

def default_output(argument):
    print(argument + ' output')

default_output('Default')

@first_decorator
def default_output(argument):
    print(argument + ' output')

default_output('Default')

@second_decorator
def default_output(argument):
    print(argument + ' output')

default_output('Default')

@third_decorator
def default_output(argument):
    print(argument + ' output')

default_output('Default')

@first_decorator
@second_decorator
@third_decorator
def default_output(argument):
    print(argument + ' output')

default_output('Default')
