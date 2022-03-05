# lab5.1.4-courseList.py
# This program is used to store a sudents name, coursed and course grades
# author: David Burke

student = {"name":"Mary",
            
            "modules": [{"courseName":"Programming", "grade": 45}, 
                        {"courseName":"History", "grade":99}]}

#print student name
print ("Student: {}".format(student["name"]))

# for each module in the module list, print name and grade
for module in student["modules"]:
    #\t used for neater formatting
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))