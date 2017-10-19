'''
Programming Exercises from John Zelle's "Python Programming: An introduction to computer science
Created on Oct 6, 2015
@author: Icarus
'''
# CHAPTER 3

# EX 3.1 PROGRAM TO CALCULATE VOLUME AND AREA OF A CIRCLE def main ():
# import math print("Program for calculating V (volume) and A (area)
# of a circle") x = eval(input("Enter radius: ")) volume = 4 / 3 *
# math.pi * (x ** 3) area = (math.pi) * (x ** 2) print('The volume is:
# ', volume, end="") print(', and the area is: ', area) main()   

# EX 3.2 PROGRAM TO CALCULATE COST OF SQUARE INCH OF PIZZA def main():
# import math print('This program will calculate the cost per square
# inch of pizza') diameter, cost = eval(input('Please enter the
# pizza\'s diameter and cost, separated by a comma (","): ')) radius =
# diameter / 2 area = math.pi * (radius ** 2) ans = cost / area ans =
# round(ans, 2) print('You pay: $', ans, 'per square inch of pizza!')
# main()

# EX 3.3 PROGRAM TO CALCULATE WEIGHT OF HYDROCARBON BASED ON THE NUMBER OF EACH TYPE OF ATOM
# def main():
#     print('This program will calculate the weight of hydrocarbon!')
#     print('')
#     import math
#     H = 1.0079
#     C = 12.011
#     O = 15.9994
#     h,c,o = eval(input('Please enter the amount of Hydrogen, Carbon, and Oxygen, in that order and separated by commas: '))
#     ans = H * h + C * c + O * o
#     ans = round(ans, 2)
#     print('This particular compound wieghs a total of', ans,' atomic mass units!')
# 
# main()

# EX 3.4 PROGRAM TO CALCULATE DISTANCE OF A LIGHTNING STRIKE BASED ON TIME BETWEEN FLASH AND SOUND
# def main():
#     import math
#     mile = 5280
#     speed = 1100
#     print('This program will calculate the distance a lightning strike based on the time elapsed between seeing the flash and hearing the thunder!')
#     print('')
#     time = eval(input('How many seconds elapsed between the flash and thunder? '))
#     ans = (time * speed) / mile
#     ans = round(ans, 2)
#     print('The lightning occured ', ans, ' mile/s from your locus!') 
# main() 

# EX 3.5 PROGRAM TO CALCULATE COST OF COFFEE, SHIPPING, AND ADDED FIXED COST BASED ON AMOUNT OF POUNDS PER ORDER
# def main():
#     import math
#     print('This program will calulate your coffee order, including shipping!')
#     print('')
#     c_costpp = 10.50
#     s_costpp = 0.86
#     fixed_cost = 1.50
#     pounds = eval(input('How many pounds of coffee would you like to order? '))
#     ans = round((pounds * c_costpp) + (pounds * s_costpp) + fixed_cost, 2)
#     print('Your total is: $', ans)
#     
# main()

# EX 3.6 PROGRAM TO CALCULATE THE SLOPE OF A LINE
# def main():
#     print('This program will calculate the slope of a line, provided you can supply two of the line\'s coordinates!')
#     print('')
#     x1,y1 = eval(input('Enter the first point (x,y): '))
#     x2,y2 = eval(input('And the second point: '))
#     slope = round((y2 - y1) / (x2 - x1), 2)
#     print('This line\'s slope is: ', slope)
# 
# main()

# EX 3.7 PROGRAM TO CALCULATE THE SLOPE OF A LINE
# def main():
#     import math
#     print('This program will calculate the distance of a line, provided you can supply two coordinates!')
#     print('')
#     x1,y1 = eval(input('Enter the first point (x,y): '))
#     x2,y2 = eval(input('And the second point: '))
#     distance = round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)
#     print('The line\'s  distance is: ', distance)
#  
# main()

# EX 3.8 PROGRAM TO CALCULATE THE GREGORIAN EPACT
# def main():
#     import math
#     print('This program will calculate the gregorian epact for a given year!')
#     print('')
#     year = eval(input('Enter a year (four digits): '))
#     c = year // 100
#     epact = (8 + (c // 4) - c + (((8 * c) + 13) // 25) + (11 * (year % 19))) % 30
#     print('This year\'s epact is: ', epact)
# 
# main()

# EX 3.9 PROGRAM TO CALCULATE THE AREA OF A TRIANGLE, GIVEN THE LENGTH OF ITS THREE SIDES
# def main():
#     import math
#     print('This program will calculate the area of a triange, if you can provide the lengths of all three sides!')
#     print('')
#     a,b,c = eval(input('Enter the length for each of the three sides (a,b,c): '))
#     s = (a + b + c) / 2
#     A = math.sqrt(s * (s - a) * (s - b) * (s -c))
#     print('The triangle\'s area is: ', A)
#     
# main()

# EX 3.10 PROGRAM TO CALCULATE A LADDER'S LENGTH, GIVEN THE ANGLE AND HEIGHT IT REACHES TO
# def main():
#     import math
#     print('This program will calculate the length of ladder you need to reach a given height and at a given angle!')
#     print('')
#     height, angle = eval(input('Enter the height (in feet) to be reached and the angle of the ladder: '))
#     r_angle = (math.pi / 180) * angle
#     length = height / (math.sin(r_angle))
#     length = round(length, 1)
#     print('With that angle and to reach that height, you will need a ladder that is', length, 'feet long.')
# 
# main()

# EX 3.11 PROGRAM FOR CALCULATING THE SUM OF FIRST NATURAL NUMBERS TO GIVEN INPUT
# def main():
#     import math
#     total = 0
#     print('This program will calculate the sum of all natural numbers leading up to your input\'s value!')
#     n = eval(input('Please enter a natural number: '))
#     for i in range(0, n+1):
#         total = total + i
#     print('Total is:', total)
# main()

# EX 3.12 PROGRAM FOR CALCULATING THE SUM OF CUBED FIRST NATURAL NUMBERS TO GIVEN INPUT
# def main():
#     import math
#     total = 0
#     print('This program will calculate the sum of all cubed natural numbers leading up to your input\'s value!')
#     n = eval(input('Please enter a natural number: '))
#     for i in range(0, n+1):
#         total = total + (i ** 3)
#     print('Total is:', total)
# main()

# EX 3.13 PROGRAM FOR CALCULATING THE SUM OF USER SPECIFIED NUMBERS. AMOUNT OF NUMBERS IS ALSO SPECIFIED BY USER. 
# def main():
#     print('This program will calculate the sum of all your numbers, you even get to choose how many to input!')
#     a = eval(input('Please enter the amount of numbers you would like to input: '))
#     total = 0
#     num = 0
#     for i in range(1, a+1):
#         num = eval(input('Enter a number: '))
#         total = total + num
#     print('These', a,'numbers add up to:', total)
# main()

# EX 3.14 PROGRAM FOR CALCULATING THE AVERAGE OF USER SPECIFIED NUMBERS. AMOUNT OF NUMBERS IS ALSO SPECIFIED BY USER. 
# def main():
#     print('This program will calculate the average of all your numbers, you even get to choose how many to input!')
#     a = eval(input('Please enter the amount of numbers you would like to input: '))
#     total = 0
#     num = 0
#     for i in range(1, a+1):
#         num = eval(input('Enter a number: '))
#         total = total + num
#     average = total / a
#     print('These', a,'numbers average to:', average)
# main()

# EX 3.15 PROGRAM FOR ESTIMATING PI BASED ON AN AMOUNT OF TERMS ENTERED BY THE USER
# def main():
#     import math
#     print('This program will estimate the value of pi, dependent upon an amount of terms to calculate it by!')
#     print('')
#     n = eval(input('Enter an amount of terms: '))
#     total = 0
#     for i in range(1, n * 2, 2):
#         total = (total + 4/i) * -1
#     total = abs(total) 
#     acc = math.pi - total
#     print('Pi approximation using', n,'terms is:', total)
#     print('Approximation accuracy: within', acc)  
# main()

# EX 3.16 PROGRAM FOR CALCULATING THE NTH TERM OF THE CLASSIC FIBONACCI SEQUENCE, WHERE N IS AN INPUT BY THE USER
# def main():
#     print('This program will calculate a specific term of the classic Fibonacci sequence. The term is determined by you!')
#     print('')
#     n = eval(input('Please enter the term you would like to calculate for: '))
#     x = 1
#     y = 1
#     for i in range(2, n):
#         x,y = x + y,x
#     print('That term of the sequence is:', x)
# main()

