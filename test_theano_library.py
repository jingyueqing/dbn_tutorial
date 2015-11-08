import theano

a = theano.tensor.vector('a')   # declare variable
b = a * a                       # build expression
f = theano.function([a], b)     # compile function
print f([0, 1, 2])
