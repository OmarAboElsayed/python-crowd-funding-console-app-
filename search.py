import json
from create_project import validate_datetime
from view_projects import view_projects
def search_project(user_mail):
    view_projects(user_mail)
    project_date = input('\n please Enter Your Date  (dd/mm/yyyy) : ')
    try:
        valid_date = validate_datetime(project_date)
        if valid_date:
            list = []
            json_file = open('projects_data.json')
            for line in json_file:
                Dict = json.loads(line)
                list.append(Dict)
            for dict in list:
                if project_date == dict['Start_Time'] or project_date == dict['End_Time']:
                    print("\nYour project information:")
                    print(dict)
                else:
                    print("No Data")
                    search_project(user_mail)

        else:
            print("\nplease enter valid data :")

    except ValueError:
        print('Invalid data')
  
         