# EX 3.17 THIS PROGRAM FOLLOWS AN ALGORITH WHICH APPROXIMATES THE FUNCTION OF SQUARE ROOT USING NEWTON'S METHOD OF GUESSING
# def main():
#     import math
#     print('This program is designed to guess at the square root of a given number, each time it thinks through the problem it will make a more educated guess.') 
#     print('You must specify both the number to find the square root, as well as how many times to think through the problem!')
#     print('')
#     root, n = eval(input('Please enter the desired radical, a comma, and then the amount of times the program should think: '))
#     guess = root / 2
#     for i in range(1, n):
#         guess = (guess + (n / guess)) / 2
#     actual = math.sqrt(root)
#     diff = actual - guess
#     print('The program guesses the square root of', root,'is:', guess)
#     print('The ACTUAL square root of', root,'is:', actual)
#     print('This guess was off by:', diff)
# main()


    
# CHAPTER 4

# PRACTICE    

# from graphics import *
# 
# def main():
#     win = GraphWin("CHAPTER 4 EXERCISES", 400, 400)

   
#     a = Point(10,10)
#     b = Point(290,290)
#     c = Line(a,b)
#     c.draw(win)
#     
#     d = Oval(Point(50,50), Point(60,100))
#     d.draw(win)
#     d.setFill('blue')
#     
#     e = Point(50,50)
#     e.draw(win)
#     e.setFill('red')
#     
#     shape = Polygon(Point(5,5), Point(350,350), Point(5,350), Point(350,5))
#     shape.setFill('orange')
#     shape.draw(win)
#     
#     word = Text(Point(250,250), "Got Milk?")
#     word.setFace("courier")
#     word.setSize(18)
#     word.setStyle("italic")
#     word.draw(win)
    
# EX 4.1A
#     shape = Rectangle(Point(50,50), Point(100,100))
#     shape.setOutline('red')
#     shape.setFill('red')
#     shape.draw(win)
#     
#     for i in range(10):
#         p = win.getMouse()
#         c = shape.getCenter()
#         dx = p.getX() - c.getX()
#         dy = p.getY() - c.getY()
#         shape.move(dx,dy)
#     win.close()

# EX 4.1B   
#     shape = Rectangle(Point(50,50), Point(100,100))
#     shape.setOutline('red')
#     shape.setFill('red')
#     shape.draw(win)
#     
#     for i in range(10):
#         p = win.getMouse()
#         c = shape.getCenter()
#         dx = p.getX() - c.getX()
#         dy = p.getY() - c.getY()
#         x = shape.clone()
#         x.move(dx,dy)
#         x.draw(win)
#         
#     win.close()  

# EX 4.1C
#     shape = Rectangle(Point(50,50), Point(100,100))
#     shape.setOutline('red')
#     shape.setFill('red')
#     shape.draw(win)
#      
#     for i in range(10):
#         p = win.getMouse()
#         c = shape.getCenter()
#         dx = p.getX() - c.getX()
#         dy = p.getY() - c.getY()
#         x = shape.clone()
#         x.move(dx,dy)
#         x.draw(win)
#     
#     quitText = Text(Point(100,100), "Click again to quit")
#     quitText.draw(win)
#     win.getMouse()     
#     win.close() 

# EX 4.2
#     win.setCoords(-0.5, -0.5, 10.5, 10.5)
#     white = Circle(Point(5.0,5.0), 5.0)
#     black = Circle(Point(5.0,5.0), 4.0)
#     blue = Circle(Point(5.0,5.0), 3.0)
#     red = Circle(Point(5.0,5.0), 2.0)
#     yellow = Circle(Point(5.0,5.0), 1.0)
#     
#     black.setFill('black')
#     blue.setFill('blue')
#     red.setFill('red')
#     yellow.setFill('yellow')
#     
#     white.draw(win)
#     black.draw(win)
#     blue.draw(win)
#     red.draw(win)
#     yellow.draw(win)
    
# EX 4.3
#     win.setCoords(-0.5, -0.5, 10.5, 10.5)
#     head = Circle(Point(5,5), 5)
#     head.setFill(color_rgb(0,255,179))
#     
#     leftEye = Circle(Point(3,6), 1.5)
#     leftEye.setFill('white')
#     leftIris = Circle(Point(3,6), .8)
#     leftIris.setFill('green')
#     leftPupil = Circle(Point(3,6), .25)
#     leftPupil.setFill('black')
#     
#     rightEye = leftEye.clone()
#     rightEye.move(4,0)
#     
#     rightIris = leftIris.clone()
#     rightIris.move(4,0)
#     
#     rightPupil = leftPupil.clone()
#     rightPupil.move(4,0)
#     
#     nose = Polygon(Point(5.5,5), Point(3.5,3), Point(5.5,3))
#     nose.setFill('red')
#     
#     mouth = Rectangle(Point(2,1.5), Point(8,2.5))
#     mouth.setWidth(2)
#     mouth.setFill('blue')
#     
#     head.draw(win)
#     leftEye.draw(win)
#     leftIris.draw(win)
#     leftPupil.draw(win)
#     rightEye.draw(win)
#     rightIris.draw(win)
#     rightPupil.draw(win)
#     nose.draw(win)
#     mouth.draw(win)

# EX 4.4
#     win.setCoords(0,0,100,100)
#     win.setBackground('blue')
#     a = Rectangle(Point(-1,-1), Point(101,33))
#     a.setFill('white')
#     
#     b = Rectangle(Point(67, 20), Point(73,30))
#     b.setFill('brown')
#     c = Polygon(Point(70,30), Point(55,30), Point(70,40), Point(60,40), Point(70,50), Point(65,50), Point(70,55), Point(75,50), Point(70,50), Point(80,40), Point(70,40), Point(85,30), Point(70, 30,))
#     c.setFill('green')
#     
#     d = Circle(Point(30,10), 15)
#     d.setFill('white')
#     e = Circle(Point(30,25), 10)
#     e.setFill('white')
#     f = Circle(Point(30,35), 5)
#     f.setFill('white')
#     
#     a.draw(win)
#     b.draw(win)
#     c.draw(win)
#     d.draw(win)
#     e.draw(win)
#     f.draw(win)

# EX 4.5
#     win.setCoords(0,0,100,100)
#     win.setBackground('brown')
#     
#     die = Rectangle(Point(10,10), Point(15,15))
#     one = Circle(Point(12,12), 1)
#     one.setFill('black')
#     two = Circle(Point(11,12), 1) 
#         
# main()




# CHAPTER 5

# EX 5.1
# def main():
#     day, month, year = eval(input("Enter day, month, and year numbers: "))
#     
#     date1 = str(month)+"/"+str(day)+"/"+str(year)
#     
#     months = ["January","February","March","April","May","June","July",
#               "August", "September","October","November","December"]
#     monthStr = months[month-1]
#     date2 = monthStr+" "+str(day)+", "+str(year)
#     
#     print("The date is {0}, or {1}".format(date1, date2))
# 
# main()

# EX 5.2
# def main():
#     score = int(input("Enter score of quiz: "))
#     
#     grades = ["A", "B", "C", "D", "F", "F"]
#     quiz_grade = grades[abs(score-5)]
#     
#     print("Grade: {0}".format(quiz_grade))
# 
# main()

# EX 5.2
# def main():
#     score = int(input("Enter score (0-100) of quiz: "))
#     score = score//10 
#     
#     grades = ["A", "A", "B", "C", "D", "F", "F", "F", "F", "F", "F"]
#     quiz_grade = grades[abs(score-10)]
#      
#     print("Grade: {0}".format(quiz_grade))
#  
# main()

# EX 5.3
# def main():
#     phrase = input("Enter a phrase to be turned into an acronym: ")
#     phrase = phrase.upper()
#     phrase_pieces = phrase.split()
#     acro = []
#     
#     for i in phrase_pieces:
#         acro.append(i[0])
#            
#     print("".join(acro))
#     
# main() 

# EX 5.4
# def main():
#     name = input("Enter a name, and I'll calculate it's number: ")
#     
#     name = name.lower()
#     
#     ans = 0
#     
#     for i in name:
#         ans = ans + (ord(i) - 96)
# 
#     print("This name's number is: {0}".format(ans))
#     
# main()

