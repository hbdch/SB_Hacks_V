# Takes a person's personality values and compare it to a dictionary of company personality values.
# Dictionary wit keys as company names
# Creates a file called results.json in the data folder with an array of the top 5 company names
import json
import operator

def loadJSONData(filename):
	data = open(filename).read()
	return json.loads(data)

def compareData(traits, companies):
	companyScores = {}	
	for company in companies.keys():
		score = 0
		for trait in traits.keys():
			score += (companies[company][trait] - traits[trait])**2
		companyScores[company] = score
	sortedScores = sorted(companyScores.items(), key = operator.itemgetter(1))
	return sortedScores

def writeToJSONFile(fileName, data):
    filePathNameWExt = 'data/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def saveResults(results):
	topFive = []
	for i in range(0,5):
		if i >= len(results):
			break
		topFive.append(results[i][0])
	writeToJSONFile("results", topFive)

if __name__ == "__main__":
	personalityTraits = loadJSONData("data/values.json")
	companies = loadJSONData("data/companies.json")
	results = compareData(personalityTraits, companies)
	saveResults(results)