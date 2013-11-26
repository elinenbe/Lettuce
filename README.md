A handful of scenarios I used to learn a bit about lettuce, and complete the following:

    Starting at http://sendgrid.com/docs/api_workshop.html
    Build a test that fills out the api method for mail. 
    Verify you can fill out all the supported fields and that the email will send properly.

Just run lettuce from the tests folder.  pycurl is needed to do the http call.

You will need to use put your own credentials on lines 10 and 11.  Replace username with your SendGrid username and password with your SendGrid password.

    world.emailattributes['api_user'] = 'username'
    world.emailattributes['api_key'] = 'password'

Line 12 and 27 should also have valid email addresses.