# EX 5.5 & 5.6
# def main():
#     name = input("Enter a name, and I'll calculate it's number: ") 
#     name = name.lower()
#     name = name.replace(" ","")
#      
#     ans = 0
#      
#     for i in name:
#         ans = ans + (ord(i) - 96)
#  
#     print("This name's number is: {0}".format(ans))
#      
# main()  

# EX 5.7 & 5.8
# def main():
#     
#     print("Caesar cipher")
#     print()
# 
#     key = eval(input("Enter the key value: "))
#     plain = input("Enter the phrase to encode: ")
# 
#     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
# 
#     cipher = ""
#     for letter in plain:
#         pos = chars.find(letter)
#         newpos = (pos + key) % len(chars)
#         cipher = cipher + chars[newpos]
# 
#     print("Encoded message follows:")
#     print(cipher)
# 
# main()

#EX 5.9
# def main():
#     sentence = input("Type a sentence: ")
#     ans = len(sentence.split())
#     print("This sentence has {0} words in it.".format(ans))
#     
# main()

#EX 5.10
# def main():
#     sentence = input("Type a sentence: ")
#     words = sentence.split()
#     tally = 0
#     
#     for wrd in words:
#         tally = tally + len(wrd)
#         
#     ans = tally // len(words)
#     print("The words in this sentence have an average of {0} letters.".format(ans))
#     
# main()

# EX 5.11

# def main():
#     x,y = eval(input("Enter two numbers: "))
#     
#     print("")
#     print("INDEX {0:>8} {1:>9}".format(x,y))
#     print("----------------------------")
#     
#     for i in range(10):
#         x = 3.9 * x * (1 - x)
#         y = 3.9 * y * (1 - y)
#         
#         print("{0:>3} {1:>12.6f} {2:>10.6f}".format(i+1,x,y))
#     
# main()

# EX 5.12
# def main():
#     scoreFileName = input("What file has the recorded scores? ")
#     reportFileName = input("Where should the results be posted? ")
#     
#     scoreFile = open(scoreFileName, "r")
#     reportFile = open(reportFileName, "w")
#     
#     grades = ["A", "A", "B", "C", "D", "F", "F", "F", "F", "F", "F"]
#     
#     for line in scoreFile:
#         quiz_grade = grades[abs((int(line))//10)-10]
#         
#         print("Grades: {0:^10}".format(quiz_grade), file=reportFile)
#         
#     scoreFile.close()
#     reportFile.close()
#     
#     print("Scores have been reported in {0}".format(reportFile))
#   
# main()

# EX 5.13
# def main():
#     scoreFileName = input("What file should I count up? ")
#      
#     scoreFile = open(scoreFileName, "r")
#     
#     L = 0
#     W = 0
#     C = 0
#           
#     for line in scoreFile:
#         L = L + 1
#         C = C + len(line)
#         W = W + len(line.split())
#         
#     scoreFile.close()
#      
#     print("The document, {0:^3}, contains {1} lines, {2} words, and {3} characters".format(scoreFileName, L, W, C))
#    
# main()

# EX 5.14
# from graphics import *
# 
# def main():
#     inFileName = input("What file contains the grades? ")
#     inFile = open(inFileName)
#     
#     fileList = []
#     
#     for line in inFile:
#         fileList.append(line)
#     
#     y = int(fileList[0])
#     
#     win = GraphWin("Student Grade Chart", 400, 400)
#     win.setCoords(-10, -10, 130, (y*10)+10)
#     
#     Text(Point(65, y*10+5), "STUDENT GRADE CHART").draw(win)
#     
#     index = 1
#     
#     for line in fileList[1:]:
#         pieces = line.split()
#         Text(Point(0,(y*10)-(index*10)), pieces[0]).draw(win)
#         Rectangle(Point(20,(y*10)-(index*10)-3), Point(20 + int(pieces[1]),(y*10)-(index*10)+3)).draw(win)
#         index = index + 1
# main()

# EX 5.15
# from graphics import *
#  
# def main():
#     inFileName = input("What file contains the grades? ")
#     inFile = open(inFileName)
#     
#     win = GraphWin("Student Grade Chart", 400, 400)
#     win.setCoords(-10, -10, 120, 120)
#      
#     Text(Point(55, 115), "STUDENT GRADE HISTOGRAM").draw(win) 
#      
#     ansList = ""
#      
#     for line in inFile:
#         ansList = ansList + line
#         
#     ansList = ansList.split()
#     
#     index = 0
#     
#     for i in ansList:
#         ansList[index]=int(i)
#         index = index + 1
#              
#     for i in range(11):
#         height = ansList.count(i)
#         Text(Point((i*10)+10, 10), i).draw(win)
#         Rectangle(Point((i*10)+8, 20), Point(i*10+12, height*10+20)).draw(win)
# main()



# CHAPTER 6

# PRACTICE (value updates if object is mutable)
# 
# def addInterest(balances, rate):
#     for i in range(len(balances)):
#         balances[i] = balances[i] * (1+rate)
# 
# def test():
#     amounts = [1000,2150,800,3275]
#     rate = 0.05
#     addInterest(amounts,rate)
#     print(amounts)
# 
# test()

# EX 6.1
# def oldM():
#     print("Old MacDonald had a farm, Ei-igh, Ei-igh, Oh!")
#     
# def farmAnimal(animal,sound):
#     oldM()
#     print("And on that farm he had a {0}, Ei-igh, Ei-igh, Oh!".format(animal))
#     print("With a {0}, {0} here and a {0}, {0} there.".format(sound))
#     print("Here a {0}, there a {0}, everywhere a {0}, {0}".format(sound))
#     oldM()
#     print()
#     
# def main():
#     farmAnimal('cow','moo')
#     farmAnimal('dog','woof')
#     farmAnimal('cat','meow')
#     farmAnimal('horse','neigh')
#     farmAnimal('monkey','ooh-ooh-ah-ah')
# 
# main()
        
# EX 6.2
# def openingLyric(number):
#     print("The ants go marching {0} by {0}, hurrah! hurrah!".format(number))
#     print("The ants go marching {0} by {0}, hurrah! hurrah!".format(number))
#     print("The ants go marching {0} by {0},".format(number))
#     
# def actionEndLyric(verb,noun):
#     print("The little one stops to {0} his {1},".format(verb,noun))
#     print("And they all go marching down...")
#     print("In the ground...")
#     print("To get out...")
#     print("Of the rain.")
#     print("Boom! Boom! Boom!")
#     
# def main():
#     
#     numberWords = ["one","two","three","four","five","six","seven","eight","nine","ten"]
#     
#     verbWords = input("Provide ten verbs (separate each by a comma and space, please!): ")
#     verbWords = verbWords.split(", ")
#     nounWords = input("Provide ten nouns (separate each by a comma and space, please!): ")
#     nounWords = nounWords.split(", ")
#     
#     for verse in range(10):
#         openingLyric(numberWords[verse])
#         actionEndLyric(verbWords[verse], nounWords[verse])
#         print()
# 
# main()

# EX 6.3
# def sphereArea(radius):
#     import math
#     a = 4 * math.pi * (radius ** 2)
#     return a
#  
# def sphereVolume(radius):
#     import math
#     v = 4 / 3 * math.pi * (radius ** 3) 
#     return v
#  
# def main ():
#     print("Program for calculating V (volume) and A (area) of a circle")
#     x = eval(input("Enter radius: "))
#     volume = sphereArea(x)
#     area = sphereVolume(x)
#     
#     print('The volume is: {0:0.2f}'.format(volume), end="")
#     print(', and the area is: {0:0.2f}.'.format(area))
# main()  

# EX 6.4
# def sumN(n):
#     sum = 0
#     for i in range(n+1):
#         sum = sum + i
#         
#     return sum
# 
# def sumNCubes(n):
#     sum = 0
#     for i in range(n+1):
#         sum = sum + i ** 3
#     
#     return sum
# 
# def main():
#     n = eval(input("Enter a number: "))
#     
#     ans1 = sumN(n)
#     ans2 = sumNCubes(n)
#     
#     print("Results: {0}, and {1}".format(ans1,ans2))
#     
# main()

