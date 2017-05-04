#!/bin/bash

curl --verbose \
-X POST \
--data-binary @eric.jpg \
--header "Content-Type: image/jpg" \
--header "Content-Transfer-Encoding: UTF-8" \
"http://sendgrid.com/api/mail.send.json?to=eric.linen%40mail.com&toname=Eric%20Lineng&x-smtpapi=%7B%22category%22%20%3A%20%22interview%22%7D&from=jjbigglesworth%40sendgrid.com&fromname=JJ%20Bigglesworth&subject=Hey%20there%2C%20pokey%20web%20interface&text=I%20would%20like%20to%20ask%20you%20a%20couple%20of%20questions%2C%20busta!&html=%3C!DOCTYPE%20HTML%20PUBLIC%20%22-%2F%2FW3C%2F%2FDTD%20HTML%204.01%20Transitional%2F%2FEN%22%3E%3Chtml%3E%3Chead%3E%3Cmeta%20http-equiv%3D%22content-type%22%20content%3D%22text%2Fhtml%3B%20charset%3DISO-8859-1%22%3E%3C%2Fhead%3E%3Cbody%20bgcolor%3D%22%23ffffff%22%20text%3D%22%23000000%22%3EMy%20email%20body%20is%20kind%20of%20pointless%3Cbr%3E%3Cbr%3EThanks%20for%20coming%2C%3Cbr%3EEric%3Cbr%3E%3C%2Fi%3E%3C%2Fdiv%3E%3C%2Fbody%3E%3C%2Fhtml%3E&bcc=eric.linenberg%40siriusxm.com&date=Tue%2C%2026%20Nov%202013%2020%3A43%3A53%20-0000&headers=%7B%22X-Mailer%22%3A%20%22Stinky%20Microsoft%20Outlook%22%7D&files=eric.jpg&api_user=elinenbe&api_key=123456"
