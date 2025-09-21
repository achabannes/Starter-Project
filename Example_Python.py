import math

# This was code for my discrete class hw. I am using it to test github function 
# DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class Triangles:

    def isIsoscelesTriangle(self, x1, y1, x2, y2, x3, y3):

        if x1==x2 and y1==y2:

            return False

        if x2==x3 and y2==y3:

            return False

        if x3==x1 and y3==y1:

            return False

        

        distance_1= math.sqrt((x1-x2) **2 +(y1-y2) **2)

        distance_2= math.sqrt((x2-x3) **2 +(y2-y3) **2)

        distance_3= math.sqrt((x3-x1) **2 +(y3-y1) **2)

        

        if distance_1==distance_2:

            return True

        if distance_2==distance_3: 

            return True

        if distance_3==distance_1:

            return True

        else :

            return False 


# For testing your code uncomment below lines.


t = Triangles()

print(t.isIsoscelesTriangle(0, 0, 2, 0, 1, 2))


# Comment or delete the above test code before submitting.