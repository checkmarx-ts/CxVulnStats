"""
Author: Uday Korlimarla <Uday.Korlimarla@checkmarx.com>
Copyright (c) 2020, Checkmarx Australia.
"""
import argparse
from pathlib import Path
from scans import ScanDetails


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project", help="To get Vulnerability stats of a prject, type project='project_name'", type=str)
parser.add_argument("--all", help="Get vulnerability stats of all projects in User's scope", action="store_true")
args = parser.parse_args()

class VulnStats(ScanDetails):
    def __init__(self):
        super().__init__()
        self.stats_file =  Path.home().joinpath("CxVulnStats.txt")
    def __enter__(self):
        self.stats_file_handle = open(self.stats_file, 'a')
        return self
    
    def __exit__(self, type, value, tb):
        self.stats_file_handle.close()
        return

if __name__ == "__main__":
    if args.project or args.all:
        with VulnStats() as vuln_stats:

            for vuln_stat in vuln_stats.stats_summary:
                if args.all:
                    vuln_stats.stats_file_handle.writelines(str(vuln_stat))
                    vuln_stats.stats_file_handle.write("\n")

                elif args.project and vuln_stat['name'].lower() == args.project.lower():
                    vuln_stats.stats_file_handle.write(str(vuln_stat))
                    vuln_stats.stats_file_handle.write("\n")
