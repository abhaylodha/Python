########################################################################
# Program to iterate over a list and finding distance between first 
# and last same element.
########################################################################

inp=input()
#[1,2,3,4,1]

def getPosition(lst, item) :
  for index in range(len(lst)) :
    if (lst[index] == item):
      return index

def getReversePosition(lst, item) :
  for index in range(len(lst),0, -1):
    if (lst[index-1] == item):
      return index-1

lst = inp.strip("[").strip("]").split(",")
st=set(lst)
max_distance=0

for i in st:
  pos1=getPosition(lst,i)
  pos2=getReversePosition(lst,i)
  #print (i, pos1, pos2)
  distance=pos2-pos1-1
  if (max_distance < distance) :
    max_distance = distance

print(max_distance)
