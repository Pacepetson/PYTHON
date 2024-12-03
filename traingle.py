from operator import truediv


def check_triangle():
   sides=[side1,side2,side3]
   sides.sort()
   if sides[2]**2== sides [0]**2+sides[1]**2:
       return true
   return false
   side1=int(input("enter the side 1 of the triangle:"))
   side2=int(input("enter the side 2 of the triangle:"))
   side3=int(input("enter the side 3 of the triangle:"))
   if is_right_angle_traingle(side1,side2,side3):
       print(f"the given sides are part of the right angle traingle:")
   else:
       print(" the given sides are not a part of right angle traingle")