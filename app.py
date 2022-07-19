
# Otus Microservices cources
# Home Work 1
# Author Ibragimov R.M.
# Date 16.07.2022

from flask import Flask, json

status = {"status": "OK"}

api = Flask(__name__)

@api.route('/health', methods=['GET'])

def get_hw1():
  return json.dumps(status)

if __name__ == '__main__':
    api.run()