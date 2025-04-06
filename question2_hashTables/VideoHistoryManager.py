from VideoHistoryHashTable import *
import csv
#Takes in list of Dictionaries in format[{},{}] 
# Returns HashTable in the Format [{'ID':..,"DATA":{}}]
def create_VideoHistory(VideoRecords):
    size=7
    H = create_hashtable(size)
    for i in VideoRecords:
        key = i["Video_ID"]
        data = {
            "Video_URL": i["Video_URL"],
            "Views": i["Views"],
            "Likes": i["Likes"],
            "Dislikes": i["Dislikes"]}
        H,size = put(H,key,data,size)
    return H

        

    
        
    
    
#Takes as input the Hashtable and Name of Operation file 
# Returns a Tuple with two items 
#   1. collision Path in the format {1:[],2:[]} where the keys are the Operation number
#   2. Final HashTable After All Operations performed.
def perform_Operations(H,operationFile):
    collision_path = {}
    size = len(H)
    with open(operationFile, mode ='r')as file:
        csvFile = csv.reader(file)
        for opNumber, lines in enumerate(csvFile, start=1):
            R = lines[0].split( )
            operation = R[0]
            data = R[1].split(";")
            if operation == "Like":
                key = data[0]
                Update(H,key,"Likes",size,collision_path,opNumber)
            elif operation == "Dislike":
                key = data[0]
                Update(H,key,"Dislikes",size,collision_path,opNumber)
            elif operation == "Delete":
                key = data[0]
                collision_path[opNumber] = []
                H, size = delete(H, key, size, collision_path, opNumber)
            elif operation == "Watch":
                key = data[0]
                data = {
                    "Video_URL": data[1],
                    "Views": eval(data[2]),
                    "Likes": eval(data[3]),
                    "Dislikes": eval(data[4])}
                collision_path[opNumber] = []
                Data,index = get(H,key,size,collision_path,opNumber)
                if Data != None:
                    Update(H,key,"Views",size,collision_path,opNumber)
                else:
                    H,size = put(H,key,data,size)
                    

    return(collision_path, H)






            

            
#Takes the File name is input 
# Returns the list of Dictionaries to be converted to a hashtable in format [{},{}...]

def main(filename):
    P = []
    with open(filename, mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            Q = {}
            R = lines[0].split(";")
            Q["Video_ID"] = R[0]
            Q["Video_URL"] = R[1]
            Q["Views"] = int(R[2])
            Q["Likes"] = int(R[3])
            Q["Dislikes"] = int(R[4])
            P.append(Q)
    return P
            

    
            
    

# Driver Code
VideoRecords=main('watchedVideos.csv')
# print(VideoRecords)
H=create_VideoHistory(VideoRecords)
print(H)
print(perform_Operations(H,'Operations3.csv'))