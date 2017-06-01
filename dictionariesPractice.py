
testDict = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', 'Http'],
            'Kenneth Love': ['Python Basics', 'Python Collections']}


def num_teachers(dictionary):
    return len(dictionary)

def num_courses(dictionary):
    total = 0
    for value in dictionary.values():
        total += len(value)
    print(total)

def courses(dictionary):
    courseList = []
    for value in dictionary.values():
        for course in value:
            courseList.append(course)
    print(courseList)

def most_courses(dictionary):
    maxNumCourses = 0
    teacher = ''
    for item in dictionary.items():
        if len(item[1]) > maxNumCourses:
            maxNumCourses = len(item[1])
            teacher = item[0]
    return teacher

def stats(dictionary):
    newList = []
    for item in dictionary.items():
        elemList = []
        elemList.append(item[0])
        elemList.append(len(item[1]))
        newList.append(elemList)
    return newList

print(stats(testDict))