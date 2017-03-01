import random

user = raw_input("Choose your weapon from rock, paper or scissors : ")
comp = random.choice( ['rock','paper','scissors'] )

print 'the user (you) chose', user
print 'the comp (I) chose', comp

if user == 'rock' and comp =='paper':
    print 'Ha! I really chose paper -- I WIN!'
if user == 'paper' and comp =='scissors':
    print 'Ha! I really chose scissors -- I WIN!' 
if user == 'scissors' and comp =='rock':
    print 'Ha! I chose rock -- I WIN!'
if ((user == 'rock' and comp =='scissors') or (user == 'scissors' and comp =='paper') or (user == 'paper' and comp =='rock')):
    print ' I LOSE :/!'
if ((user == 'rock' and comp =='rock') or (user == 'scissors' and comp =='scissors') or (user == 'paper' and comp =='paper')):
    print ' Its a tie :/!'
