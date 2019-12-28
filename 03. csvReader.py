import csv
import os

with open(os.path.dirname(os.path.abspath(__file__)) + '\\mpg.csv') as csvFile :
    mpg = list(csv.DictReader(csvFile))

print(mpg[:1])

print(len(mpg))

print(mpg[0].keys())

print('%.2f' %(sum(float(d['cty']) for d in mpg) / len(mpg)))

print('%.2f' %(sum(float(d['hwy']) for d in mpg) / len(mpg)))

cylinders = set(d['cyl'] for d in mpg)

print(cylinders)

cTypeMpgByCyl = []

for c in cylinders :
    submpg = 0
    cyltypecount = 0
    for d in mpg :
        if d['cyl'] == c :
            submpg += float(d['cty'])
            cyltypecount += 1
    cTypeMpgByCyl.append((c, submpg / cyltypecount))

cTypeMpgByCyl.sort(key = lambda x : x[0])

print(cTypeMpgByCyl)

vehicleClasses = set(d['class'] for d in mpg)

hwayMpgByClass = []

for c in vehicleClasses :
    submpg = 0
    vClassCount = 0
    for d in mpg :
        if d['class'] == c :
            submpg += float(d['hwy'])
            vClassCount += 1
    hwayMpgByClass.append((c, submpg / vClassCount))

hwayMpgByClass.sort(key = lambda x : x[1])

print(hwayMpgByClass)
