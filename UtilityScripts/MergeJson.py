import json

def merge(a, b):
    "merges b into a"
    for key in b:
        if (key != "categories") and (key in a):# if key is in both a and b
           #print("\n"+key)
           a[key] = a[key]+ b[key] 
        else: # if the key is not in dict a , add it to dict a
            a.update({key:b[key]})
    return a
    
filename1 = input("Enter first json (with .json extension):")
filename2 = input("Enter second json (with .json extension):")

with open(filename1, 'r') as f1:
  data1 = json.load(f1)
#print(data1)

with open(filename2, 'r') as f2:
   data2 = json.load(f2)
#print(data2)   

#get the count of ids from first json file
count = 0
for i in data1['images']:
  if 'id':
    count = count+1
#print(count)

#get the image id count from the fust json file
imgId = 0
for i in data1['annotations']:
  id = i['image_id']
  if(id > imgId):
    imgId = id
print(imgId)

#update the count of ids of the second json file
for i in data2['images']:
 i['id'] = i['id'] + count
#print(data2)

#update the image_id of second json file
oldId = 0
newId = 0
for i in data2['annotations']:
  oldId = i['image_id']
  i['image_id'] = i['image_id'] + imgId
  newId = i['image_id']
  if(i['image_id'] == oldId):
    i['image_id'] = newId

#merge the files
with open('MergedFile.json', 'w') as f:
  data3 = merge(data1, data2)
  #print(data3)
  json.dump(data3, f)
  print("\n Files merged. Check MergedFile.json")







