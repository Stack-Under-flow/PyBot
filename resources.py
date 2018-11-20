import re
import json



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
        with open('resources.json', 'w') as outfile:
            json.dump(self.resources, outfile)

    def add_url(self, target, url):
        """Adds {url} to existing {target} file.
        Creates a backup of {target} in Backups directory.
        Raises FileNotFoundError if {target} does not point to an existing file.
        """
        # does not add malformed URLs
        if not re.search(Resources.url_pattern, url):
            return

        # trying to add a url for a target that does not exist - creates empty
        if target not in self.resources:
            self.resources[target] = []

        # does not add direct duplicates
        if url in self.resources[target]:
            return


        self.resources[target].append(url)

        self.save_file()

    # def restore(self, target):
    #     """Restores {target} with its backup."""
    #     with open(f'Backups/{target}_backup.txt') as backup_file:
    #         with open(f'Resources/{target}.txt', 'w') as target_file:
    #             target_file.write(backup_file.read())
                
    #     self.refresh()

    def get_urls(self, target):
        return self.resources.get(target, [])

def get_dictionary():
#returns a dict containing resource information
#{'resource_title': [urls]}
    resources = {}
    filenames = listdir(path='Resources')
    for filename in filenames:        
        #take first half of filename split at file descriptor        
        resource_title = filename.split('.')[0]
        urls = []
        with open(f'Resources/{filename}', 'r') as resource_file:
            for line in resource_file:
                urls.append(line.strip())
            resources[resource_title] = urls    
    return(resources)


def search_dictionary(search_term):
    #Searches through dictionary for the command passed to it
    #Returns (Keyword, related Urls)
    workingDictionary = get_dictionary()
    for name, links in workingDictionary.items():
        linkString = ""
        if name == search_term:
            for i in range(len(links)):
                linkString += (links[i] + "\n")
                final = name + " Resources:\n" + linkString
    #Returns fully formated for printing to discord
            return(final)


