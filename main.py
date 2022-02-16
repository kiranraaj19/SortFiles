import os, time, shutil

#get current date and time of file created
c_t = lambda x: time.ctime(os.path.getmtime(x))


#current directory
curr_path = os.path.dirname(os.path.abspath(__file__))

#files names
files = os.listdir(curr_path)

#find different month and year for folder names
folders = []
for x in files:
    date = c_t(curr_path+"/"+x)
    date = date.split(" ")
    date = [x for x in date if x!=""]
    month = date[1]
    year = date[4]
    folder_name = month + " " + year 
    if folder_name not in folders:
        folders.append(folder_name)
        os.mkdir(folder_name)
        shutil.move(curr_path+"/"+x,curr_path+"/"+folder_name+"/"+x)
    else:
        shutil.move(curr_path+"/"+x,curr_path+"/"+folder_name+"/"+x)

