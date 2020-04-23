"""
Author: Uday Korlimarla <Uday.Korlimarla@checkmarx.com>
Copyright (c) 2020, Checkmarx Australia.
"""
import http.client
import mimetypes
from json import loads
import ssl

def connection(https, host):
    conn = None
    if https:
        conn = http.client.HTTPSConnection(host, context = ssl._create_unverified_context())
    else:
        conn = http.client.HTTPConnection(host)
    
    return conn

def str_to_json(payload):
    return loads(payload)
