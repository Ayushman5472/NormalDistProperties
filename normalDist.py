import plotly.express as px
import random
import statistics 
import plotly.figure_factory as ff  
import plotly.graph_objects as go

diceResults = []
for i in range (0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceSum = dice1 + dice2
    diceResults.append(float(diceSum))

mean = sum(diceResults)/len(diceResults)
#print(mean)

standardDeviation = statistics.stdev(diceResults)
#print(standardDeviation)

median = statistics.median(diceResults)
#print(median)

mode = statistics.mode(diceResults)
#print(mode)

FirstPropertyStart = mean - standardDeviation
FirstPropertyEnd = mean + standardDeviation
#print(FirstPropertyStart)
#print(FirstPropertyEnd) 
list_firstDeviation = [result for result in diceResults if result>FirstPropertyStart and result<FirstPropertyEnd]
percentage = "{}% of Data Lies within First Standard Deviation".format(len(list_firstDeviation)*100/len(diceResults))
#print(percentage)

SecondDeviationStart = mean- 2*standardDeviation
SecondDeviationEnd = mean + 2*standardDeviation

list_secondDeviation = [result for result in diceResults if result>SecondDeviationStart and result<SecondDeviationEnd]
Secondpercentage = "{}% of Data lies in Second Deviation".format(len(list_secondDeviation)*100/len(diceResults))
#print(Secondpercentage)


ThirdDeviationStart = mean - 3*standardDeviation
ThirdDeviationEnd = mean + 3*standardDeviation

list_ThirdDeviation = [result for result in diceResults if result>ThirdDeviationStart and result<ThirdDeviationEnd]
ThirdPercentage = "{}% of data lies within Third Deviation".format(len(list_ThirdDeviation)*100/len(diceResults))
#print(ThirdPercentage)

graph = ff.create_distplot([diceResults], ["Dice Results"], show_hist = False)
graph2 = graph.add_trace(go.Scatter(x = [mean, mean], y = [0.17], mode = "lines", name = "Mean line" ))
graph2.show()