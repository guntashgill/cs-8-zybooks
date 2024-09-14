#functions
def print_main_menu(menu):
    '''to print main menu'''
    print(menu)

def get_grades(all_grades):
    '''to print main menu'''
    grade_list = []
    for i in all_grades:
        grade_list.append(i['grades'])
    return grade_list
    
def get_list_avg(grade_list):
    '''to print main menu'''
    avg_list = []
    for i in grade_list:
        if len(i) == 0:
            avg_list.append(0)
        else:
            avg_list.append(sum(i)/len(i))
    return avg_list

def get_total_grade(info_list, show_steps = False):
    '''to print main menu'''
    if len(info_list) == 0:
        return 0
    grade_list = get_grades(info_list)
    avg_list = get_list_avg(grade_list)
    total_grade = 0
    for i, v in enumerate(avg_list):
        total_grade = total_grade + (0.01)*(info_list[i]['weight'])*v
    return total_grade

def get_selection(action, suboptions):
    '''to print main menu'''
    selection = None
    while selection not in suboptions:
        print(f"What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        selection = input("::: Enter your selection\n> ")
        selection = selection.upper() # to allow us to input lower- or upper-case letters
    print(f"You selected {selection} to",
          f"{action.lower()} {suboptions[selection].lower()}.")
    return selection

def print_grade_info(info_list, show_grades = True):
    '''to print main menu'''
    for i in range(len(info_list)):
        if show_grades == True:
            print(f"{i+1} - {info_list[i]['category']} ({info_list[i]['weight']}%)")
            print(f"{info_list[i]['grades']}")
        else:
            print(f"{i+1} - {info_list[i]['category']} ({info_list[i]['weight']}%)")
    print('---')

def is_num(val):
    """
    The function checks if `val` is a string;
    returns False if `val` is not a string.
    Otherwise, returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
    num_of_dots = 0
    if type(val) != str:
        return False
    else:
        for i in range(len(val)):
            if '0'<= (val[i]) <= '9':
                continue
            elif val[i] == '.':
                num_of_dots += 1
                if num_of_dots >1:
                    return False
            else:
                return False
        return True
       

def create_category(info_str):
    '''to print main menu'''
    new_dict = {}
    spl = info_str.split(' ')
    if len(spl)==2:
        if (len(spl[0]) > 1) and (',' not in spl[0]):
            if is_num(spl[1]) == True:
                 new_dict['category'] = spl[0]
                 new_dict['weight'] = float(spl[1])
                 new_dict['grades'] = []
                 return new_dict
            return 0
        return -1
    return -2

def is_num_str_list(main_list):
    '''to print main menu'''
    if len(main_list) == 0:
        return False
        
    for i in main_list:
        if type(i) != str:
            return False
        if not is_num(i):
            return False
    return True
        
def is_valid_index(idx, in_list, start_idx = 0):
    '''to print main menu'''
    if idx.isdigit() == True:
        if int(idx)-start_idx>=0:
            if int(idx)-start_idx < len(in_list):
                return True
    return False

def update_category(info_list, idx, info_str):
    '''to print main menu'''
    if type(create_category(info_str)) == dict:
        original_grades = info_list[idx]['grades'] 
        info_list[idx] = create_category(info_str)
        info_list[idx]['grades'] = original_grades
        return info_list[idx]
    else:
        return create_category(info_str)

def delete_item(info_list, idx, start_idx = 0):
    '''to print main menu'''
    if len(info_list) > 0:
        if is_valid_index(idx, info_list, start_idx):
            return info_list.pop(int(idx)-start_idx)
        return -1
    return 0
    


            
    
            
        
    
