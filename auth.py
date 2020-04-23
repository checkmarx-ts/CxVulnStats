"""
Author: Uday Korlimarla <Uday.Korlimarla@checkmarx.com>
Copyright (c) 2020, Checkmarx Australia.
"""
from utils import connection, str_to_json
import configparser

class PerformAuth(object):
    """
    Get Bearer Token here
    """
    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.read('cx.ini')
        
        self.auth_headers = {
            'Accept': 'application/json;v=1.0',
            'Authorization': ''
        }
        self.https_flag = False if self.config['cx']['https_flag'] == 'False' else True
        self.host = self.config['cx']['host']
 
        self.payload = None
        self.connnection = connection(https=self.https_flag, host=self.host)
        self.auth_endpoint = "/CxRestApi/auth/identity/connect/token"
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded', 'v': '0.1'}
        self.bearer_token = None
        self.set_payload()
        self.get_bearer_token()
        self.auth_headers['Authorization'] = self.bearer_token
        return self
    
    def set_payload(self):
        # pylint: disable=line-too-long
        # To-Do: Receive user/pw from Vault or ENV
        payload_params = {
            "Username": self.config['cx']['username'],
            "password": str(self.config['cx']['password']),
            "grant_type": self.config['cx']['grant_type'],
            "scope": self.config['cx']['scope'],
            "client_id": self.config['cx']['client_id'],
            "client_secret": self.config['cx']['client_secret']
        }
        self.payload = "username={0}&password={1}&grant_type={2}&scope={3}&client_id={4}&client_secret={5}".format(
            payload_params['Username'],
            payload_params['password'],
            payload_params['grant_type'],
            payload_params['scope'],
            payload_params['client_id'],
            payload_params['client_secret']
        )

    def get_bearer_token(self):
        # Make Authentication request
        self.connnection.request("POST", self.auth_endpoint, self.payload, self.headers)
        
        response = self.connnection.getresponse()
        response_data = str_to_json(response.read().decode("utf-8"))
        if not response_data.get('error'):
            self.bearer_token = "{0} {1}".format(response_data['token_type'], response_data['access_token'])
        else:
            print('[-] error', response_data['error'])