# EX 6.5
# def pizzaArea(diameter):
#     import math
#     
#     r = diameter / 2
#     area = math.pi * (r ** 2) 
#     
#     return area
# 
# def pizzaCost(cost,area):
#     price = round(cost / area, 2)
#     
#     return price
# 
# def main():
#     import math
#     print('This program will calculate the cost per square inch of pizza')
#     diameter, cost = eval(input('Please enter the pizza\'s diameter and cost, separated by a comma (","): '))
#     A = pizzaArea(diameter)
#     ans = pizzaCost(cost, A)
#     print('You pay: ${0:0.2f} per square inch of pizza!'.format(ans))
# main() 

# EX 6.6
# def triangleArea(a,b,c):
#     import math
#     
#     s = (a + b + c) / 2
#     A = math.sqrt(s * (s - a) * (s - b) * (s -c))
#     
#     return A
    
# EX 6.7
# def fibSeq(nth):
#     x = 1
#     y = 1
#     for i in range(2, nth):
#         x,y = x + y,x
#     print('That term of the sequence is:', x)
# 
# def main():
#     print('This program will calculate a specific term of the classic Fibonacci sequence. The term is determined by you!')
#     print('')
#     n = eval(input('Please enter the term you would like to calculate for: '))
#     
#     fibSeq(n)
#     
# main()

# EX 6.8
# def nextGuess(root, n):
#     import math
#     
#     guess = root / 2
#     for i in range(1, n):
#         guess = (guess + (n / guess)) / 2
#     actual = math.sqrt(root)
#     diff = actual - guess
#     
#     return guess, diff, actual
#     
# def main():
#     print('This program is designed to guess at the square root of a given number, each time it thinks through the problem it will make a more educated guess.') 
#     print('You must specify both the number to find the square root, as well as how many times to think through the problem!')
#     print('')
#     
#     root, n = eval(input('Please enter the desired radical, a comma, and then the amount of times the program should think: '))
#     
#     guess, diff, actual = nextGuess(root, n)
#     print('The program guesses the square root of', root,'is:', guess)
#     print('The ACTUAL square root of', root,'is:', actual)
#     print('This guess was off by:', diff)
# main()

# EX 6.9
# def grade(score):
#     score = score//10 
#      
#     grades = ["A", "A", "B", "C", "D", "F", "F", "F", "F", "F", "F"]
#     ans = grades[abs(score-10)]
#     
#     return ans
# 
# def main():
#     x = int(input("Enter score (0-100) of quiz: "))
#     
#     quiz_grade = grade(x)
#       
#     print("Grade: {0}".format(quiz_grade))
#   
# main()

# EX 6.10
# def acronym(phrase): 
#     phrase = phrase.upper()
#     phrase_pieces = phrase.split()
#     acro = []
#      
#     for i in phrase_pieces:
#         acro.append(i[0])
#     
#     ans = "".join(acro)
#     
#     return ans
# 
# def main():
#     inp = input("Enter a phrase to be turned into an acronym: ")
#     
#     x = acronym(inp)
#             
#     print(x)
#      
# main()     

# EX 6.11
# def squareEach(nums):
#     i = 0
#     
#     for n in nums:
#         nums[i] = n ** 2
#         i = i + 1
#     
# def main():
#     print("This program will square each number in a given list")
#     numString = input("Enter a string of numbers: ")
#     
#     numList = []
#     
#     for ch in numString:
#         numList.append(int(ch)) 
# 
#     squareEach(numList)
#     
#     print(numList)
#     
# main()
        
# EX 6.12
# def sumList(nums):
#     sum = 0
#     
#     for n in nums:
#         sum = sum + n
#     
#     return sum
#      
# def main():
#     print("This program will provide the sum of each number in a given list")
#     numString = input("Enter a string of numbers: ")
#      
#     numList = []
#      
#     for ch in numString:
#         numList.append(int(ch)) 
#  
#     ans = sumList(numList)
#      
#     print(ans)
#      
# main()

# EX 6.13
# def toNumbers(strList):
#     i = 0
#      
#     for ch in strList:
#         strList[i] = int(ch)
#         i = i + 1

# EX 6.14
# def file2NumList(file):
#     inFile = open(file, "r")
#     
#     rawList = inFile.readlines()
#     fileList = []
#     
#     for line in rawList:
#         x = line.split()
#         fileList.append(int(x[0]))
#     
#     inFile.close()
#     
#     return fileList
# 
# def squareEach(nums):
#     i = 0
#      
#     for n in nums:
#         nums[i] = n ** 2
#         i = i + 1
#         
# def sumList(nums):
#     sum = 0
#      
#     for n in nums:
#         sum = sum + n
#      
#     return sum
#      
# def main():
#     print("")
#     print("This program takes a specified file and formats it \ninto a list of integers. Then it squares each number and \nreports the total sum.")
#     print("")
#     
#     inputFile = input("Enter a file name which contains numbers separated by new lines: ")
#     
#     numList = file2NumList(inputFile)
#     
#     squareEach(numList)
#     
#     ans = sumList(numList)
#     
#     print("The sum of each listed number, squared, is: {0}".format(ans))
#     
# main()

# EX 6.15
# from graphics import *
# 
# def drawFace(center, size, window):
#     eyeSize = 0.15 * size
#     eyeOff = size / 3.0
#     mouthSize = 0.8 * size
#     mouthOff = size / 2.0
#     head = Circle(center, size)
#     head.setFill("yellow")
#     head.draw(window)
#     leftEye = Circle(center, eyeSize)
#     leftEye.move(-eyeOff, -eyeOff)
#     rightEye = Circle(center, eyeSize)
#     rightEye.move(eyeOff, -eyeOff)
#     leftEye.draw(window)
#     rightEye.draw(window)
#     p1 = center.clone()
#     p1.move(-mouthSize/2, mouthOff)
#     p2 = center.clone()
#     p2.move(mouthSize/2, mouthOff)
#     mouth = Line(p1,p2)
#     mouth.draw(window)
# 
# def main():
#     win = GraphWin("Faces")
#     drawFace(Point(50,50), 10, win)
#     drawFace(Point(100,100), 20, win)
#     drawFace(Point(150,150), 30, win)
#     win.getMouse()
#     win.close()
#     
# main()
   
# EX 6.16

# EX 6.17
# SAME AS EX IN CHAPTER 4 :(

# CHAPTER 7

# EX 7.1
# def main():
#     print("\nThis program will calculate wages, including overtime (>40 hours @ 150% pay).")
#     print()
#     hours, rate = eval(input("How many work hours occured this week,\nand what is the regular hourly wage? "))
#     
#     if hours <= 40:
#         pay = hours * rate
#         
#     else:
#         ot = (hours - 40) * (rate * 1.5)
#         pay = 40 * rate + ot
#       
#     print("This week's pay is ${0:0.2f}".format(pay))
#     
# main()

# EX 7.2
# def main():
#     print("\nThis program will calculate your grade!\n")
#     
#     score = int(input("What score did you get? "))
#     
#     grade = "Please enter a score between 0-5."
#     
#     if score == 5:
#         grade = 'A'
#         
#     if score == 4:
#         grade = 'B'
#         
#     if score == 3:
#         grade = 'C'
#         
#     if score == 2:
#         grade = 'D'
#         
#     if score <= 1:
#         grade = 'F'
#     
#     print("\nYour grade: {0}".format(grade))
#     
# main()

# EX 7.3
# def main():
#     print("\nThis program will calculate your grade!\n")
#      
#     score = int(input("What score did you get? "))
#      
#     grade = "Please enter a score between 0-100."
#      
#     if score <= 100 and score >= 90:
#         grade = 'A'
#          
#     if score < 90 and score >= 80:
#         grade = 'B'
#          
#     if score < 80 and score >= 70:
#         grade = 'C'
#          
#     if score < 70 and score >= 60:
#         grade = 'D'
#          
#     if score < 60:
#         grade = 'F'
#      
#     print("\nYour grade: {0}".format(grade))
#      
# main()

# EX 7.4
# def main():
#     print("\nThis program will inform you of your class standing based on the amount of credits you have completed.")
#     print()
#     credits = int(input("How many credits have you earned? "))
#     
#     if credits < 7:
#         print("\nYou are a Freshman!")
#     
#     if credits >= 7 and credits < 16:
#         print("You are a Sophomore!")
#         
#     if credits >= 16 and credits < 26:
#         print("You are a Junior!")
#         
#     if credits >= 26:
#         print("You are a Senior!") 
# 
# main()

