# opening the data file
file = open("logcat_applications.txt")

# reading the file as a list line by line
content = file.readlines()

# closing the file
file.close()
dict={}
numar_aplicatii = 0
for i in range(0, len(content)):
    aplicatie={}
    if "START u0" in content[i]:
        numar_aplicatii = numar_aplicatii + 1
        x = content[i].find("cmp=") + 4
        start_time = ""
        for j in range(0,17):
            start_time = start_time + content[i][j]
        app_name=""
        while content[i][x] != "/":
            app_name = app_name + content[i][x]
            x = x + 1
        aplicatie["app_name"] = app_name
        aplicatie["start_time"] = start_time
        #print(aplicatie)
        print(app_name)
        #print(content[i])
        dict[numar_aplicatii] = aplicatie
#print(dict)
print()
for i in range(0, len(content)):
    if "Destroyed ActivityRecord" in content[i]:
        end_time = ""
        app_name = ""
        for j in range(0,17):
            end_time = end_time + content[i][j]
        x = content[i].find("com")
        while content[i][x] != "}" and content[i][x] != "/":
            app_name = app_name + content[i][x]
            x = x + 1
        print(app_name)



        
        #print(content[i])
