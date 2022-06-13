#!/usr/bin/env python3

import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_passwd():
    length = int(input("Enter Passwd Length > "))
    
    alphabets_count = int(input("Enter alphabets count in password: "))
	digits_count = int(input("Enter digits count in password: "))
	special_characters_count = int(input("Enter special characters count in password: "))
 
 	characters_count = alphabets_count + digits_count + special_characters_count

	if characters_count > length:
		print("Characters total count is greater than the password length")
		return

    
    