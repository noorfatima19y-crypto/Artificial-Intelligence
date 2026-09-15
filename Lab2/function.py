#defining and calling a function

def my_function(fname):
    print(fname +"refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

#passing list as a parameter

def func(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
func(fruits)


#returrn values

def myfunction(x):
    return 5*x
print(myfunction(3))
print(myfunction(5))
print(myfunction(4))

#keyword arguments

def function(child3,child2,child1):
    print("The youngest child is "+child3)

function(child1="emil",child2="tobias",child3="linus")



