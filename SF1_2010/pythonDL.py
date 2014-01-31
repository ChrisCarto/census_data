import urllib2, urlparse

censusURL = r'http://www2.census.gov/geo/tiger/TIGER2013/ROADS'

def buildFilesToDownload(inURL):
	myArray = []
	for item in urllib2.urlopen(inURL).readlines():
		if '.zip' in item:
			myArray.append(urlparse.urljoin(censusURL, str(item.split('href="')[1].split('.zip')[0]) + ".zip"))
	print len(myArray)
	print myArray

buildFilesToDownload(censusURL)