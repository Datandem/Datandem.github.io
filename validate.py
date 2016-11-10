#!/usr/bin/python

import sys
from swagger_spec_validator import validate_spec_url

if len(sys.argv) > 1:
  url = sys.argv[1]
else:
  print "URL to JSON file required"

#validate_spec_url('file:///Users/aj/Sources/Datandem/Datandem.github.io/api/swagger.json')
validate_spec_url(url)
