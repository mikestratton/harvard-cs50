def f(*args, **kwargs):
    print("Positional: ", args)
    print("Named: ", kwargs)


f(galleons=100, sickles=50, knuts=25)