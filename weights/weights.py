import os
import csv
import matplotlib.pyplot as plt

from datetime import date



def recordweights(weight, bmi):
    with open("weights.csv", "a") as csvfile:
        today = date.today()
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([today.isoformat(), weight, bmi])
        print("Your information has been recorded.")


def calculatebmi(weight, height):
    bmi = round(float(weight), 2) / (float(height) ** 2)
    bmi = round(bmi, 2)
    if bmi > 30:
        print("You have a BMI of over 30, this is overweight.")
    return(bmi)


# Initialize the CSV file
fileexists = os.path.isfile("./weights.csv")
if fileexists is False:
    print("Unable to find weight history.")
    print("Starting new history file.")
    with open("weights.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['Date', 'Weight (KG)', 'BMI'])

fileexists = os.path.isfile("./weightscfg.csv")
if fileexists is False:
    with open("weightscfg.csv", "w") as csvfile:
        print("No config found. Starting setup!")
        print("This data will be used to understand how much weight you've lost over time.")
        firsttime = date.today()
        name = input("What's your name?: ")
        height = input("What's your height? (m): ")
        startingweight = input("What's your starting weight? (kg): ")
        bmi = calculatebmi(startingweight, height)
        recordweights(startingweight, bmi)
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([firsttime.isoformat(), name, height, startingweight, bmi])
        print("Run the program again to update your weight and see how you've progressed!")
        exit()

with open("weightscfg.csv") as csvfile:
    cfgreader = csv.reader(csvfile)
    cfg = list(cfgreader)
    row = cfg[0]
    firsttime = row[0]
    name = row[1]
    height = row[2]
    startingweight = row[3]
    firsttime = date.fromisoformat(firsttime)
    print("Config loaded.")

print(f"Welcome back {name}.")
latestweight = input("What do you weigh? (KG): ")
bmi = calculatebmi(latestweight, height)
latestweight = round(float(latestweight), 2)
print(f"{height} {latestweight} {bmi}")
recordweights(latestweight, bmi)

totalloss = float(startingweight) - float(latestweight)

print(f"You have been recording since {firsttime} and have lost {totalloss} kg!")

with open("weights.csv") as csvfile:
    weightlist = []
    datelist = []
    weightsreader = csv.reader(csvfile)
    i=0
    for row in weightsreader:
        i = i+1
        weightlist.append(row[1])
        datelist.append(row[0])
    datelist.pop(0)
    weightlist.pop(0)
    print(datelist)
    plt.plot(datelist,weightlist)
    plt.title('test')
    plt.xlabel('test')
    plt.ylabel('test')
    plt.savefig('test.png')
