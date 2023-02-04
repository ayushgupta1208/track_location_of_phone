""""TRACK PHONE LOCATION"""
import phonenumbers #phonenumber module
from phonenumbers import timezone,geocoder,carrier #these are functions of "phonenumbers"module
number=input("enter our no.with +___")
phone= phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
