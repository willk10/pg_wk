import pyautogui as pg
import time
import webbrowser

points=0

# Question
answer = pg.prompt(
"""
Which would you rather do?

a) Read Macbeth
b) Watch Netlix
c) Watch harry potter movies
"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 3
elif answer == "b":
    points += 2
elif answer == "c":
    points += 1
    
# Question
answer = pg.prompt(
"""
Who is your role model?

a) Macbeth
b) Steve Jobs
c) J.K. Rowling
"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 3
elif answer == "b":
    points += 2
elif answer == "c":
    points += 1
    
    # Question
answer = pg.prompt(
"""
What is your favorite book you have read this year?

a) Macbeth 
b) Top Man
c) Harry Potter
"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 3
elif answer == "b":
    points += 2
elif answer == "c":
    points += 1
    
    # Question
answer = pg.prompt(
"""
Who is your favorite Author?

a) Shakespeare
b) John Stienbeck
c) J.K. Rowling
"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 3
elif answer == "b":
    points += 2
elif answer == "c":
    points += 1




# END OF SURVEY
pg.alert("You are ...")

# Macbeth Fan should be a
if points >= 10:
    pg.alert('Macbeth Fan!')
    webbrowser.open("https://www.youtube.com/watch?v=zt13FbL1xyw")
# A Typical student should be b
elif points < 10 and points >= 7:
    pg.alert("A typical student!")
    webbrowser.open("https://www.youtube.com/watch?v=azSPB7dMfjc")

# Harry Potter fan should be c
elif points < 7:
    pg.alert("Harry Potter Fan!")
    webbrowser.open("https://www.youtube.com/watch?v=Tx1XIm6q4r4")
