# *****
# *****
# *****
# *****
# *****
# lines = 10
# for j in range(lines):
#     for i in range(lines):
#         print("*",end=" ")
#     print()


# lines = 10
# for j in range(lines):
#     print("*"*lines)
   
# *
# **
# ***
# ****
# *****


# lines = 5
# for j in range(lines):
#     for i in range(j+1):
#         print("*",end=" ")
#     print()


# lines = 5
# for j in range(lines):
#     print("*"*(j+1))

# *****
# ****
# ***
# **
# *

# lines = 5
# for j in range(lines):
#     for i in range(lines-j):
#         print("*",end=" ")
#     print()

#     *
#    **
#   ***
#  ****
# *****


# lines = 5
# for j in range(lines):
#     for k in range(lines-(j+1)):
#          print(" ",end=" ")

#     for i in range(j+1):
#         print("*",end=" ")
#     print()

# *****
#  ****
#   ***
#    **
#     *


# lines = 5
# for j in range(lines):
#     for k in range(j):
#          print(" ",end=" ")

#     for i in range(lines-j):
#         print("*",end=" ")
#     print()

    
#     *
#    * *
#   * * *
#  * * * *
# * * * * * 



# lines = 5
# for j in range(lines):
#     for k in range(lines-(j+1)):
#          print(" ",end="")

#     for i in range(j+1):
#         print("* ",end="")
#     print()


#     *
#    * *
#   * * *
#  * * * *
# * * * * * 
#  * * * *
#   * * *
#    * *
#     *


#     *
#    * *
#   *   *
#  *     *
# *       * 
#  *     *
#   *   *
#    * *
#     *



# lines = 5
# for j in range(lines):
#     for k in range(lines-(j+1)):
#          print(" ",end="")

#     for i in range(j+1):
#         print("* ",end="")
#     print()
# for j in range(lines):
#     for k in range(j+1):
#          print(" ",end="")

#     for i in range(lines-(j+1)):
#         print("* ",end="")
#     print()



# lines = 5
# for j in range(lines):
#     for k in range(lines-(j+1)):
#          print(" ",end="")

#     for i in range(j+1):
#         if i==0 or i==(j):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for j in range(lines):
#     for k in range(j+1):
#          print(" ",end="")

#     for i in range(lines-(j+1)):
#         if i==0 or i==(lines-(j+2)):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()



lines = 11
stars=1
spaces=lines
mid = (lines//2)+1
for i in range(1,lines+1):
    for k in range(1,spaces):
        print(" ",end="")
    for j in range(1,stars+1):
        if j==1 or j==stars:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<mid:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1