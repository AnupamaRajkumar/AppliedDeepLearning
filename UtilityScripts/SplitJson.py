#split the single json into 2 based on id 
#Json format used as per the kaggle simpsons dataset https://www.kaggle.com/mlwhiz/simpsons-main-characters

import json
import os
import itertools
import numpy as np


path = 'D:\EIT_AUS_ELTE\WiSe2020_AppliedDeepLearning'
os.chdir(path)
print(os.getcwd())

fileName = 'instances.json'

#read the json file
with open(fileName, 'r') as f1:
    data = json.load(f1)

recordTrain = {}
recordTest = {}
#info
infoObj = {
        "year"          : 2020,
        "version"       : "1.0",
        "description"   : "SimpsonsInstanceSegmentation COCO Dataset",
        "contributor"   : "HyperLabel",
        "url"           : "https://www.hyperlabel.com",
        "date_created"  : "2020/9/19"
}
recordTrain["info"] = infoObj
recordTest["info"] = infoObj

#licenses
licenses =  {
        "url"           : "https://creativecommons.org/licenses/by/2.0/",
        "id"            : 2,
        "name"          : "Attribution License"
}
recordTrain["licenses"] = licenses
recordTest["licenses"] = licenses


#images
imgObjTrain = []
imgObjTest = []
for i in data['images']:
    mult = i['id']%81
    fileName = i["file_name"]
    fileName = fileName.replace("\\", "//")
    obj = {
            "file_name" : fileName,
            "image_id"  : i["id"],
            "height"    : i["height"],
            "width"     : i["width"],
        }
    if (mult == 0 or mult < 73):
        imgObjTrain.append(obj)
    else:
        imgObjTest.append(obj)
recordTrain["images"] = imgObjTrain
recordTest["images"] = imgObjTest

#annotations
annoObjTrain = []
annoObjTest = []
for a in data['annotations']:
    mult = a['id']%81
    obj = {
        "image_id"      :   a['id'],
        "bbox"          :   a["bbox"],
        "segmentation"  :   a["segmentation"],
        "category_id"   :   a["category_id"] - 1,
        "iscrowd"       :   a["iscrowd"],
    }
    if (mult == 0 or mult < 73):
        annoObjTrain.append(obj)
    else:
        annoObjTest.append(obj)
recordTrain["annotations"] = annoObjTrain
recordTest["annotations"] = annoObjTest

#categories
catObj = []
for c in data['categories']:
    obj = {
        "category_id"   :   c["id"],
        "category_name" :   c["name"],
    }
    catObj.append(obj)
recordTrain["categories"] = catObj
recordTest["categories"] = catObj

with open('trainset.json', 'a+') as trainFile:
    json.dump(recordTrain, trainFile)
with open('testset.json', 'a+') as testFile:
    json.dump(recordTest, testFile)


for (i, a) in zip(data["images"], data["annotations"]):
    #print(i["id"])
    #print(a["category_id"])
    
    testObj = {}
    trainObj = {}
    mult = i['id']%81
    fileName = i["file_name"]
    fileName = fileName.replace("\\", "//")
    obj = {
            "file_name"     :   fileName,
            "image_id"      :   i["id"],
            "height"        :   i["height"],
            "width"         :   i["width"],
            "bbox"          :   a["bbox"],
            "segmentation"  :   a["segmentation"],
            "category_id"   :   a["category_id"] - 1,
            "iscrowd"       :   a["iscrowd"],
    }
    if (mult == 0 or mult < 73):
        trainObj[str(i['id'])] = obj
        with open('trainset1.json', 'a+') as trainFile:
            json.dump(trainObj, trainFile)
    else:
        testObj[str(i['id'])] = obj
        with open('testset1.json', 'a+') as testFile:
            json.dump(testObj, testFile)

# catObj = []
# for c in data['categories']:
#     obj = {
#         "category_id"   :   c["id"],
#         "category_name" :   c["name"],
#     }
#     catObj.append(obj)
# recordTrain["categories"] = catObj
# recordTest["categories"] = catObj

# with open('trainset1.json', 'a+') as trainFile:
#     json.dump(recordTrain, trainFile)
# with open('testset1.json', 'a+') as testFile:
#     json.dump(recordTest, testFile)


#for d in dataTest:
#    print(d)

for a in data["annotations"]:
    for s in a["segmentation"]:
        arr = s
        count = 0
        px = []
        py = []
        for i in arr:
            if(count%2 == 0):
                px.append(i)
            else:
                py.append(i)
            count = count + 1  
    poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)] 
    poly = [p for x in poly for p in x]
    print(poly)



    



