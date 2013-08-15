class convertTypes():
    """ Determine whether we should use keyword parameter types or names. 
        Names were originally used in 10.1, but don't work for localized 
	environments, which was resolved by switching to keywords in 10.1SP1. 
	Detect our version, and do the correct one based on the version.
    """ 
    def __init__(self):
        pass
         
    def getVersion(self):
        return arcpy.GetInstallInfo['Version']

    def getSP(self):
        return arcpy.GetInstallInfo['SPNumber']


from BeautifulSoup import BeautifulSoup
f = open('listing-of-keywords.htm', 'r')
soup = BeautifulSoup(f.read())
table = soup.find('table')

types = {}
with open('res.txt', 'w') as out:
    out.write("{\n")
    for tr in table.findAll('tr')[1:]:
        (name, keyword, desc) = [p.text for p in tr.findAll('p')]
        types[name] = keyword 
        out.write("  '" + name.encode('utf8') + "': {'keyword': '" + keyword.encode('utf8') + "',  'description': '" + desc.encode('utf8') + "'},\n")
    out.write("}\n")
