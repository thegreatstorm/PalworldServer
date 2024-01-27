import argparse


def argument_controller():
    # Plugins may have to been done manual has mods are different per game server.
    parser = argparse.ArgumentParser('Automate your Palworld Server!')
    parser.add_argument('--install', help='Install Palworld Server', required=False, action='store_true')
    parser.add_argument('--start', help='Run Palworld Server', required=False, action='store_true')
    parser.add_argument('--stop', help='Stop Palworld Server', required=False, action='store_true')
    parser.add_argument('--check', help='Check Running', required=False, action='store_true')
    parser.add_argument('--restart', help='Restart Palworld Server', required=False, action='store_true')
    args = parser.parse_args()
    return args