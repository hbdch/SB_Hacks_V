from watson_developer_cloud import PersonalityInsightsV3
from os.path import join, dirname
import json

#list of companies
companies = {}
companies['A'] = 'earsplitting encouraging minor phobic four disgusting disagreeable fortunate handsomely valuable oval fast dull overt yummy regular dusty fearful soggy roomy classy befitting well-made unique ill-informed false interesting truculent scared guarded keen sour cumbersome unbecoming vacuous detailed superficial magnificent mushy remarkable longing unsightly awake womanly selective thinkable reflective pretty accidental solid homeless ugly tough lopsided chunky gullible lowly godly broken thoughtless wonderful thirsty fine acoustic disagreeable obnoxious warlike drab plain nice third tired subdued thankful panicky grateful like left impossible historical grandiose better grieving yellow hard outgoing supreme eatable uninterested quack spiteful fluffy pricey previous watery adventurous abrupt adhesive irritating sleepy nutritious obsequious humdrum bright frantic solid interesting cute kaput vulgar grateful ambitious silent silent terrible dizzy cloistered jobless chivalrous subdued evasive pumped talented axiomatic languid'
companies['B'] = 'minor worthless abashed royal cultured kind motionless insidious obtainable zesty fantastic insidious imminent snotty envious last permissible bright fabulous symptomatic barbarous petite ossified deranged upset confused husky scattered disastrous necessary righteous best unknown oval powerful literate halting invincible quizzical aquatic green handsome actually capricious parched infamous delicate wrong incompetent hushed necessary undesirable toothsome abnormal shrill caring maddening fascinated seemly nostalgic stiff dizzy spiffy defective afraid lowly brash encouraging hapless weak tranquil versed understood last icky gratis wary sharp necessary hospitable trashy petite knotty zany deeply first natural first purple equal lying tremendous weak freezing fluffy delicate offbeat sharp ludicrous deeply lethal colossal whimsical vivacious wealthy kaput whole earsplitting premium impossible quizzical enormous hanging bizarre erratic tranquil crazy glib moldy evanescent fabulous shrill animated special '
companies['C'] = 'chivalrous absorbing secretive rainy tame anxious optimal sore drab steep wiry goofy direful shy sturdy ceaseless chivalrous divergent ossified blue-eyed steep nutty immense disturbed immense psychedelic embarrassed huge silky freezing round wicked nosy pricey bouncy skillful three innate macabre trashy black-and-white dispensable wrathful humorous frightening rotten near deadpan long-term gullible handsome grumpy scientific screeching depressed sharp futuristic damaging longing early xenophobic juvenile panicky grubby homely lyrical awful shocking supreme third late evanescent absorbed ready chilly keen silent smart hungry flawless cruel rich yellow uneven teeny ugliest familiar abiding better wealthy testy giant gamy unwritten high-pitched violent slimy adventurous jazzy odd screeching tired gruesome uptight abortive parallel mere dirty necessary royal late talented flagrant evasive tightfisted chivalrous different cloistered scintillating superficial sophisticated cynical tasteful'
companies['D'] = 'voracious unaccountable substantial null exotic defective hypnotic creepy idiotic glamorous gaudy one malicious large tiresome illustrious faulty gainful highfalutin clammy dysfunctional fluttering cooperative chief famous shut ugly mean statuesque unkempt foolish spiffy parched cowardly creepy repulsive moaning receptive truculent outstanding short knotty grouchy mushy frequent literate living coordinated cynical depressed determined gratis moldy gigantic alert well-groomed domineering young busy ill spooky deeply ancient resolute hard pricey caring gray brown goofy needless majestic long-term lavish nippy ruthless fluffy cruel happy unequal purring cloistered alert friendly unruly satisfying clever same mean used abandoned eight nutty empty jittery purple scientific stupendous unique willing functional delightful elegant terrific torpid royal cultured imported abortive sudden gruesome wacky screeching soft animated therapeutic fabulous psychotic rhetorical glib spotty capricious slow aboard'
companies['E'] = 'physical devilish needy pleasant keen sassy polite historical erect disgusted elastic squealing dry aloof rough detailed malicious aromatic tightfisted slimy wonderful responsible near tame juvenile kaput extra-large powerful illustrious numerous selective striped skinny hurt mysterious aspiring black-and-white satisfying deadpan little exuberant long-term unkempt immense silent historical daily quirky terrible addicted dapper clear devilish tremendous calm past right nimble homeless receptive afraid gabby tender dynamic first abundant deadpan shaggy useful astonishing slow earthy fearful uneven cowardly mixed torpid insidious tightfisted sour standing alleged fine rapid luxuriant glossy pricey adjoining faithful accidental panicky safe real verdant didactic ancient aggressive unbecoming robust screeching tired gruesome uptight abortive parallel mere dirty necessary royal late talented flagrant evasive tightfisted chivalrous different cloistered scintillating superficial sophisticated cynical tasteful functional delightful elegant terrific torpid royal cultured imported abortive sudden gruesome wacky'
companies['F'] = 'enormous old-fashioned rambunctious bustling evanescent clear inquisitive minor furry third weary disgusted narrow coherent fumbling imaginary obese determined painful eatable defiant deafening ugliest responsible plant observant noxious aberrant teeny military useless clever careful wet plastic painful puzzling excited available motionless befitting abusive well-off elastic waiting lacking upbeat sparkling broad romantic internal obedient giddy worried calculating closed nervous ragged glib wonderful bawdy certain determined aware selective noisy wanting adjoining rude rightful square graceful yellow abortive trashy ruthless ambiguous instinctive lean regular bewildered distinct divergent hot future marked tasteful stupid important selfish blue aware available concerned trashy lucky eminent goofy pushy first cheerful righteous abundant mundane somber possessive womanly kind certain right economic adhesive wiggly elfin red female savory icy elderly nine public flowery disgusted merciful dark cooing gullible complex heavy broad cowardly watery tacit squealing needy awake tawdry smart unarmed nonstop upbeat wicked irritating striped talented vague staking sweltering squalid curved'
companies['G'] = 'tedious whole jaded dashing bustling empty afraid elastic likeable left aloof picayune cooing macho madly bored guarded bustling colossal confused gusty furry pumped calculating repulsive ill tender adventurous disturbed macho panicky craven furtive mysterious thundering elegant nervous rightful devilish exclusive dashing fast vigorous sparkling obtainable onerous orange wealthy able sable lopsided thick zealous spooky second-hand eminent painstaking great high-pitched shrill hellish highfalutin fixed broken adventurous torpid wretched deadpan strong accidental shaggy unequaled separate normal trite piquant colorful one squealing simplistic lazy bewildered cagey secret noiseless future adaptable graceful incandescent stereotyped annoying incredible lame humorous majestic economic last ritzy petite red fixed hulking oafish outstanding striped used offbeat hurried separate impossible silent substantial icky mature hot succinct lyrical somber military useful wrathful spicy receptive plain truthful grumpy needy loose deadpan rural youthful whispering worried hospitable innocent fluffy perpetual healthy sour powerful delirious excellent stereotyped defeated dynamic slim medical gullible purple'
companies['H'] = 'cagey hapless cuddly medical awful judicious amuck regular depressed vacuous dazzling abashed known wrathful rabid skillful energetic better wistful voracious poor bad animated demonic useful superb nappy fine puzzled luxuriant smoggy shut mature chunky ultra loutish reminiscent coherent complete large slippery scarce hesitant supreme creepy paltry unhealthy ubiquitous wiggly childlike encouraging loving half versed abject nostalgic normal long-term scarce selfish crooked famous bustling adhesive scattered quirky red bouncy spurious tedious hideous skinny thin thin silky beneficial brawny mixed unwieldy new moldy awful poor fluttering hanging chunky brawny psychedelic best exciting wrathful pretty teeny-tiny evanescent zonked watery disastrous fat deafening concerned cheerful simplistic threatening childlike grieving plausible jolly offbeat overconfident jaded macho woozy gifted insidious psychedelic evanescent spiky zippy equable ordinary tasteful ablaze verdant nervous yielding spotless nosy undesirable garrulous madly cruel left flowery jagged rough wooden whispering psychotic naughty kindly abundant used weary graceful heartbreaking yellow abject clammy'

personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    iam_apikey='NNlSpXaQCB0NFKCmhsdebwGtYJnsadq8CWPGscH2rfac',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)

#the main dictionary. Keys: company name, Value: dictionary with keys being traits and values being percentile
database = {}

#writes the json file to place
def writeToJSONFile(fileName, data):
    filePathNameWExt = 'data/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
#given name and description, will update companies dict and database dict        
def expand_data(comp_name,description):
    if comp_name not in companies.keys():
        companies[comp_name] = description;
    
    database[comp_name] = {}
    profile = personality_insights.profile(
                companies[comp_name],
                content_type = 'text/plain',
                consumption_preferences=True,
                raw_scores =True
                ).get_result()
        
    for entry in profile['personality']:
        database[comp_name][entry['name']] = entry['percentile']
            
    for entry in profile['needs']:
        database[comp_name][entry['name']] = entry['percentile']
            
    for entry in profile['values']:
        database[comp_name][entry['name']] = entry['percentile']
    

#fill the data_base with stored companies data
def initial_fill() -> dict:
    for scan in companies.keys():
        expand_data(scan,companies[scan])
    
#print out database     
def print_data(): 
    for x in database:
        print(x)
        for scan in database[x]:
            print('       ' + scan + ': ' + str(database[x][scan]))
        print()

#create a json file of the database
def get_JSON():
    writeToJSONFile('company_data',database)
        
if __name__ == '__main__':
    initial_fill()
    print_data()
    
