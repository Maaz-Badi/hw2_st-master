import math
"""
# INSTRUCTIONS >> DO NOT MODIFY EXISTING CODE USE the FUNCTIONS MENTIONED IN THE FILE 
# YOU CAN CREATE YOUR OWN FUNCTIONS IF NEEDED

#Takes size as Input
#Returns Empty hast table of 'size'
#DO NOT MODIFY THIS CODE
"""
def create_hashtable(size): # returns list of dictionaries
    htable=[{}]*size
    for i in range(size):
        htable[i]={"ID": None,
                   "DATA": None}    
    return htable


"""
#Takes Existing hashtable, size and a bool indicating wether to increase or decrease the size
#Returns a Tuple Containing new Hash Table and its New Size (Hashtable,newsize)
"""
def resize_hashtable(hashtable,size,increase):
    if increase == True:
        n = size*2
        prime = False
        p = n  
        while prime == False:
            p += 1
            is_prime = True
            for i in range(2, int(math.sqrt(p)) + 1):
                if p % i == 0:
                    is_prime = False
                    break
            prime = is_prime
    else:
        n = size// 2
        prime = False
        p = n  
        while prime == False:
            p += 1
            is_prime = True
            for i in range(2, int(math.sqrt(p)) + 1):
                if p % i == 0:
                    is_prime = False
                    break
            prime = is_prime
    
    if p <7:
        return hashtable
    new_hash = create_hashtable(p)
    for i in range(size):
        new_hash[i] == hashtable[i]

    hashtable = new_hash

    return (hashtable,p)

"""
#Takes Key and size as parameters
#Returns Original address of type(int) for the Key using the Hash Function Mentioned in the Document
"""
def hash_function(key,size):
    sum = 0
    for i in key:
        sum +=ord(i)

    sum = sum >> 4
    address = sum%size
    return address

"""
##Takes Key , OldAddress  and size as parameters
#Returns new address of type(int) for the Key using the Key Offset method Mentioned in the Document
"""
def collision_resolver(key,oldAddress,size):
    sum = 0
    for i in key:
        sum +=ord(i)

    offset = sum//size
    address = (offset+oldAddress)%size

    return address

"""
#Takes hashtable, key, data and size and Insert key and Data into the Hash Table 
# After Insertion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable and its Size as a Tuple (hashtable,size)
"""
def put(hashtable,key, data,size):
    address = hash_function(key,size)
    if hashtable[address]["ID"] == None:
        hashtable[address]["ID"] = key
        hashtable[address]['DATA'] = data
    # else:
        # newaddress = collision_resolver(key, address,size)
        # put(hashtable,key,data,size)


        

    

  
"""
#Takes hashtable and size as parameters 
# Returns load factor of type float   
"""
def loadFactor(hashtable,size):
    count = 0
    for i in hashtable:
        if (type(i) == dict) or (i == "#"):
            count += 1
    
    return ((count/len(hashtable)*100))

"""
#Takes in hash table, key, Name of the Column to be updated, 
# size of hash table, Collision Path and Operation Number as Parameters
#Searches for the key in hashtable and update the Column Name of the hashtable also updates the collision path of the key
#Returns Nothing
"""
def Update(hashtable,key, columnName, size,collision_path,opNumber):
    pass

"""        
# Update the Column Name of the hashtable founf at Index
#Returns Nothing
"""
def UpdateAtIndex(hashtable,index,columnName):
  pass
    
"""   
#Takes hash table, key, size , Collision path and Operation Number as parameters
# Searches for the key in Hash table update the Collision path and 
#If key is found returns a Tuple Containing 'DATA' part of the Hash table and the index of the key  
# Return format -> (hashtable[index]['DATA],index)  
#If key is not Found return (None,None)
"""
def get(hashtable,key,size,collision_path,opNumber):
    pass


"""
#Takes hashtable, key, size , Collision path and operation Number 
# Delete key and Data from the Hash Table 
# After deletion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable
""" 
def delete(hashtable, key, size,collision_path,opNumber):
    pass