# EX 7.5
# def height2Inches(raw):
#     if raw[1] == "'" and raw[-1] == '"':
#         inches = ((int(raw[0]) * 12) + (int(raw[2:-1])))
#         return inches
#     else:
#         return
#  
# def bmiReport(bmi):
#     if bmi < 19:
#         report = "Your BMI, {0},is below the healthy range. You will likely die very, very soon... :(".format(bmi)
#     elif bmi > 25:
#         report = "Your BMI, {0},is above the healthy range. Painful, fat death is imminent...:(".format(bmi)
#     else:
#         report = "Your BMI, {0}, is nicely within the healthy range. You will live forever...:)".format(bmi)
#  
#     return report
#  
# def main():
#     print("\nThis program will report your BMI (Body Mass Index) based on your weight and height.")
#     print()
#      
#     weight = int(input("Please enter your weight (in lbs): "))
#     height = input("Please enter your height(X\'X\"): ")
#      
#     height = height2Inches(height)
#     
#     if height == None:
#         print("Please properly format your height!")
#         return
#     
#     else: 
#         bmi = weight * 720 // (height ** 2)
#          
#         report = bmiReport(bmi)
#          
#         print(report)
#      
# main()

# EX 7.6
# def main():
#     print("This program will calculate a speeding ticket based on an incremented penalty system.")
#     print()
#     limit, speed = eval(input("What was the speed limit, and clocked speed at the time of the infraction? (FORMAT: X, X) "))
#     
#     if speed > limit:     
#         penalty = (speed - limit) * 5 + 50
#         
#         if speed > 90:
#             penalty = penalty + 200
#         
#         message = "You broke the speed limit. Your fine is: ${0:0.2f}".format(penalty)
#         
#     else:
#         message = "Your speed was legal, no fee!"
# 
#     print()
#     print(message)
# 
# main()

# EX 7.7
# def timeInMinutes(time):
#     time = time.split(":")
#     minutes = time[1]
#     
#     if minutes[-2:] == "PM":
#         time[0] = int(time[0]) + 12
#     
#     minutes = int(minutes[0:2])
#     hours = time[0]
#     
#     total = int(hours) * 60 + minutes
#         
#     print(total)
#     return total
#         
#            
# def main():
#     print("\nThis program will calculate babysitting costs, based on work hours and factoring in adjusting rates(based on time).")
#     print()
#     start = input("What was the start time? (FORMAT => hour:minutes AM/PM) ")
#     end = input("What was the end time? (FORMAT => hour:minutes AM/PM) ")
#     
#     start2 = timeInMinutes(start)
#     end2 = timeInMinutes(end)
#     
#     if end2 > 1260:
#         norm = 1260 - start2
#         xtra = end2 - 1260
#         fee = (norm / 60 * 2.50) + (xtra / 60 * 1.75)
#         
#     else:
#         diff = end2 - start2    
#         fee = diff / 60 * 2.50
#         
#     print("Babysitting from {0} to {1} at $2.50/hour (and $1.75/hour after 9:00PM) costs: \n${2:0.2f}".format(start, end, fee))  
#     
# main()

# EX 7.8
# def main():
#     print("\nThis program will determine your eligibility for the Senate and House of Representatives.")
#     print()
#     
#     age, citizen = eval(input("Please enter your current age, followed by the amount of year(s) you have been a US citizen: "))
#     
#     senate = "are NOT"
#     house = "are NOT"
#     
#     if age > 29 and citizen > 8:
#         senate = "ARE"
#         
#     if age > 25 and citizen > 7:
#         house = "ARE"
#         
#     print("\nYou {0} currently elligible to join the Senate, and you {1} currently elligible to join the House of Representatives".format(senate, house))
#     
# main()

# EX 7.9
# def main():
#     print("\nThis program will calculate the date of Easter for a specified year.")
#     print()
#     year = int(input("Please enter a year between 1982 and 2048: "))
#     
#     if year >= 1982 and year <= 2048:
#         a = year%19
#         b = year%4
#         c = year%7
#         d = ((19 * a) + 24)%30
#         e = ((2 * b) + (4 * c) + (6 * d) + 5)%7
# 
#         ans = 22 + d + e
#         month = "March"
#         
#         if ans > 31:
#             ans = ans - 31
#             month = "April"
#         
#         print("\nEaster is {0} {1} in {2}.".format(month,ans,year))
#         
#     else:
#         print("\nPlease make sure the year falls within the specified years.")
# 
# main()

# EX 7.10
# def main():
#     print("\nThis program will calculate the date of Easter for a specified year.")
#     print()
#     year = int(input("Please enter a year between 1900 and 2099: "))
#     mod = 0
#     
#     if year == 1954 or year == 1981 or year == 2049 or year == 2076:
#         mod = 7
#     
#     if year >= 1900 and year <= 2099:
#         a = year%19
#         b = year%4
#         c = year%7
#         d = ((19 * a) + 24)%30
#         e = ((2 * b) + (4 * c) + (6 * d) + 5)%7
# 
#         ans = 22 + d + e
#         month = "March"
#         
#         if ans > 31:
#             ans = ans - 31 - mod
#             month = "April"
#         
#         print("\nEaster is {0} {1} in {2}.".format(month,ans,year))
#         
#     else:
#         print("\nPlease make sure the year falls within the specified years.")
# 
# main()

# EX 7.11
# def checkYear(x):
#     if x % 100 == 0 and x % 400 != 0:
#         return False
#     elif x % 4 == 0:
#         return True
#     else:
#         return False
#     
# 
# def main():
#     print("\nThis program will calculate if the input year is a leap year or not.")
#     print()
#     year = int(input("Enter a year: "))
#     
#     ans = checkYear(year)
#     
#     if ans == True:
#         ans = "IS"
#         
#     else:
#         ans = "IS NOT"
#     
#     print("\nThis year {0} a leap year!".format(ans))
#     
# main()

# EX 7.12
# def checkYear(x):
#     if x % 100 == 0 and x % 400 != 0:
#         return False
#     elif x % 4 == 0:
#         return True
#     else:
#         return False
#      
# def findMax(month, year):
#     if month == 1:
#         x = checkYear(year)
#         if x:
#             max = 29
#         else:
#             max = 28
#     elif month == 3 or month == 5 or month == 8 or month == 10:
#         max = 30
#     else:
#         max = 31
#         
#     return max
# 
# def checkDate(date):
#     try: 
#         pieces = date.split("/")
#         pieces[0] = int(pieces[0])
#         pieces[1] = int(pieces[1])
#         pieces[2] = int(pieces[2])   
#     except:
#         return False
#     
#     if pieces[0] != abs(pieces[0]) or pieces[1] != abs(pieces[1]) or pieces[2] != abs(pieces[2]):
#         return False
#     if pieces[0] > 12 or pieces[0] < 1:
#         return False
#     if pieces[1] < 1:
#         return False
#     if pieces[2] < 1:
#         return False
#     if pieces[1] > findMax(pieces[0]-1, pieces[2]):
#         return False 
#     
#     return True
# 
# def main():
#     print("\nThis program will validate your date input!")
#     print()
#     date = input("Please enter a date with this format (X/XX/XXXX): ")
#     val = "VALID"
#     
#     x = checkDate(date)
#     
#     if x == False:
#         val = "INVALID"
#     
#     print("\n{0} is {1}!".format(date,val))
#     
# main()
    
# EX 7.13
# def checkYear(x):
#     if x % 100 == 0 and x % 400 != 0:
#         return False
#     elif x % 4 == 0:
#         return True
#     else:
#         return False
#       
# def findMax(month, year):
#     if month == 1:
#         x = checkYear(year)
#         if x:
#             max = 29
#         else:
#             max = 28
#     elif month == 3 or month == 5 or month == 8 or month == 10:
#         max = 30
#     else:
#         max = 31
#          
#     return max
#  
# def checkAndShredDate(date):
#     try: 
#         pieces = date.split("/")
#         pieces[0] = int(pieces[0])
#         pieces[1] = int(pieces[1])
#         pieces[2] = int(pieces[2])   
#     except:
#         return False
#      
#     if pieces[0] != abs(pieces[0]) or pieces[1] != abs(pieces[1]) or pieces[2] != abs(pieces[2]):
#         return False
#     if pieces[0] > 12 or pieces[0] < 1:
#         return False
#     if pieces[1] < 1:
#         return False
#     if pieces[2] < 1:
#         return False
#     if pieces[1] > findMax(pieces[0]-1, pieces[2]):
#         return False 
#      
#     return True, pieces[0], pieces[1], pieces[2]
#  
# def main():
#     print("\nThis program will validate your date input, and then convert the input date into what day number of the year it is!")
#     print()
#     date = input("Please enter a date with this format (X/XX/XXXX): ")
#      
#     x, month, day, year = checkAndShredDate(date)
#      
#     if x == False:
#         ans = "This date is INVALID!"
# 
#     else:
#         ans = 31 * (month - 1) + day
#     
#     if month > 2:
#         ans = ans - (((4 * month) + 23) // 10)
#     
#     if checkYear(year) == True and month > 2:
#         ans = ans + 1
#         
#     print("The given date is day number {0} for the year of {1}".format(ans,year))    
#      
# main()



