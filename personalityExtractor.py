from watson_developer_cloud import PersonalityInsightsV3
from os.path import join, dirname
import json

def writeToJSONFile(fileName, data):
    filePathNameWExt = 'data/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def getPersonalityTraits(text):
	personality_insights = PersonalityInsightsV3(
	    version='2017-10-13',
	    iam_apikey='swNCFlkcHlcaXRJOghDmBlNJ6RqA8hV8XI7GCIDKpVgu',
	    url='https://gateway.watsonplatform.net/personality-insights/api'
	)

	profile = personality_insights.profile(
		text,
	    content_type='text/plain',
	    raw_scores=True
	    ).get_result()

	writeToJSONFile("rawData", profile)
	#print(json.dumps(profile, indent=2))
	return profile

def findTraits(trait):
	resultValues = {}
	for i in range(0,len(trait)):
		resultValues[trait[i]["name"]] = trait[i]["percentile"]
	with open('data/values.json', 'w') as fp:
		json.dump(resultValues,fp)
	return resultValues

def loadText(fileName):
	reader = open(fileName, "r", encoding="utf8")
	return reader.read()

# INPUT: essay.txt in a sub folder called data
# OUTPUT: A JSON file named values.json in the same sub folder with all of the personality values

if __name__== "__main__":
	text = loadText("data/essay1.txt")
	profile = getPersonalityTraits(text)
	values = findTraits(profile["personality"])
