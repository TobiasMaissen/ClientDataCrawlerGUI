import fnmatch
from tkinter import *
import json
import numpy
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


file_list_path = resource_path('file_list.txt')
name_list_path = resource_path('name_list.txt')
nested_dict_path = resource_path('nested_dict_output.json')
pst_logo_path = resource_path('YOUR_logo.PNG')


# ------------- PATH, VARIABLES ETC. -------------------------------------------------------------------------------- #
ad_hoc_path = "you/path/to/the/main_folder/where/all/subfolders/are/to_be/searched/for"

# used to save result when searching
matching = []
# like a cut from the nested_dict based on the search and for listing to main listbox
by_name_result_dict = {}


# ------------- FUNCTIONS ------------------------------------------------------------------------------------------- #
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


def search_within_adhoc_dict():
    global matching

    # delete the previous searched items in listbox
    listbox_name_file.delete(0, END)

    # take the input from the search_label and add * to star&end from string
    search_input = '*' + input_search_by_name.get().lower() + '*'

    # search the whole ad-hoc folder (files_list) and store the matching result in matching
    if fnmatch.filter(nested_dict, search_input) is not None:
        matching = fnmatch.filter(nested_dict, search_input)

        # go through all results within matching and insert each to listbox without adHoc-folder-prefix
        for item in matching:
            listbox_name_file.insert(matching.index(item), item)



def open_file_from_listbox_all_results(event):
    # open the selected file in listbox
    open_path = ad_hoc_path + listbox_all_results.get(listbox_all_results.curselection())
    open_path = open_path.replace('/', '\\')
    os.startfile(open_path)



def lists_results_from_name_selection(event):
    # lists the folder & it's items within
    global by_name_result_dict

    # delete the previous searched items in listbox
    listbox_all_results.delete(0, END)

    # create dict from the already matched person where key is a folder and value is a list of files within
    by_name_result_dict = nested_dict[listbox_name_file.get(listbox_name_file.curselection())]

    # iterates through the folders and it's files for inserting it to the listbox
    for folder, items in by_name_result_dict.items():
        listbox_all_results.insert(END, folder.split(ad_hoc_path)[1])
        each_file = by_name_result_dict[folder]
        num = len(by_name_result_dict[folder])

        for item in range(0, num):
            listbox_all_results.insert(END, each_file[item])
            print(each_file[item])

        listbox_all_results.insert(END, '\n')



def search_within_adhoc_list():
    global matching

    # delete the previous searched items in listbox
    listbox_all_results.delete(0, END)

    # take the input from the search_label and add * to star&end from string
    search_input = '*'+input_search_by_text.get().lower()+'*'

    # search the whole ad-hoc folder (files_list) and store the matching result in matching
    if fnmatch.filter(files_list, search_input) is not None:
        matching = fnmatch.filter(files_list, search_input)

        # list all results within matching and insert each to listbox_all_results
        for item in matching:
            listbox_all_results.insert(matching.index(item), item)



# ------------- MAIN  --------------------------------------------------------------------------------------------- #
print(f"file_list_path: {file_list_path}")

with open(file_list_path, "r", encoding='utf-8') as txt_file_path_output:
    files_list = txt_file_path_output.readlines()
# to use and access the values within the file my code bellow need it as a list
files_list = [line.strip() for line in files_list]

distinct_persons = distinct_list_of_namefiles(files_list)

with open(nested_dict_path, 'r', encoding='utf-8') as infile:
    nested_dict = json.load(infile)



# ------------- UI -------------------------------------------------------------------------------------------------- #
window = Tk()
window.title('Ad-Hoc Suche PADASA')
window.minsize(width=600, height=500)
window.config(padx=20, pady=20, bg="white")

# Image
canvas = Canvas(width=210, height=80, bg="white", highlightthickness=0)
pst_image = PhotoImage(file=pst_logo_path)
canvas.create_image(105, 40, image=pst_image)
canvas.grid(row=0, column=4)


# blocker ------------------------------- #
blocker = Label(text="", bg="white")
blocker.grid(row=1, column=0, columnspan=4)


# Label
label_search_by_name = Label(text="Suche n. Name:", bg="white", fg="black")
label_search_by_name.grid(row=2, column=0)

label_search_by_text = Label(text="Suche n. Freitext:", bg="white", fg="black")
label_search_by_text.grid(row=2, column=3)

# Input
input_search_by_name = Entry(width=30)
input_search_by_name.focus()
input_search_by_name.grid(row=2, column=1)

input_search_by_text = Entry(width=30)
input_search_by_text.grid(row=2, column=4)


# blocker ------------------------------- #
blocker = Label(text="", bg="white")
blocker.grid(row=3, column=0, columnspan=4)


# Listbox
listbox_all_results = Listbox(height=60, width=200)
# Create a select for the search-results for opening via the function above
listbox_all_results.bind("<<ListboxSelect>>", open_file_from_listbox_all_results)
listbox_all_results.grid(row=4, column=1, columnspan=4)

listbox_name_file = Listbox(height=60, width=50)
listbox_name_file.bind("<<ListboxSelect>>", lists_results_from_name_selection)
listbox_name_file.grid(row=4, column=0)

# Button
btn_search_by_name = Button(text="Suche Name file",
                            command=search_within_adhoc_dict,
                            bg="white",
                            highlightthickness=0,
                            width=20)

btn_search_by_name.grid(row=2, column=2)

btn_search_by_text = Button(text="Suche Freitext",
                            command=search_within_adhoc_list,
                            bg="white",
                            highlightthickness=0,
                            width=20)

btn_search_by_text.grid(row=2, column=5)


window.mainloop()
