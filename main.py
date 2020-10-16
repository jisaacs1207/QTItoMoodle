import os
import re
import string
answerAPattern = re.compile("<simpleChoice identifier=\"A\" fixed=\"true\">.+\"B\"")
answerBPattern = re.compile("<simpleChoice identifier=\"B\" fixed=\"true\">.+\"C\"")
answerCPattern = re.compile("<simpleChoice identifier=\"C\" fixed=\"true\">.+\"D\"")
answerDPattern = re.compile("<simpleChoice identifier=\"D\" fixed=\"true\">.+</choiceInteraction>")
answerPattern = re.compile("<value>[A-D]<\/value>")
questionPattern = re.compile("<prompt id=\"prompt\">.+</prompt>")
theAnswer = 5
cleanQuestion = ""
cleanAnswerA = ""
cleanAnswerB = ""
cleanAnswerC = ""
cleanAnswerD = ""
questionList = []

directory = r'/Users/joshuaisaacs/Desktop/Items16'
location = 'c:/test/temp/'
files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(directory):
   for item in f:
      if '.xml' in item:
         files_in_dir.append(os.path.join(r, item))

for item in files_in_dir:
    f = open(item, 'r')
    lines = f.readlines()
    theQuestion = '\t'.join([line.strip() for line in lines])
    foundItem = str(re.findall(answerPattern, theQuestion))
    if "<value>A</value>" in foundItem:
        theAnswer = 1
    elif "<value>B</value>" in foundItem:
        theAnswer = 2
    elif "<value>C</value>" in foundItem:
        theAnswer = 3
    elif "<value>D</value>" in foundItem:
        theAnswer = 4
    else:
        theAnswer = 5
    if theAnswer < 5:
        foundItem = str(re.findall(questionPattern, theQuestion)[0])
        foundItem = foundItem.replace("</prompt>", "")
        foundItem = foundItem.replace(">", "")
        foundItem = foundItem.replace("prompt id", "")
        foundItem = foundItem.replace("</prompt", "")
        foundItem = foundItem.replace("=\"prompt\"", "")
        foundItem = foundItem.replace("<", "")
        foundItem = foundItem.replace("&#8217;", "'")
        foundItem = foundItem.replace("&#95;", "_")
        foundItem = foundItem.replace("&#8220;", "\"")
        foundItem = foundItem.replace("&#8221;", "\"")
        foundItem = foundItem.replace("sup&#43;/sup", "+")
        foundItem = foundItem.replace("&#8211;", "-")
        foundItem = foundItem.replace("/i", "")
        if("em" in foundItem) and ("/em" in foundItem):
            foundItem = foundItem.replace("/em", "")
            foundItem = foundItem.replace("em", "")
        cleanQuestion = foundItem
        foundItem = re.findall(answerAPattern, theQuestion)
        if len(foundItem)>0:
            foundItem=foundItem[0]
        else:
            foundItem=""
        foundItem = foundItem.replace("</prompt>", "")
        foundItem = foundItem.replace(">", "")
        foundItem = foundItem.replace("prompt id", "")
        foundItem = foundItem.replace("</prompt", "")
        foundItem = foundItem.replace("=\"prompt\"", "")
        foundItem = foundItem.replace("<", "")
        foundItem = foundItem.replace("&#8217;", "'")
        foundItem = foundItem.replace("&#95;", "_")
        foundItem = foundItem.replace("&#8220;", "\"")
        foundItem = foundItem.replace("&#8211;", "-")
        foundItem = foundItem.replace("&#8221;", "\"")
        foundItem = foundItem.replace("/i", "")
        foundItem = foundItem.replace("simpleChoice identifier=\"A\" fixed=\"true\"", "")
        foundItem = foundItem.replace("	/simpleChoice	simpleChoice identifier=\"B\"", "")
        foundItem = foundItem.replace("sup&#43;/sup", "+")
        foundItem = foundItem.replace("&#246;", "ö")
        if ("em" in foundItem) and ("/em" in foundItem):
            foundItem = foundItem.replace("/em", "")
            foundItem = foundItem.replace("em", "")
        cleanAnswerA = foundItem

        foundItem = re.findall(answerBPattern, theQuestion)
        if len(foundItem) > 0:
            foundItem = foundItem[0]
        else:
            foundItem = ""
        foundItem = foundItem.replace("</prompt>", "")
        foundItem = foundItem.replace(">", "")
        foundItem = foundItem.replace("prompt id", "")
        foundItem = foundItem.replace("</prompt", "")
        foundItem = foundItem.replace("=\"prompt\"", "")
        foundItem = foundItem.replace("&#8211;", "-")
        foundItem = foundItem.replace("<", "")
        foundItem = foundItem.replace("&#8217;", "'")
        foundItem = foundItem.replace("&#95;", "_")
        foundItem = foundItem.replace("&#8220;", "\"")
        foundItem = foundItem.replace("&#8221;", "\"")
        foundItem = foundItem.replace("/i", "")
        foundItem = foundItem.replace("simpleChoice identifier=\"B\" fixed=\"true\"", "")
        foundItem = foundItem.replace("	/simpleChoice	simpleChoice identifier=\"C\"", "")
        foundItem = foundItem.replace("sup&#43;/sup", "+")
        foundItem = foundItem.replace("&#246;", "ö")
        if ("em" in foundItem) and ("/em" in foundItem):
            foundItem = foundItem.replace("/em", "")
            foundItem = foundItem.replace("em", "")
        cleanAnswerB = foundItem

        foundItem = re.findall(answerCPattern, theQuestion)
        if len(foundItem) > 0:
            foundItem = foundItem[0]
        else:
            foundItem = ""
        foundItem = foundItem.replace("</prompt>", "")
        foundItem = foundItem.replace(">", "")
        foundItem = foundItem.replace("prompt id", "")
        foundItem = foundItem.replace("</prompt", "")
        foundItem = foundItem.replace("=\"prompt\"", "")
        foundItem = foundItem.replace("&#8211;", "-")
        foundItem = foundItem.replace("<", "")
        foundItem = foundItem.replace("&#8217;", "'")
        foundItem = foundItem.replace("&#95;", "_")
        foundItem = foundItem.replace("&#8220;", "\"")
        foundItem = foundItem.replace("&#8221;", "\"")
        foundItem = foundItem.replace("/i", "")
        foundItem = foundItem.replace("simpleChoice identifier=\"C\" fixed=\"true\"", "")
        foundItem = foundItem.replace("	/simpleChoice	simpleChoice identifier=\"D\"", "")
        foundItem = foundItem.replace("sup&#43;/sup", "+")
        foundItem = foundItem.replace("&#246;", "ö")
        if ("em" in foundItem) and ("/em" in foundItem):
            foundItem = foundItem.replace("/em", "")
            foundItem = foundItem.replace("em", "")
        cleanAnswerC = foundItem

        foundItem = re.findall(answerDPattern, theQuestion)
        if len(foundItem) > 0:
            foundItem = foundItem[0]
        else:
            foundItem = ""
        foundItem = foundItem.replace("</prompt>", "")
        foundItem = foundItem.replace(">", "")
        foundItem = foundItem.replace("prompt id", "")
        foundItem = foundItem.replace("</prompt", "")
        foundItem = foundItem.replace("=\"prompt\"", "")
        foundItem = foundItem.replace("&#8211;", "-")
        foundItem = foundItem.replace("<", "")
        foundItem = foundItem.replace("&#8217;", "'")
        foundItem = foundItem.replace("&#95;", "_")
        foundItem = foundItem.replace("&#8220;", "\"")
        foundItem = foundItem.replace("&#8221;", "\"")
        foundItem = foundItem.replace("/i", "")
        foundItem = foundItem.replace("simpleChoice identifier=\"D\" fixed=\"true\"", "")
        foundItem = foundItem.replace("	/simpleChoice", "")
        foundItem = foundItem.replace("&#246;", "ö")
        foundItem = foundItem.replace("	/choiceInteraction", "")
        foundItem = foundItem.replace("sup&#43;/sup", "+")
        if ("em" in foundItem) and ("/em" in foundItem):
            foundItem = foundItem.replace("/em", "")
            foundItem = foundItem.replace("em", "")
        cleanAnswerD = foundItem

        cleanQuestion = str(cleanQuestion.strip())
        cleanAnswerA = str(cleanAnswerA.strip())
        cleanAnswerB = str(cleanAnswerB.strip())
        cleanAnswerC = str(cleanAnswerC.strip())
        cleanAnswerD = str(cleanAnswerD.strip())

        if(theAnswer==1):
            cleanAnswerA = "*" + cleanAnswerA
        elif (theAnswer == 2):
            cleanAnswerB = "*" + cleanAnswerB
        elif (theAnswer == 3):
            cleanAnswerC = "*" + cleanAnswerC
        elif (theAnswer == 4):
            cleanAnswerD = "*" + cleanAnswerD

        questionList.append(cleanQuestion)
        questionList.append(cleanAnswerA)
        questionList.append(cleanAnswerB)
        questionList.append(cleanAnswerC)
        questionList.append(cleanAnswerD)
        questionList.append("\r")

        outF = open("moodleOut.txt", "w")
        for line in questionList:
            outF.write(line)
            outF.write("\n")
        outF.close()