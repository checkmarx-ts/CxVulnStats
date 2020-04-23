# CxVulnStats

CxVulStats is collection Native python script to fetch vulnerability statistics of a single projects OR all projects on Checkmarx CxSAST.

-------------------

# Demo
[![asciicast](https://asciinema.org/a/312487.svg)](https://asciinema.org/a/312487?autoplay=1)

-------------------

# Purpose
- These scripts are an alternative to fetch Summary data via REST API instead of the ODATA Legacy API.
- Not all ODATA Endpoints are covered here.
- Please raise an issue here for features.
- Dashboarding tools like `Splunk` or any other `dashboard` require some information on all project's vulnerabilities to observe trends.
- These cross-platform native-python scripts fetch vulnerability statistics data:
  * Vulnerability summary of a project in-scope of the user configured.
  * Vulnerability summary of all projects in-scope of the user configured.
  * ScanID, ProjectID (ID), Project Name, Number of vulnerabilities (High, Low, Medium, Information only).
  * Checkmarx Statistics calculation date.

-------------------

# Checkmarx CxSAST Version

This script has been tailored to work for CxSAST 8.9 and will work for CxSAST 9.0. Usage of plaintext password in the Configuration file may change.

-------------------
# To-Do

-------------------

# Configuration
Configuration needs to be performed in the `cx.ini` file. Below is a list of the parameters to be filled.

- Set the `https_flag = True` to enable HTTPS Connections.
- Set`host = mycheckmarx.stat.url` to match your Checkmarx CxSAST Instance.
- Set `Setusername = username` to match the designated user account to access CxSAST APIs. This may be a non-interactive service account, Interactive-Login domain-user or application user. It is recommended to use a non-interactive service account with a password rotation policy.
- Set `password = FakePasswordGoesHere` with the password of chosen user. Draw-Back is that plaintext password is stored in a configuration file. This may be altered in the [future](https://github.com/checkmarx-ts/CxVulnStats/issues/2).
- Leave this as default. `grant_type = password`
- Please do not append items to the scope unless you are aware of your goals. This default scope ensures that only Checkmarx CxSAST API is authorized for the OUAUTH2 Token `scope = sast_rest_api`
- OIDC Client ID`client_id = resource_owner_client`
- OIDC Client Secret `client_secret = 012ABCDEF-GHIJ-KLMN-OPQR-STUVWXYZZZZZ`

-------------------

# Misc.

The file is appended with all future runs to ensure that a time-line of vulnerability-detection can be established with `date-time` as first dimenion and `vulnerabilitiy severity counts` as the second dimension.

As such, this script must be run on cadence to ensure that data is polulated on continously and that the timeline is observable on `Splunk` or `equivalent dashboards`.

-------------------

# Running

1. To get vulnerability stats of a single project
```
python vulnstats.py -p "<name_of_project_on_checkmarx>"
```
2.  To get vulnerability stats of all projects
```
python vulnstats.py --all
```

-------------------

# Vulnerability Statistics Location
* v0.0.1 produces statistics to a plaintext file `CxVulnStats.txt` in the user's home directory