# EX 7.16

#    An archery target.
# import math
# from graphics import *
#  
# def targetWindow():
#     win = GraphWin("Archery Scorer", 400, 400)
#     win.setCoords(-6, -6, 6, 6)
#     win.setBackground("gray")
#     center = Point(0,0)
#  
#     # Draw the target
#     c1 = Circle(center, 5)
#     c1.setFill("white")
#     c1.draw(win)
#     c2 = Circle(center, 4)
#     c2.setFill("black")
#     c2.draw(win)
#     c3 = Circle(center, 3)
#     c3.setFill("blue")
#     c3.draw(win)
#     c4 = Circle(center, 2)
#     c4.setFill("red")
#     c4.draw(win)
#     c5 = Circle(center, 1)
#     c5.setFill("yellow")
#     c5.draw(win)
#  
#     return win
#  
#  
# def drawInterface(win):
#     msg = Text(Point(0,5.5), "Click where arrow lands")
#     msg.setStyle("bold")
#     msg.setSize(14)
#     msg.draw(win)
#  
#     arrowBox = Text(Point(-4,-5.5),"Arrow:  ")
#     arrowBox.setStyle("bold")
#     arrowBox.draw(win)
#  
#     totalBox = Text(Point(4,-5.5), "Total:   ")
#     totalBox.setStyle("bold")
#     totalBox.draw(win)
#  
#     return msg, arrowBox, totalBox
#  
#  
# def getScore(pt):
#     x,y = pt.getX(), pt.getY()
#     dist = math.sqrt(x*x + y*y)
#     if dist <= 1:
#         score = 9
#     elif dist <= 2:
#         score = 7
#     elif dist <=3:
#         score = 5
#     elif dist <= 4:
#         score = 3
#     elif dist <= 5:
#         score = 1
#     else:
#         score = 0
#     return score
#  
#          
# def main():
#     win = targetWindow()
#     msg, arrowBox, totalBox = drawInterface(win)
#  
#     arrow = 0
#     total = 0
#     for i in range(5):
#         hit = win.getMouse()
#         dot = Circle(hit, 0.1)
#         dot.setFill("green")
#         dot.draw(win)
#         score = getScore(hit)
#         arrowBox.setText("Arrow: {0:1}".format(score))
#         total = total + score
#         totalBox.setText("Total: {0:2}".format(total))
#  
#     msg.setText("Click anywhere to quit.")
#     win.getMouse()
#     win.close()
#  
#  
# main()

# EX 7.17

# from time import sleep
# from graphics import *
# 
# def main():
#     win = GraphWin("Bouncing Circle", 500, 500)
#     circle = Circle(Point(240,260), 50)
#     circle.setFill('green')
#     circle.setOutline('black')
#     circle.draw(win)
#     modX = -1
#     modY = -1
#     
#     for i in range(10000):
#         if win.checkMouse() != None:
#             win.close()
#         else:
#             current = circle.getCenter()
#             x, y = current.getX(), current.getY()
#             
#             if x == 50:
#                 modX = 1
#             elif x == 450:
#                 modX = -1
#             
#             if y == 50:
#                 modY = 1
#             elif y == 450:
#                 modY = -1
#                 
#             circle.move(modX,modY)
#             sleep(0.005)
# 
# main()
    
# CHAPTER 8

# PRE EXERCISES EXERCISE
# A
# def main():
#     x = int(input("Please enter a number to sum up to: "))
#     count = 0
#     sum = 0
#     while count <= x:
#         sum = sum + count
#         count = count + 1
#     
#     print("The consecutive sum up to {0} is {1}".format(x,sum))
#     
# main()

# B
# def main():
#     x = int(input("Please enter a number to sum up (odd numbers only) to: "))
#     count = 1
#     sum = 0
#     while count <= x:
#         sum = sum + count
#         count = count + 2
#      
#     print("The consecutive sum up to {0} is {1}".format(x,sum))
#      
# main()

# C
# def main():
#     x = eval(input("\nEnter a number for me to add! (999 to report sum) "))
#     sum = 0
#     while x != 999:
#         sum = sum + x
#         x = eval(input("\nEnter another number for me to add! (999 to report sum) "))
#  
#     print("\nThe sum of all numbers entered is {0}".format(sum))   
# 
# main()
    
# D
# def main():
#     x = int(input("\nPlease enter a whole number to find the log2 of: "))
#     n = x
#     count = 0
#     
#     while x != 1:
#         x = x // 2
#         count = count + 1
#         
#     print("log2({0}) = {1}".format(n,count))
#     
# main()

# EX 8.1
# def main():
#     print("\nThis program will calculate for a specified place of the Fibonacci sequence.")
#     print()
#     term = int(input("Which term of the sequence would you like to know? "))
#     newSum = 1
#     lastSum = 0
#     count = 0
#     
#     while count < term - 1:
#         newSum, lastSum = lastSum + newSum, newSum
#         count = count + 1
#         
#     print("\nTerm number {0} is {1}".format(term, newSum))
#     
# main()
    
    
# EX 8.2
# def windChill(temp, wind):
#     chill = 35.74 + (0.6215 * temp) - (35.75 * (wind ** 0.16)) + ((0.4275 * temp) * (wind ** 0.16))
#     return chill
# 
# def main():
#     print("\nThe following is a table displaying temperatures, wind speeds, and the corresponding windchill values.")
#     print()
#     print("                                     WIND (mph)                         ")
#     topWind = "        "
#     for i in range(0, 55, 5):
#         topWind = topWind + "{0:^7}".format(i)
#     print(topWind)
#     print(" TEMP ----------------------------------------------------------------------------")
#     
#     temp = -20
#     wind = 0
#     
#     while temp <= 60:
#         vals = " {0:^5.1f}|".format(temp)
#         while wind <= 50:
#             chill = windChill(temp,wind)
#             vals = vals + " {0:^5.1f} ".format(chill)
#             wind = wind + 5
#         temp = temp + 10
#         wind = 0
#         print("{0}".format(vals))
#     
# main()

# EX 8.3
# def main():
#     print("This program will determine how long it takes for an investment to double, based on a given interest rate.")
#     print()
#     apr = eval(input("At which interest rate would you like to calculate for? "))
#     inv = 1
#     years = 0
#     
#     while inv <= 2:
#         inv = inv + inv*apr
#         years = years + 1
#     
#     print("At an interest rate of {0}, it would take {1} years for your investment to double in value.".format(apr,years))
# 
# main()

# EX 8.4
# def main():
#     print("\nThis program will print out the Syracuse sequence for a given number: ")
#     print()
#     n = int(input("Please provide a number: "))
#     originalN = n
#     seq = [n]
#     
#     while n != 1:
#         if n % 2 != 0:
#             n = 3 * n + 1
#             seq.append(n)
#         elif n % 2 == 0:
#             n = n // 2
#             seq.append(n)
#             
#     print("Here is the Syracuse sequence for {0}: {1}".format(originalN,seq))
#     
# main()
    
#EX 8.5
# from math import *
# def main():
#     print("\nThis program will take a number and determine if it is prime or not.")
#     print()
#     n = int(input("Please enter a number to check: "))
#     check = 2
#     max = int(sqrt(n))
#     ans = "PRIME!"
#       
#     while check <= max:
#         if n % check == 0:
#             ans = "NOT PRIME!"
#             break 
#         else:
#             check = check + 1
#       
#     print("{0} is {1}".format(n, ans))
#   
# main()      

