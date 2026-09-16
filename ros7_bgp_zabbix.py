#!/usr/bin/env python3

import json
import argparse
import librouteros


parser = argparse.ArgumentParser(
    description='Monitoring MikroTik RouterOS 7 BGP in Zabbix'
)
parser.add_argument(
    'command', type = str, help = 'script operating mode (discover | status)'
)
parser.add_argument('host', type = str, help = 'device hostname or ip address')
parser.add_argument('username', type = str, help = 'device username')
parser.add_argument('password', type = str, help = 'device password')
parser.add_argument(
    '-p', '--peer', 
    metavar = '', 
    type = str, 
    help = 'peer name (onle if in status mode)'
)
args = parser.parse_args()

commands = ('discover', 'status')
command = args.command

if __name__ == '__main__':
    if command in commands:
        api = librouteros.connect(**{
            'host': args.host,
            'username': args.username,
            'password': args.password
        })
        bgp_sessions = api.path('/routing/bgp/session').select(
            librouteros.query.Key('name'), 
            librouteros.query.Key('established')
        )
        peers = {
            bgp_session['name']: bgp_session['established'] 
            for bgp_session in bgp_sessions
        }
        if command == 'discover':
            result = {
                'data': [
                    {'{#BGPPEER}': peer_name} for peer_name in peers.keys()
                ]
            }
            print(json.dumps(result, indent = 4, sort_keys = True))
        elif command == 'status':
            peer_name = args.peer
            if peer_name in peers.keys():
                if peers[peer_name]:
                    print(1)
                else:
                    print(0)
            else:
                print(0)
