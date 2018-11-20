import re
import json
import shutil
import os



class Resources(object):
    """Provides tools for using resources in Resources directory"""
    
    url_pattern = re.compile("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")

    def __init__(self):
        """Calls self.refresh to make self.dictionary available."""
        self.resources = {}
        self.load_file()

    def load_file(self):
        """Sets self.dictionary to current resource information
        {'resource_title': [urls]}.
        """
        with open("resources.json", "r") as resource_file:
            self.resources = json.loads(resource_file.read())
        
    def save_file(self):
        shutil.copyfile("resources.json", "resources_backup.json")
        with open('resources.json', 'w') as outfile:
            json.dump(self.resources, outfile)

    def add_url(self, target, url) -> bool:
        """Adds {url} to existing {target} file.
        Creates a backup of {target} in Backups directory.
        Raises FileNotFoundError if {target} does not point to an existing file.
        """
        target = target.lower()
        # does not add malformed URLs
        if not re.search(Resources.url_pattern, url):
            return False

        # trying to add a url for a target that does not exist - creates empty
        if target not in self.resources:
            self.resources[target] = []

        # does not add direct duplicates
        if url in self.resources[target]:
            return False


        self.resources[target].append(url)

        self.save_file()
        return True

    def restore(self):
        """ Restore database with its backup """
        os.remove("resources.json")
        shutil.move("resources_backup.json", "resources.json")
        self.load_file()

    def get_urls(self, target):
        return self.resources.get(target.lower(), [])