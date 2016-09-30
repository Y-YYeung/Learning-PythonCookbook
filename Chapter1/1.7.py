# 有序字典

from collections import OrderedDict
import json

orderedDict = OrderedDict()
orderedDict['foo'] = 1
orderedDict['bar'] = 2
orderedDict['spam'] = 3
orderedDict['grok'] = 4

chaosDict = {}
chaosDict['foo'] = 1
chaosDict['bar'] = 2
chaosDict['spam'] = 3
chaosDict['grok'] = 4

print("#"*4 + " Section 1 " + "#"*4)
print("ordered dict")
for key in orderedDict:
    print(key, orderedDict[key])

print("#"*4 + " Section 2 " + "#"*4)
print("chaos dict")
for key in chaosDict:
    print(key, chaosDict[key])

print("#"*4 + " Section 3 " + "#"*4)
orderedJson1 = json.dumps(orderedDict)
# orderedJson2 = json.dump(orderedDict)
print("order json dumps")
print(orderedJson1)

# print("order json dump")
# print(orderedJson2)

print("#"*4 + " Section 4 " + "#"*4)
chaosJson1 = json.dumps(chaosDict)
# chaosJson2 = json.dump(chaosDict)
print("chaos json dumps")
print(chaosJson1)

# print("chaos json dump")
# print(chaosJson2)
