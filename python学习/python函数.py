# list_square=[]
# for i in range(1,4):
#     list_square.append(i**2)
#
# print(list_square)
#
# list_square2=[i**2 for i in range(1,4)]
# print("list_square2",list_square2)
#
# list_square3=[i**2 for i in range(1,4) if i !=1]
#
# print(list_square3)



def method(a):
    print(a)

method(1)

# def method(a,b=[]):
#     """
#
#     :param a:
#     :return:
#     """
#     print(a)
#     print(b)
#
# method(1,b=2)


# def method(a):
#     print(a)
#     return a+2
#
#
# print(method(1))

# def method(a,b=[]):
#     b.append(a)
#     return b
#
#
# print(method(1))
# print(method(2))
#
# def method(a,b):
#     """
#         :param a:
#     :param b:
#     :return:
#     """
#     print(a)
#     print(b)
#     return b
# method(1,2)
# method(b=1,a=2)
# method(3,b=2)


# def method(**a):
#     """
#
#     :param a:
#     :return:
#     """
#     print(a.keys( ))
# method(a=1,b=2,c=3)

# def method(*a):
#     """
#
#     :param a:
#     :return:
#     """
#     print(a[0])
#     print(a[1])
#     print(a[2])
#     print(a[3])
#
# method(1,2,3,4)

# def method(*,a):
#     """
#
#     :param a:
#     :return:
#     """
#     print(a)
#
# method(a=1)
# print(list(range(3,6)))
#
# list_a=(3,6)
# list(range(*list_a))


# def method(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# dic1={"a":1,"b":2,"c":3}
# method(**dic1)

#
# y=lambda x:x*2
# print(y(2))

# y=lambda x,y,z:x+y+z
# print(y(2,3,4))

# def method(str):
#     print("111111")