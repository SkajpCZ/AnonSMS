#!/usr/bin/env python3
# Coded by Skajp
import requests, time, os

if os.name == 'nt': os.system("cls")

snum = input("\n\033[1;93m Target \033[0;90m>\033[1;37m ")
for i in smsnumb: a = 1 if i == "+" else 0
if a == 0: smsnumb = input("\n\033[1;93m Target \033[1;38;2;160;140;180m(with country code) \033[0;90m>\033[1;37m ")
msg = input("\n\033[1;93m Message \033[0;90m>\033[1;37m ")

resp = requests.post('https://textbelt.com/text', {'phone': f'{snum}','message': f'{msg}','key': 'textbelt',})

print(resp.json())
time.sleep(2)