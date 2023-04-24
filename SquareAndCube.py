#Dahan, Regine Fae M. BSCPE 1-5 File Handling #4

#introduction
import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()
print(Fore.LIGHTRED_EX+pyfiglet.figlet_format("HEY",font="isometric1"))
time.sleep(1)
border = "—" * 100
print(border)
print(Fore.LIGHTBLUE_EX+' This Program is entitled Square And Cube. For it will square the even, and cube the odd! ')
print(border)
time.sleep(2)

#open integers.txt,create double.txt and triple.txt
with open("integers.txt", "r") as integers_file, open("double.txt", "a") as squared_file, open("triple.txt", "a") as cubed_file:

#read integers.txt
    for line in integers_file:
        print(line.strip())
        integers_file = int(line)

#if it is even
        if integers_file % 2 != 1:
                    
#   find the square of it
            int_squared = integers_file ** 2

#   write it in double.txt
            squared_file.write(str(int_squared) + "\n" )

#if it is odd
        else:
           
#   find the cube of it
           int_cubed = integers_file ** 3

#   write it in triple.txt
           cubed_file.write(str(int_cubed) + "\n" )

#display the output
print(border)
time.sleep(2)
print(Fore.GREEN+pyfiglet.figlet_format("The Square of Even...",font="digital"))
time.sleep(2)

with open("double.txt", "r") as squared_file:
    for line in squared_file:
        print("*"*5)
        print(line.strip())

print(border)
time.sleep(2)
print(Fore.CYAN+pyfiglet.figlet_format("The Cube of Odd...",font="digital"))
time.sleep(2)

with open("triple.txt", "r") as cubed_file:
    for line in cubed_file:
        print("*"*5)
        print(line.strip())

#outro
print(border)
time.sleep(2)
print(Fore.LIGHTRED_EX+pyfiglet.figlet_format("LET'S GO",font="isometric1"))


