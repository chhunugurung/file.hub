fname = input("Enter the name of file:")
try:
   fhand = open(fname)
except:
    print("The Input file does not exist.",fname)
else:
    line_number = 1       
    for line in fhand:
        print(f'LINE NUMBER : {line_number}\n{line.upper()}')
        line_number = line_number + 1
        fhand.close()
