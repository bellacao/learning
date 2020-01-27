# 这是第一堂课程，学习了变量 + 注释

message = "hello python World"
print(message.title())
print(message.upper())
print(message.lower())

message_01 = "20081210"

x = 5 
Y = 6.7

message_02 = message + str(x) + message_01

print(x+Y)

print(message_02)

#   这是第二堂课，学习了

bella = ['Cindy','Amanda','James']
print(bella)
print(bella[1])
print(bella[-3])
# print(bella[-4])

bella.append('bella')
print(bella[3].title())

james = 'amanda'
print(james)

print(bella[-1])

message_03 = "I am  " + bella[-1].title() + "."
print(message_03)

bella[2]='Bella'
print(bella)

bella.insert(0,"james")
print(bella)

del bella[-1]
bella.remove('Amanda')
print(bella)