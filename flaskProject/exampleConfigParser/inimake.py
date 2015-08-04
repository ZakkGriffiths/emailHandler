#!/usr/bin/env python
import ConfigParser

cfgfile = open('/Users/alexbrown/Zakk/emailHandler/flaskProject/testing/ini.ini', 'w')

Config = ConfigParser.ConfigParser()
Config.add_section('Person')
Config.set('Person', 'HasEyes', True)
Config.set('Person', 'Age', 50)
Config.write(cfgfile)
cfgfile.close()
