import os, subprocess
import glob,ast

def main():
    newest = max(glob.iglob('label/resources/*.jpg'), key=os.path.getctime)
    path_to_image = newest
    path_to_script = "./label/label.py"
    command = "./label/label.py label/resources/girl_pants.jpg"
    print ("init")
    label_dict = subprocess.check_output([path_to_script, newest])
    print ("label:dict " + label_dict)
    search_string = ""
    for i in range(3):
        if(label_dict[i] == "clothing" or label_dict[i] == "cloth"):
            continue
        else:
            search_string += label_dict[i] + "-"
    print(" Search String : " + search_string)
    return search_string

def main_1():
    newest_image = max(glob.iglob('/home/ssm/Documents/projects/djangoProjects/october/cloud-vision1/django-jquery-file-upload/media/pictures/*.jpg'), key=os.path.getctime)
    print("newest image: "+ newest_image)
    path_to_script = './label/label.py '
    command = path_to_script + newest_image
    #label_dict = subprocess.check_output([path_to_script, newest])
    shell_output = os.popen(command).read()
    print("String label returned by popen : " + shell_output)
    #search_string = ast.literal_eval(label_dict)
    #print(search_string)
    label_list = shell_output
    #print(label_list[0:-1])
    return label_list[0:-1]

#main_1()
#newest = max(glob.iglob('../django-jquery-file-upload/label/resources/*.jpg'), key=os.path.getctime)
#path_to_image = newest
#path_to_script = "./../django-jquery-file-upload/label/label.py"
#label_dict = subprocess.check_output([path_to_script, path_to_image])
#print ("label:dict " + label_dict)