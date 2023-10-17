import os
import fnmatch
import numpy
import json
import time



# ------------- PATH, VARIABLES ETC. -------------------------------------------------------------------------------- #
adhoc_path = "you/path/to/the/main_folder/where/all/subfolders/are/to_be/searched/for"

# first dict is to store key = folders and value = list of files within
first_dict = {}
# nested dict is the main dict to store key = .name and value = first_dict
nested_dict = {}


# ------------- FUNCTIONS -------------------------------------------------------------------------------------------------------- #
def timing_decorator(func):
    """
    Decorator to show how long a function took to run
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run. \n")
        return result

    return wrapper



@timing_decorator
def create_txtfile_with_all_files_from(dir_path):
    """
    dir_path: provide the inputpath in "..."

    Create a copy of the adhoc folder
    This part creates a list which is kind a copy from the ad-hoc folder with all sub-folders and files within
    """
  
    files_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            with open("file_list.txt", 'a', encoding='utf-8') as file_input:
                file_input.write(root.lower() + '//' + str(file.lower()) + '\n')



@timing_decorator
def distinct_list_of_namefiles(files_found):
    """
    files_found:    variable which stores the input which should become distinct

    Find all distinct .name files in the provided variable (files_found)
    - Split a string (here it is from path) by '/'
    - Take the last index (here a file)
    - Filter for .name file
    - Return just the distinct .name files
    """
    unique_list = [name_file.split('/')[-1] for name_file in files_found]
    return fnmatch.filter(numpy.unique(numpy.array(unique_list)), '*.name')



@timing_decorator
def proced_filelist_txt_for_distinct_output():
    """
    Code open the saved file from create_txtfile_with_all_files_from()
    to have better performance instead of re-walk the path
    """
    with open("file_list.txt", "r", encoding='utf-8') as txt_file_path_output:
        files_list = txt_file_path_output.readlines()
    # to use and access the values within the file the code bellow need it as a list
    files_list = [line.strip() for line in files_list]
    distinct_persons = distinct_list_of_namefiles(files_list)

    return distinct_persons



@timing_decorator
def create_adhoc_structure_json(distinct_list, dir_path):
    """
    distinct_persons:   the variable which contains a list of distinct values (here persons)
    dir_path:           which path/folder should be processed

    Create a nested dict like bellow with the info's from above
    Loop through all distinct .name files and create for each person a dict with their folders and files
    """
    for person in distinct_list:
        first_dict = {}
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if person.lower() in (str(file.lower())):
                    for subdir, subdirs, subfiles in os.walk(root):
                        first_dict[root + subdir.split(root)[1]] = [f for f in subfiles if not f.endswith('.name')]
        nested_dict[person] = first_dict

    # writes the output from the above to a json file.
    with open("nested_dict_output.json", 'w', encoding='utf-8') as outfile:
        json.dump(nested_dict, outfile, indent=4, ensure_ascii=False)



def delete_file_content(file_path):
    with open(file_path, "w") as file:
        pass  # Do nothing, since the file is already emptied by opening it in write mode



# ------------- MAIN: Processing ad-hoc Folder to JSON Output ------------------------------------------------------------------------ #
delete_file_content("file_list.txt")

create_txtfile_with_all_files_from(adhoc_path)

distinct_persons_list = proced_filelist_txt_for_distinct_output()

with open("name_list.txt", "w", encoding='utf-8') as txt_file_distinct_name:
    txt_file_distinct_name.writelines([item + '\n' for item in distinct_persons_list])

create_adhoc_structure_json(distinct_persons_list, adhoc_path)
# ------------- END  ---------------------------------------------------------------------------------------------------------------- #
