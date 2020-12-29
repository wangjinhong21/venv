import os

# # os.mkdir("testdir")#创建目录
# print(os.listdir("./"))#打印目录
# # os.removedirs("testdir")
# print(os.getcwd()) #当前路径

#再文件夹b下的test.txt中输入一串信息

print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")

if not os.path.exists("b/test.txt"):
    f=open("b/test.txt","w")
    f.write("hello")

