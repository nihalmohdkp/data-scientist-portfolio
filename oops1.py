# class Jump:
#     x=10
#     j=9
#     print (x)
# y= Jump()
# print(y.x)
# print(y.j)
# print(y)
# class Humen:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def talking(self):
#         print (self.name,'jijijiji')
# class Father:
#     def __init__(self):
#         print ('father')
#     def work(self):
#         print('i can work')
# class Mother:
#     def __init__(self):
#         print('mother')
#     def superwomen (self):
#         print('super women')

# class child(Father,Mother):
#     def __init__(self):
#         print('study')
#         pass
# ammu=child()
# anu=Mother()
class Person :
    name='ammu'
    place='anamangad'
    age=23
obj = Person()
x=getattr(obj, 'name')
x= getattr(obj,'age','not given')
print(x)
# delattr(Person, 'name')
# print (obj.name)
x=hasattr(Person,'name')
print (x)

