import itchat,time,re
from itchat.content import *
@itchat.msg_register([TEXT])
def text_reply(msg):
	match = re.search('新年',msg['Text']).span()
	if match:
		itchat.send(('那我就祝您狗年大吉大利'),msg['FromUserName'])
@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
def other_reply(msg):
	itchat.send(('那我就祝福您狗年大吉大利'),msg['FromUserName'])
itchat.auto_login(True)
itchat.run()