import shapefile
import matplotlib.pyplot as plt
import numpy as np

sf=shapefile.Reader("H:\\Scheduling\\GeoData\\Michigan2017.shp")

print(sf)

fields=sf.fields

print(fields)

shapes=sf.shapes()
print(shapes)


for name in dir(shapes[3]):
     if not name.startswith('_'):
        print(name)

print(shapes[0].points)
print(shapes[0].parts)
print(shapes[0].shapeTypeName)

count=0

for shapeRec in sf.iterShapeRecords():
    for shapeRecname in dir(shapeRec):
        if not shapeRecname.startswith('_'):
            pass
            #print('shapeRecname=',shapeRecname)
    #break
    #print(shapeRec.record.IRI)
    #print(shapeRec.shape.points)
    shapeRec.shape.points = np.array(shapeRec.shape.points)
    #print(shapeRec.shape.points)
    if shapeRec.record.IRI == 0:
        #print("IRI not recorded")
        shapeRec.record.IRI==0
    elif shapeRec.record.IRI > 0 and  shapeRec.record.IRI <=100:
        #print("IRI is good")
        shapeRec.record.IRI=1
        #print(shapeRec.record.IRI)
    elif shapeRec.record.IRI > 100 and  shapeRec.record.IRI <=200:
        #print("IRI is fair")
        shapeRec.record.IRI=2
    else:
        #print("IRI is bad")
        shapeRec.record.IRI=3

    cdict = {0: 'grey', 1: 'green', 2: 'yellow', 3:'red'}
    try:
        plt.plot(shapeRec.shape.points[:,0],shapeRec.shape.points[:,1], c = cdict[shapeRec.record.IRI])
    except:
        pass

    count=count+1
    if count==20000:
        break
    percent = count / 187418 *100
    print("percent=", percent)


plt.show()
   # break






