"""
Author: Uday Korlimarla <Uday.Korlimarla@checkmarx.com>
Copyright (c) 2020, Checkmarx Australia.
"""
from auth import PerformAuth
from utils import connection, str_to_json


class GetProject(PerformAuth):
    def __init__(self):
      super().__init__()
      self.list_project_ep = '/cxrestapi/projects'
      self.connection = None
      self.projects = None
      self.current_project_id = None,
      self.current_project_name = None,
      self.current_project_uri = None,
      self.list_all_projects()
    
    def list_all_projects(self):
      self.connection = connection(self.https_flag, self.host)
      self.connection.request("GET", "/cxrestapi/projects", headers=self.auth_headers)
      res = self.connection.getresponse()
      data = res.read()
      self.projects = str_to_json(data.decode("utf-8"))

    def get_project_id_by_name(self, project_name):
      self.current_project_id = [{'id': project['id'], 'name': project['name']} for project in self.projects]

    def set_current_project_by_id(self, id):
      result = [{'id': project['id'], 'name': project['name']} for project in self.projects if id == project['id']][0]
      self.current_project_id, self.current_project_name = result['id'], result['name']
    
    def set_current_project_by_name(self, name):
      result = [{'id': project['id'], 'name': project['name'], 'uri': project['link']['uri']} for project in self.projects if name == project['name']][0]
      self.current_project_id, self.current_project_name, self.current_project_uri = result['id'], result['name'], result['uri']
