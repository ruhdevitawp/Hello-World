list_topic =[{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0,1]},
             {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
             ]

dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                 1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                 2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                 }

def show_topic(a,b):
    print('----Fungsi "show_topic" dijalankan----')
    for x in range (len(list_topic)):
        print('\n')
        print("Title: ",list_topic[x]['Title'])
        print("Description: ",list_topic[x]['Description'])
        print("List Activity: ",'\n'"ID",'\t',"| Title",'\t\t',"| Type",'\t',"| Description")
        print("-----------------------------------------------------------------------")
        for i in list_topic[x]['Activities']:
            print(i,'\t',"|",dict_activity[i]["Title"],'\t',"|",dict_activity[i]["Type"],'\t',"|",dict_activity[i]["Description"])  

show_topic(list_topic, dict_activity)
