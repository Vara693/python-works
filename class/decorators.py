#Decorators
def greet(fx):
    def mfx(*args, **kwargs):
        print("\nNamaste")
        fx(*args, **kwargs)
        print("Loved being with you")
    return mfx

@greet
def hello():
    print("Substaintial hello!")

@greet
def add(a,b):
    print(a+b)

hello()
add(30,84)