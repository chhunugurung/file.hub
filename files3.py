fname = input("Enter the file name:")
fname = input("Enter the file name:")
fhand = open (fname, "r")
Total_spam_confidence = 0
count = 0
for  line in fhand:
    if line.startswith("X-DSPAM-Confidece:0.8475:"):
        line = line.rstrip()
        Total_spam_confidence += 1
        count += 1
if count > 0:
    average_spam_confidense = Total_spam_confidence / count
    print("The average confidence is:", average_spam_confidense)
else:
    print("Not found.")