# EX 8.6
# from math import *
# def main():
#     print("\nThis program will report all prime numbers less than or equal to a given positive number.")
#     print()
#     n = int(input("Please enter a number: "))
#     check = 2
#     max = int(sqrt(n))
#     primes = []
#     index = 1
#       
#     while index <= n: 
#         while check <= max:
#             if index % check == 0:
#                 break 
#             elif check == max:
#                 primes.append(index)
#                 break
#             elif index == 3:
#                 primes.append(index)
#                 break
#             else:
#                 check = check + 1
#         check = 2
#         index = index + 1
#         
#     print("Here is a list of all prime numbers up to {0}: {1}".format(n, primes))
#     
# main()      
    
# EX 8.7
# from math import *
# def primeList(n):
#     check = 2
#     max = int(sqrt(n))
#     primes = []
#     index = 1
#        
#     while index <= n: 
#         while check <= max:
#             if index % check == 0:
#                 break 
#             elif check == max:
#                 primes.append(index)
#                 break
#             elif index == 3:
#                 primes.append(index)
#                 break
#             else:
#                 check = check + 1
#         check = 2
#         index = index + 1
#          
#     return primes
# 
# def main():
#     print("This program will take an even number, and find two prime numbers that add up to the given even number (which, according to the Goldbach conjecture, should always be possible).")
#     print()
#     n = int(input("Please enter an even number: "))
#     
#     while n % 2 != 0:
#         n = int(input("\nThat is an odd number, please enter an even number! "))
#      
#     x = primeList(n)
#     xi = 0
#     yi = 0 
#     sum = x[xi] + x[yi]  
#     
#     while yi < len(x) - 1:   
#         while xi < len(x) - 1:
#             if sum == n:
#                 break
#             else:
#                 xi = xi + 1
#                 sum = x[xi] + x[yi]
#         
#         if sum == n:
#             break
#         else:
#             xi = 0
#             yi = yi + 1
#             sum = x[xi] + x[yi]
#             
#     print("\nThe prime numbers {0} and {1} add up to {2}.".format(x[xi],x[yi],n))
#     
# main()  
    
# EX 8.8
# def gcd(m,n):
#     while m != 0:
#         n, m = m, n % m
#     return n
# 
# def main():
#     print("Euclid's GCD algorithm\n")
#     x1, x2 = eval(input("Enter two natural numbers (n1, n2): "))
#     print("The GCD of", x1, "and", x2, "is", gcd(x1,x2))
# 
# if __name__ == '__main__':
#     main()

# EX 8.9
# def findMPG(start, end, gal):
#     miles = end - start
#     mpg = miles / gal
#     return mpg
# 
# def unpack(string):
#     x = string.split(" ")
#     odo = eval(x[0])
#     gal = eval(x[1])
#     return odo, gal
#     
# def main():
#     print("\nThis program will calculate your fuel efficiency in MPG across multiple legs of travel.")
#     print()
#     start = int(input("What was the initial odometer reading? "))
#     string = input("After the first leg of the trip, what was the odometer reading and amount of gas (in gallons) used? (separated by a space!) ")
#     odo, gal = unpack(string)
#     report = ""
#     count = 0
#     total = 0
#     
#     while string != "":
#         count = count + 1
#         odo, gal = unpack(string)
#         mpg = findMPG(start, odo, gal)
#         total = total + mpg 
#         start = odo
#         report = report + "\nTrip #{0} efficiency: {1:0.1f} MPG".format(count,mpg)
#         string = input("And the next leg? (press enter to calculate report) ")
#     
#     total = total / count
#     print(report + "\nAnd the total efficiency for all {0} trips was {1:0.1f} MPG".format(count, total))
# 
# main()

    
# EX 8.10
# def findMPG(start, end, gal):
#     miles = end - start
#     mpg = miles / gal
#     return mpg
#  
# def unpack(string):
#     x = string.split(" ")
#     odo = eval(x[0])
#     gal = eval(x[1])
#     return odo, gal
#      
# def main():
#     print("\nThis program will calculate your fuel efficiency in MPG across multiple legs of travel.")
#     print()
#     
#     fileName = input("Select file: ")
#     infile = open(fileName, "r")
#     
#     line = infile.readline()
#     start = eval(line)
#     
#     line = infile.readline()
#     report = ""
#     count = 0
#     total = 0
#      
#     while line != "":
#         odo, gal = unpack(line)
#         mpg = findMPG(start, odo, gal)
#         total = total + mpg 
#         start = odo
#         report = report + "\nTrip #{0} efficiency: {1:0.1f} MPG".format(count,mpg)
#         line = infile.readline()
#         count = count + 1
#     total = total / count
#     print(report + "\nAnd the total efficiency for all {0} trips was {1:0.1f} MPG".format(count, total))
#  
# main()


# EX 8.11
# def main():
#     print("\nThis program will take a list of average daily temperatures and compute a running total of cooling and heating degree-days.")
#     print()
#     allDays = input("Enter a sequence of average daily temperatures: (separate each by a space) ")
#     cooling = 0
#     heating = 0
#     
#     for i in allDays.split(" "):
#         if int(i) > 80:
#             cooling = cooling + (int(i) - 80) 
#         elif int(i) < 60:
#             heating = heating + (60 - int(i))
#     
#     print("Cooling degree-days: {0}\nHeating degree-days: {1}".format(cooling,heating))
#     
# main()
        
# EX 8.12
# def main():
#     print("\nThis program will take a list of average daily temperatures and compute a running total of cooling and heating degree-days.")
#     print()
#     fileName = input("Where is the file? ")
#     inFile = open(fileName, "r")
#     cooling = 0
#     heating = 0
#      
#     for line in inFile:
#         if int(line) > 80:
#             cooling = cooling + (int(line) - 80) 
#         elif int(line) < 60:
#             heating = heating + (60 - int(line))
#      
#     print("Cooling degree-days: {0}\nHeating degree-days: {1}".format(cooling,heating))
#      
# main()
    
# EX 8.13
    
# EX 8.14
    
# EX 8.15

# CHAPTER 9

# EX 9.1 & 9.2
# RACQUETBALL SIMULATION
# from random import random

# def main():
#     printIntro()
#     probA, probB, n, m = getInputs()
#     m_winsA, m_winsB, shutAtot, shutBtot = simMMatches(m, n, probA, probB)
#     printSummary(m_winsA, m_winsB, n, m, shutAtot, shutBtot)

# def printIntro():
#     print("This program simulates a game os raquetball between two")
#     print('players called "A" and "B". The abilities of each player is')
#     print("indicated by a probability (a number between 0 and 1) that")
#     print("the player wins the point when serving. Player A always")
#     print("has the first serve.")
    
# def getInputs():
#     # Returns the three simulation parameters
#     a = eval(input("What is the prob. player A wins a serve? "))
#     b = eval(input("What is the prob. player B wins a serve? "))
#     n = eval(input("How many games per match? (Must be odd to avoid ties) "))
#     while n % 2 == 0:
#         n = eval(input("Oops, that number is even! Please enter an odd number so each match may have an undisputed winner: "))
#     m = eval(input("How many matches to simulate? "))
#     return a, b, n, m

# def simMMatches(m, n, probA, probB):
#     m_winsA = 0
#     m_winsB = 0
#     shutAtot = 0
#     shutBtot = 0
#     for i in range(m):
#         winsA, winsB, shutAtot, shutBtot = simNGames(n, probA, probB)
#         if winsA > winsB:
#             m_winsA = m_winsA + 1
#         else:
#             m_winsB = m_winsB + 1
#     return m_winsA, m_winsB, shutAtot, shutBtot

# def simNGames(n, probA, probB):
#     # Simulates n games of raquetball between players whose
#     # abilities are represented by the probability of winning a serve.
#     # Returns number of wins for A and B
#     winsA = 0
#     winsB = 0
#     shutAtot = 0
#     shutBtot = 0
#     gameNumber = 0
#     for i in range(n):
#         gameNumber = gameNumber + 1
#         scoreA, scoreB, shutA, shutB = simOneGame(probA, probB, gameNumber)
#         if scoreA > scoreB:
#             winsA = winsA + 1
#         else:
#             winsB = winsB + 1
#         if shutA == True:
#             shutAtot = shutAtot + 1
#         if shutB == True:
#             shutBtot = shutBtot + 1
#     return winsA, winsB, shutAtot, shutBtot
    
