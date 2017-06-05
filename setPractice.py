a = {1, 2, 3}
print(type(a))

# not a set
b = {}
print(type(b))

c = set()
print(type(c))

# add, update
songs = {"first", "second", "third"}
songs.add("Treehouse Hula")
songs.update({"Python Two-Step", "Ruby Rhumba"}, {"last song"})

# operations
set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

set1.union(set2)
sum = set1 | set2

set1.difference(set2)
set2.difference(set2)
diff = set1 - set2

unique = set1 ^ set2
set2.symmetric_difference(set1)

set1.intersection(set2)
intersect = set1 & set2

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

testTopics = {"PHP", "Python"}

def covers(searchTopics):
    result = []
    for keyCourse, valueCourse in COURSES.items():
        checkSet = set(valueCourse)
        if (searchTopics.intersection(checkSet)):
            result.append(keyCourse)
    return result
