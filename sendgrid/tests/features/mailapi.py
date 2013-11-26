from lettuce import * # lettuce
import pycurl #much better than urllib ;-)
import urllib #to clean up my calls
import StringIO #to write the pycurl response
from email.Utils import formatdate # for rfc 2822 time

def basic_email():
    world.rootURL = 'http://sendgrid.com/api/mail.send.json'
    world.emailattributes = {}
    world.emailattributes['api_user'] = 'username'
    world.emailattributes['api_key'] = 'password'
    world.emailattributes['to'] = 'email@gmail.com'
    world.emailattributes['from'] = 'jjbigglsworth@sendgrid.com'
    world.emailattributes['subject'] = 'The party is in the back room'
    world.emailattributes['text'] = 'Why aren\'t you here?  I\'d really like to beat you in a game of poker!'
    #world.fileattach = None

@step('When I fill in the fields to, from, subject, and text')
def generate_basic_email(step):
    basic_email()
    world.call = world.rootURL+'?'+urllib.urlencode(world.emailattributes)

@step('When I fill out all the fields of the Mail API')
def generate_advanced_email(step):
    basic_email()
    world.emailattributes['html'] = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="content-type" content="text/html; charset=ISO-8859-1"></head><body bgcolor="#ffffff" text="#000000">We are having a party!<br><br>Woo hoo,<br>Eric<br></i></div></body></html>"""
    world.emailattributes['bcc'] = 'bcc_email@gmail.com'
    world.emailattributes['date'] = formatdate()
    world.emailattributes['headers'] = '{"X-Mailer": "Stinky Microsoft Outlook"}'
    world.emailattributes['fromname'] = 'JJ Bigglesworth'
    world.emailattributes['x-smtpapi'] = '{"category" : "interview"}'
    world.emailattributes['files'] = 'eric.jpg'
    #world.fileattach = open('eric.jpg', 'rb').read()
    world.call = world.rootURL+'?'+urllib.urlencode(world.emailattributes)
        
@step('Then make the mail.send.json call')
def call_mail_api(step):
    email_request = pycurl.Curl()
    email_request.setopt(pycurl.URL,world.call)
    #if world.fileattach: #not necessary -- the web interface doesn't seem to do HTTP POST
    #   email_request.setopt(pycurl.POSTFIELDS, world.fileattach)
    #   email_request.setopt(pycurl.POST, 1)
    world.email_request_page = StringIO.StringIO()
    email_request.setopt(pycurl.WRITEFUNCTION, world.email_request_page.write)    
    email_request.perform()
    email_request.close()
    
@step('I should receive a successful response')
def process_response(step):
    assert world.email_request_page.getvalue()  == '{"message":"success"}'
    
@after.each_scenario
def print_out(step):
    print '\nHere is the mail.send.json call I made:\n'
    print world.call 
    print '\nAnd the result:\n' 
    print world.email_request_page.getvalue()  