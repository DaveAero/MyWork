# lab5.1.5-readData.py
# This program is used to store a sudents name, coursed and course grades
# author: David Burke

#user inputs
transcript = []
studentName = str(input("Please input students name:"))
module = str(input("Enter a module name (leave blank to quit) :"))

while module != "":
    modules = {"courseName":str(module),
                "grade":0}
    transcript.append(modules)
    module = str(input("Enter another module name (leave blank to quit) :"))

## assign grades to each module
#check a module has been entered
if len(transcript) != 0:
    for i in range(0, len(transcript)):
        grade = {"grade":int(input("Please input the grade for {}:".format(transcript[i]["courseName"])))}
        (transcript[i]).update(grade)

#create the data structure for the student
student = {"name":studentName,
             "modules": transcript}

#print student name
print ("Student: {}".format(student["name"]))

# for each module in the module list, print name and grade
for module in student["modules"]:
    #\t used for neater formatting
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))