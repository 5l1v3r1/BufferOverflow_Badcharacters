#!/usr/bin/python
pattern_file = open("pattern.txt","r")
pattern = pattern_file.read()
pattern_file.close()
pattern = pattern.replace("x","")
pattern = pattern.replace("\\","")
a = pattern
b = list(a)

#file = open("Original_Badcharacters.csv", "a+")

def bad(i1,i2,i):
	while (i > 0):
		z = b[i2]+b[i1]
		print z.upper()
		#file.write(z.upper())
                #file.write("\n")
		i1 = i1 - 2 #6-2=4
		i2 = i2 - 2 #7-2=5
		x = b[i2]+b[i1]
		print x.upper()
		#file.write(x.upper())
                #file.write("\n")
		i1 = i1 - 2
		i2 = i2 - 2
		i = i - 2


def main():
	i1 = 7
	i2 = 6
	i = 4
	bad(i1,i2,i)
	try:
		while (i1 < 530):
			i1 = i1 + 8
        		i2 = i2 + 8
        		i = 4
			bad(i1,i2,i)
	except:
		print "Completed...Now run Stack_Badcharacter.py...copy both result in provided excel sheet and compare the results."

if __name__ =='__main__':
        main()
