import json

id_list = []

with open('json.fake-data.json') as json_file:
    data = json.load(json_file)

    #print(data) #1
    
    # 2 print(data[0]['name']) # 0 star for 1 i python sprak
    #print(data[0]['email'])
    #print(data[0]['campany'])

# 3 om man vill att far alla info for denna person
    name = (data[0]['name']) 
    email = (data[0]['email'])
    campany = (data[0]['campany'])


    id = {
        'name': name,
        'email': email,
        'campany': campany
    }

    print(id)


       

   


        
    

    