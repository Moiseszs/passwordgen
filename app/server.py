from methods import *
from flask import Flask, jsonify, request

server = Flask(__name__)

@server.route('/')
def get_string():
    return jsonify('Password generator API')

@server.route('/strings/<int:length>/')
def str_wrapper(length):
    if(length < 1):
        length = 1
    return jsonify(get_only_strings_pwd(length))

@server.route('/digits/<int:length>')
def onlydig_wrapper(length):
    return jsonify(get_only_num_pwd(length))

@server.route('/alphanum/<int:length>')
def alphanum_wrapper(length):
    return jsonify(get_alphanum_pwd(length))

@server.route('/symbols/<int:length>')
def symbols_wrapper(length):
    return  jsonify(get_symbols_pwd(length))

@server.route('/all/<int:length>')
def all_wrapper(length):
    return jsonify(all_togheter_pwd(length))


@server.route('/strings-capital/<int:length>')
def capital_wrapper(length):
    return jsonify(first_cap_letter_strings_pwd(length))

if __name__ == "__main__":
    server.run()