# def simOneGame(probA, probB, gameNumber):
#     # Simulate a single game of racquetball between players whose
#     # abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     if gameNumber % 2 == 0:
#         serving = "B"
#     else:
#         serving = "A"
#     scoreA = 0
#     scoreB = 0
#     shutA = False
#     shutB = False
#     while gameOver(scoreA, scoreB) == "A" or gameOver(scoreA, scoreB) == "B" or not gameOver(scoreA, scoreB) :
#         if gameOver(scoreA, scoreB) == "A":
#             shutA = True
#             break
#         elif gameOver(scoreA, scoreB) == "B":
#             shutB = True
#             break
#         elif serving == "A":
#             if random() < probA:
#                 scoreA = scoreA + 1
#             else:
#                 serving = "B"
#         else:
#             if random() < probB:
#                 scoreB = scoreB + 1
#             else:
#                 serving = "A"
    
#     return scoreA, scoreB, shutA, shutB

# def gameOver(a, b):
#     # a and b represent scores of racquetball game
#     # Returns True if the game is over, False otherwise.
#     if a == 0 and b == 7:
#         return "B"
#     if a == 7 and b == 0:
#         return "A"
#     else:
#         return a == 15 or b == 15
    
# def printSummary(m_winsA, m_winsB, n, m, shutAtot, shutBtot):
#     # Prints a summary of wins for each player
#     shutAperc = 0
#     shutBperc = 0
#     if m_winsA > 0:
#         shutAperc = shutAtot/m_winsA
#     if m_winsB > 0:
#         shutBperc = shutBtot/m_winsB
    
#     print("\nAmount of {0} game matches simulated: {1}".format(n,m))
#     print("Wins for A: {0} ({1:0.1%}), Shutouts: {2} ({3:0.1%})".format(m_winsA, m_winsA/m, shutAtot, shutAperc))
#     print("Wins for B: {0} ({1:0.1%}), Shutouts: {2} ({3:0.1%})".format(m_winsB, m_winsB/m, shutBtot, shutBperc))
    
# if __name__ == '__main__' : main()

# EX 9.3
# VOLLEYBALL SIMULATION

# from random import *
# from math import *

# def main():
#     printIntro()
#     x,y,z = getInputs()
#     winA, winB = simulateGames(x,y,z)
#     printResults(winA, winB, z)

# def printIntro():
#     print('\nThis program simulates a Volleyball game! Each game must be played to at least 15 points and the winner must beat his opponent by at least 2 points. Players can only score if they are serving.')

# def getInputs():
#     x = eval(input('\nChance that player A wins a point? '))
#     y = eval(input('Chance that player B wins a point? '))
#     z = int(input('How many games to be played? '))

#     return x,y,z

# def simulateGames(x,y,z):
#     i = 0
#     winA = 0
#     winB = 0
#     while i < z:
#         result = simulateOneGame(x,y)
#         if result:
#             winA = winA + 1
#         elif not result:
#             winB = winB + 1
#         i = i + 1

#     return winA,winB

# def simulateOneGame(x,y):
#     serve = True
#     scoreA = 0
#     scoreB = 0
#     while not gameOver(scoreA,scoreB):
#         if serve:
#             if random() < x:
#                 scoreA = scoreA + 1
#             else:
#                 serve = False
#         elif not serve:
#             if random() < y:
#                 scoreB = scoreB + 1
#             else:
#                 serve = True
    
#     if scoreA > scoreB:
#         return True
#     elif scoreB > scoreA:
#         return False
#     else:
#         print('Game simulation failed') 
            
# def gameOver(scoreA,scoreB):
#     if (scoreA >= 15 or scoreB >= 15) and (abs(scoreA - scoreB) >= 2):
#         return True
#     else:
#         return False

# def printResults(winA,winB,z):
#     champion = 'Tie!'
#     if winA > winB:
#         champion = 'Player A'
#     elif winB > winA:
#         champion = 'Player B'
    
#     print('\nThe score, after {3} games played:\n Player A: {0} \n Player B: {1} \n Winner: {2}'.format(winA,winB,champion,z))

# if __name__ == '__main__' : main()
    

# EX 9.4
# VOLLEYBALL SIMULATION 2.0

# from random import *
# from math import *

# def main():
#     printIntro()
#     x,y,z = getInputs()
#     winA, winB = simulateGames(x,y,z)
#     printResults(winA, winB, z)

# def printIntro():
#     print('\nThis program simulates a Volleyball game! Each game must be played to at least 15 points and the winner must beat his opponent by at least 2 points. Players can only score if they are serving.')

# def getInputs():
#     x = eval(input('\nChance that player A wins a point? '))
#     y = eval(input('Chance that player B wins a point? '))
#     z = int(input('How many games to be played? '))

#     return x,y,z

# def simulateGames(x,y,z):
#     i = 0
#     winA = 0
#     winB = 0
#     while i < z:
#         result = simulateOneGame(x,y)
#         if result:
#             winA = winA + 1
#         elif not result:
#             winB = winB + 1
#         i = i + 1

#     return winA,winB

# def simulateOneGame(x,y):
#     scoreA = 0
#     scoreB = 0
#     while not gameOver(scoreA,scoreB):
#         if random() < x and random() > y:
#             scoreA = scoreA + 1
#         if random() > x and random() < y:
#             scoreB = scoreB + 1
    
#     if scoreA > scoreB:
#         return True
#     elif scoreB > scoreA:
#         return False
#     else:
#         print('Game simulation failed') 
            
# def gameOver(scoreA,scoreB):
#     if (scoreA >= 25 or scoreB >= 25) and (abs(scoreA - scoreB) >= 2):
#         return True
#     else:
#         return False

# def printResults(winA,winB,z):
#     champion = 'Tie!'
#     if winA > winB:
#         champion = 'Player A'
#     elif winB > winA:
#         champion = 'Player B'
    
#     print('\nThe score, after {3} games played:\n Player A: {0} \n Player B: {1} \n Winner: {2}'.format(winA,winB,champion,z))

# if __name__ == '__main__' : main()


# EX 9.5

# EX 9.6

# EX 9.7

# EX 9.8

# EX 9.9

# EX 9.10

# EX 9.11

# EX 9.12

# EX 9.13

# EX 9.14

# EX 9.15

# CHAPTER 10

# EX 10.1
# projectile.py
"""
PROVIDES A SIMPLE CLASS FOR MODELING THE FLIGHT OF PROJECTILES.
"""

from math import sin, cos, radians

class Projectile:

    """SIMULATES THE FLIGHT OF SIMPLE PROJECTILES NEAR THE EARTH'S SURFACE,
    IGNORING WIND RESISTANCE. TRACKING IS DONE IN TWO DIMENSIONS: HEIGHT (Y)
    AND DISTANCE (X). """
    
    def __init__(self, angle, velocity, height):
        """CREATE A PROJECTILE WITH GIVEN LAUNCH ANGLE, INITIAL VELOCITY, AND HEIGHT."""
        
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.maxY = height

    def update(self, time):
        """UPDATE THE STATE OF THIS PROJECTILE TO MOVE IT TIME SECONDS FARTHER INTO
        ITS FLIGHT"""
        
        lastY = self.ypos
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8* time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

        if self.ypos > lastY:
            self.maxY = self.ypos 

    def getY(self):
        "RETURNS THE Y POSITION (HEIGHT) OF THIS PROJECTILE."
        return self.ypos

    def getX(self):
        "RETURNS THE X POSITION (DISTANCE) OF THIS PROJECTILE."
        return self.xpos
    
    def getMax(self):
        "RETURNS THE MAXIMUM HEIGHT THAT WAS OBSERVED FROM REPORTED UPDATES."
        return self.maxY

# CANNONBALL PROGRAM
    
def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))
    return a,v,h,t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    print("\nMaximum height recorded: {0:0.1f} meters.".format(cball.getMax()))

# EX 10.2

# EX 10.3

# EX 10.4

# EX 10.5

# EX 10.6

# EX 10.7

# EX 10.8

# EX 10.8

# EX 10.9

# EX 10.10

# EX 10.11

# EX 10.12

# EX 10.13

# EX 10.14

# EX 10.15

# EX 10.16

# EX 10.17

    
# CHAPTER 11

# CHAPTER 12

# CHAPTER 13
        
        
        
        
