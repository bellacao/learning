# 3-4

guest_list = ['amanda','cindy','james']
print(guest_list)

message_01 = 'Dear ' + guest_list[0] + " you can come today."
message_02 = 'Dear ' + guest_list[1] + " you can come today."
message_03 = 'Dear ' + guest_list[2] + " you can come today."

print(message_01)
print(message_02)
print(message_03)

# 3-5

message_04 = guest_list[1] + ' cannot come.'
print(message_04)

guest_list[1] = 'my grandma and my grandpa'

message_01 = 'Dear ' + guest_list[0] + " you can come today."
message_02 = 'Dear ' + guest_list[1] + " you can come today."
message_03 = 'Dear ' + guest_list[2] + " you can come today."

print(message_01)
print(message_02)
print(message_03)

#3-6

guest_list.append('ai sheng lian')
guest_list.insert(0,'liu jun ming')
guest_list.insert(1,'lu hu')

message_01 = 'Dear ' + guest_list[0] + " you can come today."
message_02 = 'Dear ' + guest_list[1] + " you can come today."
message_03 = 'Dear ' + guest_list[2] + " you can come today."
message_04 = 'Dear ' + guest_list[3] + " you can come today."
message_05 = 'Dear ' + guest_list[4] + " you can come today."
message_06 = 'Dear ' + guest_list[5] + " you can come today."

print(message_01)
print(message_02)
print(message_03)
print(message_04)
print(message_05)
print(message_06)

#3-7

name = guest_list.pop(0)
message = 'Sorry ' + name + ', I am kidding you.'
print(message)

name = guest_list.pop(0)
message = 'Sorry ' + name + ', I am kidding you.'
print(message)

name = guest_list.pop(1)
message = 'Sorry ' + name + ', I am kidding you.'
print(message)

name = guest_list.pop(2)
message = 'Sorry ' + name + ', I am kidding you.'
print(message)

message = 'dear ' + guest_list[0] + ' you can come tonight.'
message_01 = 'dear ' + guest_list[1] + ' you can come tonight.'
print (message)
print (message_01)

del guest_list[0]
del guest_list[0]
print(guest_list)