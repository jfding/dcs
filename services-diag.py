#!/usr/bin/env python

import os, sys
import yaml

fn = '/srv/services.yml'
try:
    fn = sys.argv[1]
except:
    pass

try:
    data = yaml.load(file(fn).read())
except:
    print 'Load file failed'
    sys.exit(1)

conflicts = []
conflict_found = False

for serv in data['Services']:
    if 'Ports' not in serv:
        continue

    name = serv['Name']
    ports = serv['Ports']

    if not os.path.isdir(name):
        print 'Warning: [%s] dir not exist' % name

    for port in ports:
        for res_port in data['ReservedPorts']:
            if port == res_port['Port']:
                print 'Warning: [%s] port <%d> conflicts with reserved port: [%s]' % (name, port, res_port['Service'])
                conflict_found = True

        if '%s:%d' % (name, port) in conflicts:
            continue

        for other_ser in data['Services']:
            if other_ser['Name'] == name or 'Ports' not in other_ser:
                continue

            for o_port in other_ser['Ports']:
                if port == o_port:
                    conflicts.append('%s:%d' % (other_ser['Name'], o_port))
                    print 'Warning: [%s] port <%d> conflicts with other service [%s]' % (name, port, other_ser['Name'])
                    conflict_found = True

if not conflict_found:
    print 'No news is good news, congrats'

