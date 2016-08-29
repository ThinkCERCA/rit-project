# ThinkCERCA RIT Score Calculator
#
# Jason Li - 7.26.15
#
# Calculate projected scores for inputs, spring to spring
#
import sys
#import numpy as np
import csv
import math
#############################
#  defining methods         #
#############################

#Input could be grade level of reading, instead of actual RIT score
#####
#######
#########
###########

gradeInput = int(sys.argv[1])
ritInput = int(sys.argv[2])

def read_csv(filename):
    '''
    Read data from the specified file, specifically csv. Output list of lists [Grade, Begin, Mid, End, Diff]

    Inputs:
      filename: name of the file to be read

    Returns:
      (list of strings, 2D array)
    '''

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        standardRIT = list(reader)

    while len(standardRIT) > 10:
        del(standardRIT[-1])

    for x in standardRIT:
        while len(x) > 5:
            del(x[-1])

    finalRIT = [standardRIT[0]]

    for group in standardRIT[1:]:
        finalRIT.append(list(map(float, group)))

    return finalRIT

def round(number):
    b = (math.ceil(number*1000)/1000)
    return b

def growthToYears(ritResults, dataRIT):
    '''
    Given ritResults, which include a starting and end score, compare to standardRIT and find yearly value, by increments of 0.5
    Inputs:
      ritResults (tuples), dataRIT

    Returns:
      tuple of [grade, growth amount in years]

      ritGrowth = [A, B, C]

    '''
    yearStart = 0
    yearEnd = 0
    startScore = ritResults[0]
    endScore = ritResults[1]

#Finds the grade level for starting score
    for group in dataRIT[1:]:
        if startScore >= group[3]:
            yearStart += 1
        elif startScore >=group[2]:
            yearStart += 0.5
        else: break

#Finds the grade level for ending score
    for group in dataRIT[1:]:
        if endScore >= group[3]:
            yearEnd += 1
        elif endScore >= group[2]:
            yearEnd += 0.5
        else: break

#returns the difference, AKA Growth
    return yearEnd-yearStart

def YearCalculator(resultList, dataRIT):
    yearsGrown =[0, 0, 0]

    yearsGrown[0]= growthToYears([resultList[0], resultList[1]], dataRIT)
    yearsGrown[1]= growthToYears([resultList[1], resultList[2]], dataRIT)
    yearsGrown[2]= growthToYears([resultList[2], resultList[3]], dataRIT)

    return yearsGrown

def readingLevel(score, dataRIT):
    '''
        Checks through DataRIT for the EOY score. If score is less than EOY score, we return grade of that year.
    '''
    for grade in dataRIT[1:]:
        if score < grade[3]:
            return grade[0]
        #else: return dataRIT[-1][0] #if score/reading level is too high, change grade to 11



def projectRIT(grade, score, dataRIT, ritGrowthPercents):

    growthYear1 = dataRIT[grade-2][4]*ritGrowthPercents[grade-3][1]
    growthYear2 = dataRIT[grade-1][4]*ritGrowthPercents[grade-2][1]
    growthYear3 = dataRIT[grade][4]*ritGrowthPercents[grade-1][1]

    resultsYear1 = score+growthYear1
    resultsYear2 = resultsYear1+growthYear2
    resultsYear3 = resultsYear2+growthYear3

    return [[growthYear1, growthYear2, growthYear3], [score, resultsYear1, resultsYear2, resultsYear3]] ####Added startingScore


#############################
#  def done                 #
#############################
# this is data on how much each grade should grow, percentage above the standard.
ritGrowthPercents = [[3, 1.05], [4, 1.147], [5, 1.428], [6, 1.146], [7, 1.667], [8, 1.630], [9, 1.530], [10, 1.640], [11, 1.650]]
standardRIT = read_csv("standard2015.csv")

standardRITScore = standardRIT[gradeInput-2][1]

if ritInput < standardRITScore:
    readingGrade = int(readingLevel(ritInput, standardRIT))



#print (ritInput, gradeInput, readingGrade)
#############################
#  Output Below             #
#############################

print [standardRIT[gradeInput-2][4], standardRIT[gradeInput-1][4], standardRIT[gradeInput][4]]
# (1) national averages

projectionTest = projectRIT(readingGrade, ritInput, standardRIT, ritGrowthPercents)
print [round(projectionTest[0][0]), round(projectionTest[0][1]), round(projectionTest[0][2])]
# (2) growth w ThinkCERCA

yearTest = YearCalculator(projectionTest[1], standardRIT)
print [yearTest[0], yearTest[1], yearTest[2]]
# (3) growth years

print [projectionTest[1][0], projectionTest[1][1], projectionTest[1][2], projectionTest[1][3]]
# (4) actual RIT scores with ThinkCERCA

print [standardRIT[gradeInput-2][1], standardRIT[gradeInput-1][1], standardRIT[gradeInput][1], standardRIT[gradeInput+1][1]]
# (5) actual national average RIT scores


# print ('\n', '\n')
# print ("Based on national averages, your student should grow")
# print ( standardRIT[gradeInput-2][4], "RIT points during the first year")
# print ( standardRIT[gradeInput-1][4], "RIT points between year 1 and year 2")
# print ( standardRIT[gradeInput][4], "RIT points between year 2 and year 3")
#
# print ('\n', '\n')
#
#projectionTest = projectRIT(gradeInput, ritInput, standardRIT, ritGrowthPercents)
# print ("But here's the power of ThinkCERCA: With ThinkCERCA, your student can grow up to")
# print ( round(projectionTest[0][0]), "RIT points during the first year")
# print ( round(projectionTest[0][1]), "RIT points between year 1 and year 2")
# print ( round(projectionTest[0][2]), "RIT points between year 2 and year 3")
#
# print ('\n', '\n',)
#
#yearTest = YearCalculator(projectionTest[1], standardRIT)
# print ("Translated to years of growth, this means your student is growing")
# print ( yearTest[0], "years during the first year")
# print ( yearTest[1], "years between year 1 and year 2")
# print ( yearTest[2], "years between year 2 and year 3")
