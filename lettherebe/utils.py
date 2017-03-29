from numpydoc.docscrape import NumpyDocString


def extract_arguments(function):
    """
    Given a Python function, parse the numpydoc docstring and return a standard
    list of arguments.
    """
    doc = NumpyDocString(function.__doc__)
    arguments = []
    for arg_name, arg_type, arg_description in doc['Parameters']:
        argument = {}
        argument['name'] = arg_name
        argument['type'] = type(arg_type.split(',')[0].strip())
        argument['optional'] = 'optional' in arg_type
        argument['description'] = arg_description
        arguments.append(argument)
    print(arguments)
    return arguments
