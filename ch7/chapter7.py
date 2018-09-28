import html

# section 7.1
# we want a function that can accept any number of input arguments
def func_anyArgs(first, *rest):
    """
    where rest is a tuple of all the extra arguments passed.
    """
    return (first + sum(rest))/(1 + len(rest))

# sample call
print(func_anyArgs(1, 2))
print(func_anyArgs(1, 2, 3, 4))


def make_element(name, value, **attrs):
    """
    here, attrs is a dictionary holds the passed keyword arguments
    """
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name = name, attrs = attr_str, value = html.escape(value))
    return element

# sample calls
# to create '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))
# to create '<p>&lt;span&gt;</p>'
print(make_element('p','<span>'))


# section 7.2
# we want a function to only accept a certain arguments by keyword
def recv(maxsize, *, block):
    print('receive a message')
    pass

# sample call
recv(1024, block=True)