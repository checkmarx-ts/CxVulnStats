"""
Author: Uday Korlimarla <Uday.Korlimarla@checkmarx.com>
Copyright (c) 2020, Checkmarx Australia.
"""
from projects import GetProject
from utils import connection, str_to_json


class ScanDetails(GetProject):
    def __init__(self):
        super().__init__()
        self.projects_scans = None
        self.current_project_scan_ids = list()
        self.stats_summary = list()

        for project in self.projects:
            self.current_project_id = project['id']
            self.set_current_project_by_id(project['id'])
            self.get_projects_scans()
            self.get_current_project_scan_ids()
            self.get_current_project_scan_statistics()
            
    def get_projects_scans(self):
        self.connection = connection(self.https_flag, self.host)
        self.connection.request("GET", "/cxrestapi/sast/scans", headers=self.auth_headers)
        res = self.connection.getresponse()
        data = res.read()
        self.projects_scans = str_to_json(data.decode("utf-8"))
    
    def get_current_project_scan_ids(self):
        # Filter to get All scan IDs of a specific project in context
        self.current_project_scan_ids = [{'scan_id': scan['id']} for scan in self.projects_scans if scan['project']['id'] ==self.current_project_id]
    
    def get_current_project_scan_statistics(self):
        self.connection = connection(self.https_flag, self.host)
        for scan_id in self.current_project_scan_ids:   
            rs_endpoint = "/cxrestapi/sast/scans/{0}/resultsStatistics".format(scan_id['scan_id'])
            self.connection.request("GET", rs_endpoint, headers=self.auth_headers)
            res = self.connection.getresponse()
            data = res.read()
            result = str_to_json(data.decode("utf-8"))
            result['id'], result['name'], result['scan_id'] = self.current_project_id, self.current_project_name, scan_id['scan_id']
            self.stats_summary.append(result)
