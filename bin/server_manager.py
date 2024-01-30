import os
import json
from subprocess import check_output
import re
from bin.utils.configuration_controller import config_controller
from bin.utils.rcon_controller import PalworldRcon


def run_playbook(playbook, game_server_config):
    result = json.dumps(game_server_config)
    command = "ansible-playbook {} --extra-vars '{}'".format(playbook, result)
    # print(command)
    # Run the playbook
    os.system(command)


# Make sure server_identity is simple and has no spaces.
def find_process(server_identity):
  output = check_output('ps aux | grep -ie "' + server_identity +'" | grep -v grep | awk \'{print $2}\'', shell=True)
  if len(output.split()) > 0:
      return True

  return False


def rcon_connect(server_ip, rcon_port, rcon_password):
    ## Sets up the RCON connection
    rcon_connection = PalworldRcon(server_ip, rcon_port, rcon_password)
    print("Rcon Connected. Type in exit to exit rcon.")
    while True:
        message = input("Command: ")
        if message == 'exit':
            break
        print(rcon_connection.run_command(message))
    return rcon_connection


