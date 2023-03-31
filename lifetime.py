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
    if "ActivityTaskManager: START u0" in content[i]:
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
        #print(app_name)
        #print(content[i])
        dict[numar_aplicatii] = aplicatie

for i in range(0, len(content)):
    if "Layer: Destroyed ActivityRecord" in content[i]:
        end_time = ""
        app_name = ""
        for j in range(0,17):
            end_time = end_time + content[i][j]
        x = content[i].find("com")
        while content[i][x] != "}" and content[i][x] != "/":
            app_name = app_name + content[i][x]
            x = x + 1
        for value in dict:
            if dict[value]['app_name'] == app_name:
                dict[value]['end_time'] = end_time
                #print(dict[value]['app_name'])
    
for value in dict:
    print(dict[value])



        
        #print(content[i])
        
        
'''
La final codul trebuie pus pe Github. O sa va rog sa va creeati un cont si facem upload acolo.

Cat despre activitatea in decursul saptamanii viitoare:
- o sa mai planificăm ședințe semi-adhoc pentru task-urile din Jira, unde sa participam cu toții la analiză si rezolvare
- in daily de dimineață căutăm un slot de timp favorabil pentru "adunarea ad-hoc"
- tot in daily o sa facem si o sesiune de 'analysis review' pentru un set de teste care au avut rezultate "failed", astfel impreuna putem dezbate si analiza mai multe lead-uri către un root-cause. 

Daca exista sau apar nelămuriri, nu ezitați sa spuneți :D'''
