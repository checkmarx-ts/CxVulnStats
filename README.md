# About

CxVulStats is a Native python script to fetch vulnerability stats of a single projects OR all projects in the configured user's scope.

# Demo
[![asciicast](https://asciinema.org/a/312487.svg)](https://asciinema.org/a/312487?autoplay=1)

# Configuration
Configuration needs to be performed in the `cx.ini` file. Below is a list of the parameters to be filled.

```
https_flag = True
host = mycheckmarx.stat.url
username = username
password = FakePasswordGoesHere
grant_type = password
scope = sast_rest_api
client_id = resource_owner_client
client_secret = 012ABCDEF-GHIJ-KLMN-OPQR-STUVWXYZZZZZ
```

# Running

* To get vulnerability stats of a single project
```
python vulnstats.py -p "<name_of_project_on_checkmarx>"
```
* To get vulnerability stats of all projects
```
python vulnstats.py --all
```

# Vulnerability Statistics Location
* v0.0.1 produces statistics to a plaintext file `CxVulnStats.txt` in the user's home directory
