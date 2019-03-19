def main():
    i=1
    value="0"
    while i:
        print("Selection Menu:")
        print("0. Exit Program")
        print("1. Read from a file.")
        print("2. Write integers to a file.")
        print("3. Append integers to a file.")
        answer=input("What would you like to do? ")
        if answer=="0":
            break
        elif answer=="1":
            readFile=input("Please enter a file name: ")
            in_file=checkFile(readFile)
            line=in_file.readline()
            while line !='':
                print(line)
                line=in_file.readline()
            in_file.close
        elif answer=="2":
            writeFile=input("Enter a file you'd like to write to: ")
            in_file=open(writeFile,'w')
            value=input("Enter in a number or done to finish: ")
            while (value != 'done'):
                value = checkInt(value)
                if value!=False:
                    in_file.write(str(value)+"\n")
                value=input("Enter in a number or done to finish: ")
            in_file.close()
        elif answer=="3":
            writeFile=input("Enter a file you'd like to amend to: ")
            in_file=open(writeFile,'a')
            while (value != 'done'):
                value=(input("Enter in a number: "))
                in_file.write(str(checkInt(value)))
                value=input("Type done if done, if not enter any key to continue: ")
            in_file.close()

def checkFile(file_name):
    try:
        in_file=open(file_name,"r")
        return in_file
    except:
        print("Please enter a valid file name")
        return False
    
def checkInt(value): 
    try:
        valid_int=value
        valid_int_final=int(valid_int)
        return valid_int
    except:
        return False
        
    

main()
