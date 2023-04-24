#Dahan, Regine Fae M. BSCPE 1-5 File Handling #4

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

#if it is odd
#   find the cube of it
#   write it in triple.txt

#display the output
