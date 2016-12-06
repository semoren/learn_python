print(type(123))
print(type('s'))
print(type(None))

print(type(abs))

print(type(123) == int)

import types
def fn():
    pass

print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type((x for x in range(10))) == types.GeneratorType)

print( "s ", isinstance([1,2,3], (list, tuple)))

print(dir('ABC'))

