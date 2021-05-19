import requests
import json
from os import system as s
banner = """                       __  ______  _____
||     ||     ^        ____  |     ̸    |       |    \
||     ||    / \      /      |   ̸      |       |     |
||=====||   /___\    |       |<        |-----  |< __/
||     ||  /     \   |       |  \      |       |  \
||     || /       \   \____  |    \_   |______ |   \__
"""
number = input("enter number with + code etc what ever you hve for india code is +91 !!!\n ->")

Message = input("\n enter Message")
k=Message[0:70]

m =input("send message Y/N")
if m== "y" or m== "Y":
  print("\n"+number+"\n"+k+"\n")
  p = requests.post('https://textbelt.com/text', {
  'phone': number,
  'message': k,
  'key': 'textbelt',
    })
  print(p.json())
elif m =="N" or m== "n":
  print ("exiting !!!!")
  Quit()
else :
  print("failed")
  
