import os
import csv
from datetime import date


def recordweights(weight, bmi):
    with open("weights.csv", "a") as csvfile:
        today = date.today()
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([today.isoformat(), weight, bmi])


def calculatebmi(weight, height):
    bmi = round(float(weight), 2) / (float(height) ** 2)
    bmi = round(bmi, 2)
    return(bmi)


# Initialize the CSV file
fileexists = os.path.isfile("./weights.csv")
if fileexists is False:
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
        print("Your information has been recorded.")
        print("Run the program again to update your weight and see how you've progressed!")
        exit()

with open("weightscfg.csv") as csvfile:
    cfgreader = csv.reader(csvfile)
    cfg = list(cfgreader)
    row = cfg[0]
    firsttime = row[0]
    name = row[1]
    height = row[2]
    firsttime = date.fromisoformat(firsttime)
    print("Config loaded.")

print(f"Welcome back {name}.")
latestweight = input("What do you weigh? (KG): ")
bmi = calculatebmi(latestweight, height)
latestweight = round(float(latestweight), 2)
print(f"{height} {latestweight} {bmi}")
recordweights(latestweight, bmi)

