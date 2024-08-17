# This example performs miscellaneous string actions

school = "Delta College"

print(school[1])

for aChar in school:
	print(aChar)
  
print(len(school))

loudSchool = school.upper()
print(loudSchool)

quietSchool = school.lower()
print(quietSchool)

attribute = " is cool"
school = school + attribute
print(school)

school += attribute
print(school)
