#!/usr/bin/python3

ZONE_TPL = """; {domainname}
@ 100 IN SOA ffmuc.t0biii.de. {hostmastermail} (
     {serial:010d}  ; Serial
     120         ; Refresh
     60          ; Retry
     240         ; Expire
     120  )      ; Minimum

@                                        IN NS      ns1.ffmuc.t0biii.de.
ns1					 IN A       207.180.207.34
next                                     IN CNAME   ffmuc.t0biii.de.
"""
LINE_TPL = """{name:<40} IN {type:<7} {data}"""

DOMAIN = "ffmuc.t0biii.de"

# hostnames which aren't allowed (for example next-node)
NOTALLOWED = ["next", "ns1"]

# dots in the part before the @ need to be escaped: . becomes \.
HOSTMASTERMAIL = "hostmaster@t0biii.de"

# url from where to download the meshviewer.json
MESHVIEWERJSON_URL = "https://map.ffmuc.net/data/meshviewer.json"

# local path, only used if MESHVIEWERJSONURL is empty
MESHVIEWERJSON_LOCAL = "/opt/docker-bind/meshviewer.json"

GETWARNINGS = True
