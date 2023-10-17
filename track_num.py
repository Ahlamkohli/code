#import qrcode

#img = qrcode.make('https://youtu.be/h4SAOfwefTI?si=80yDQWwmzL__u5Bm')


#img.save('qrcode.png')


import phonenumbers#module 
from phonenumbers import geocoder #import * (all)
phone_number1 = phonenumbers.parse("+917294536271") 
phone_number2= phonenumbers.parse("+213541909563") 
phone_number3 = phonenumbers.parse("+20699690495")

print("\nphone numbers location\n")
print(geocoder.country_name_for_number(phone_number1,"en"))
print(geocoder.country_name_for_number(phone_number2,"en"))
print(geocoder.country_name_for_number(phone_number3,"en"))

