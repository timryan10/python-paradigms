def ascending(n):
    arr = []
    for i in n:
        for a in i:
            arr.append(a)
    return sorted(arr)
print(ascending([[556,643,1523,4652]]))

"""
1. How does this solution ensure data immutability?
    This solution ensures data immutability because it does not change the data within the array.
    A new list is created through the function.
2. Is this solution a pure funciton? Why or why not?
    Yes this function is a pure function because it doesn't change any lists or sets outside of 
    the function.
3. Is this solution a higher order function? Why or why not?
    No this function is not a higher order function because it doesn't take in any functions as 
    an argument, nor does the function have any functions within it.
4. Would it have been easier to solve this problem using a different programming style? Why or why not?
    I personally feel that no matter how good I get with coding there will always be an easier way to 
    write it. This also depends on the variables and purpose of the function.
5. Why is funcitonal progamming a helpful paradigm when solving this problem?
    Functional programming is a helpful paradigm when solving this problem because this function does 
    not require data that needs to be changed.
"""
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        if self.condition == "trashed":
            print("Condtion has been restored")
        else:
            print("Repaired")

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, other):
        if isinstance(other, Podracer):
            other.condition = 'trashed'
            print("crashed")
        else:
            print("Invalid target for flame jet")

podracer1 = Podracer(500, "perfect", 1000)
print("Before repair:", podracer1.condition)
podracer1.repair()
print("After repair:", podracer1.condition)

anakins_pod = AnakinsPod(600, "perect", 1500)
print("Before boost:", anakins_pod.max_speed)
anakins_pod.boost()
print("After boost:", anakins_pod.max_speed)

sebulbas_pod = SebulasPod(700, "perfect", 2000)
print("Before flame jet:", podracer1.condition)
sebulbas_pod.flame_jet(podracer1)
print("After flame jet:", podracer1.condition)
"""
1. How does this solution demonstrate the four pillars of OOP?
    This solution demonstrates inheritance, polymorphism and encapsulation. Both Anakins Pod and Sebulbas
    Pod inherit from the Podracer class. Encapsulation is used when the unique attributes to the Pods are
    encapsulated within each of the three classes. Finally, polymorphism is used since Anakins Pod and Sebulbas pod
    are their own classes but adhere to the Podracer class.
2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    I don't think an easier solution could have been used for this problem. As shown in our last class, OOP is very 
    useful when it comes to reducing the amount of code written as well as being able to reuse the same code.
3. How in particular did Object Oriented Programming assist in the solving of this problem?
    As stated in question 2, using OOP reduced the amount of code written and allowed me to reuse code in different 
    classes.
"""