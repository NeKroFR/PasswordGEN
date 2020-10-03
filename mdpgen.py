#import
from random import *

#liste caractères
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#generation
def mdp_func (length):
    mdp = ""
    shuffle(characters)
    for x in range (length) :
        mdp+=characters[x]
    print(mdp)

length =int (input('Enter the length:'))
mdp_func(length)
input()
