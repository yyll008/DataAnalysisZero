#/usr/local/bin/python3 
#coding:utf-8
import itchat
itchat.login()
friends=itchat.get_friends(update=True)[0:]
male=female=other=0
for i in friends[1:]:
	sex=i["Sex"]
	if sex==1:
		male+=1
	elif sex==2:
		female+=1
	else:
		other+=1
total=len(friends[1:])

print(male,female,other)