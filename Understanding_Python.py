##############################
# Morales_C_Lab1
#Calli Morales
#Due April 10, 2017
##############################

##############################
# 1. Mathematical Calculation
##############################

height=3
print (3*11-38) + (17.0//height)**3 + 2

# the variable 'height' is used as a variable in the mathematical calculation
# the '//' discards the fractional part, effectively using floor division rather than a classic division
# the '**' operator calculates powers, in this case, to the power of 3

##############################
# 2. String Handling
##############################

name='Brianna'
sentence='Did you hear what '+name+' asked?\nNo, what happened?'
print sentence

print name+' asked "Why is your sister here?"'
print 'Oh my gosh, she didn\'t!'

# the `name` variable stores the name of a person
# /n is used to create a newline
# the string in the first line is enclosed in single quotes because the string contains a double quote
# the string can also be enclosed in double quotes as shown in the second line because no quotes needed to be used
# the final line is an example of escaping a quote within a string

##############################
# 3. String and List Indexing
##############################

Superheroname='Spiderman'
print 'Superheroname= '+Superheroname
print 'Superheroname[0]= '+Superheroname[0]
print 'Superheroname[-2]= '+Superheroname[-2]
print 'Superheroname[-3:]= '+Superheroname[-3:]
print 'Superheroname[:5] + Superheroname[5:]= '+Superheroname[:5] + ' ' + Superheroname[5:]

# Strings can be indexed (subscripted) starting with index 0 (the first character)
# You can also index strings using negative numbers (counting from the right)
# Slicing is also supported, allowing one to obtain a substring

Examplelist=['Learning', 'Python', 'for', 'the', 'Future']
print 'Examplelist[0]= '+Examplelist[0]
print 'Examplelist[-3]= '+Examplelist[-3]
print 'Examplelist length= ' + str(len(Examplelist))

print Examplelist
Examplelist[3:6] = ['Geography', '173', 'Class']
print Examplelist

# Assignment to slices are possible
# they can also be replaced
# Strings and ints cannot be concatenated in Python. In line 57 we have
# to force the length of the List into a string so we can print.

##############################
# 4. Decision Making
##############################

UCschools = 9
if UCschools == 9:
    print 'The number of UC schools is 9!'
    # convention is to indent 4 spaces because python can read the spaces before the beginning of a line
elif UCschools < 9:
    print 'sorry, try a higher number'
else:
    print'try a lower number'

##############################
# 5. Iteration Control
##############################

looping = ['we', 'are', 'learning', 'about', 'looping']
for l in looping:
    print l, len (l)

for q in range(5, 10):
    print q

# the loop will continue until the condition reaches the last value
#last number is not executed

count = 0

if count < 5:
    print "This if statement count is", count
    
while count < 10:
    print "This is number", count
    count += 1
    
# the numbers will move incrementally up because of the last line
##############################
# 6. File Handling
##############################

with open('./python_lab_file.txt', 'w') as f:
    f.write('I am now writing to a new file! The next open command will read the entire file\n')
print f.closed

with open('./python_lab_file.txt', 'r') as f:
    Filetext=f.read()
    print Filetext

# a new file is opened using python's open method.
# the w+ tells python we will both read and write to the file
# w+ will also create the file if it doesn't already exist
# using the with keyword with the file properly closes the file
# after the suite finishes. This is then verified 
