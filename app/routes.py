from app import crm, mail
from flask import render_template
from flask_mail import Message

@crm.route('/')
def index():
	send_msg()
	return render_template('index.html', title='Welcome')
	
def send_msg():
	msg = Message("hello", sender = "mrcrnkovich@gmail.com", 
		recipients = ['mrcrnkovich@gmail.com'])
	msg.body = "Hi, this is auto test from mike's app"
	mail.send(msg)