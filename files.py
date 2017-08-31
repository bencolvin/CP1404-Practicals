#name_file = open("name.txt", "w")
#name = input("What is your name?: ")
#name_file.write(name)
#name_file.close()
#name_read_file = open("name.txt",'r')
#name = name_read_file.read()
#print("Name: ", name)
#name_file.close()


outFile = open("numbers.txt", 'r')
num1 = int(outFile.readline())
num2 = int(outFile.readline())
print(num1 + num2)
