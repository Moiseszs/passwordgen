from flask import jsonify
import secrets
import string

def get_only_strings_pwd(length):
    strings = string.ascii_letters
    pwd = ''.join(secrets.choice(strings) for i in range(length))
    info = {
        'password': pwd,
        'strength': 2
    }
    return info

def get_only_num_pwd(length):
    digits = string.digits
    pwd = ''.join(secrets.choice(digits) for i in range(length))
    return pwd

def get_alphanum_pwd(length):
    alphanum = string.digits + string.ascii_letters
    pwd = ''.join(secrets.choice(alphanum) for i in range(length))
    return pwd

def get_symbols_pwd(length):
    symbols = string.punctuation
    pwd = ''.join(secrets.choice(symbols) for i in range(length))
    return pwd

def first_cap_letter_strings_pwd(length):
    strings = string.ascii_uppercase + string.ascii_letters
    pwd = ''.join(secrets.choice(strings) for i in range(length))
    return pwd

def all_togheter_pwd(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(secrets.choice(characters) for i in range(length))
    return pwd


def num_symbols_pwd(length):
    pass

def pwd_strength(pwd):
    pass