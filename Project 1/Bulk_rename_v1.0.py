# importing libraries 
import os
import re

# Function to rename multiple files 
def rename_files(path):
    try:
        total_files = str(len(os.listdir(path))) ## Total number of files
        if(total_files == '0'):
            print("\n\nFolder is empty.")
            return False
    except WindowsError:
        print("\n\n[WinError 5] Access is denied: "+path)
        return False
    name_con = input("Enter the naming convention: ")
    name_con = re.sub('[^A-Za-z0-9 _\(\)\{\}\[\]\-]+', '', name_con) ## allow only A-Z, a-z, 0-9 and some special characters
    print("Your naming convention: "+name_con)
    while True:
        confirmation = input("\n\nThere are total "+total_files+" files. Do you want to rename all? [y/n]").lower() ## getting confirmation from user
        if(confirmation == 'y'):
            for count, filename in enumerate(os.listdir(path)):
                src = path + '/' + filename ## source filename
                extension = os.path.splitext(filename)[1] ## extention of the source file
                dst = path +'/'+ name_con + str(count+1).zfill(len(total_files)) ##naming convention
                try: ## renaming file
                    os.rename(src, dst + extension) 
                except: ## if filename already exists, Create temporary filename
                    temp_count = 2
                    while True:
                        print("\n \nFilename already exists:" ,dst+extension)
                        temp_name = dst+" ("+str(temp_count)+")"+extension
                        print("Trying: ",temp_name)
                        try:
                            os.rename(src, temp_name)
                            print("Filename changed to: ",temp_name)
                            break
                        except:
                            temp_count+=1
            print("\n\n----- Rename Successful -----\n\n")
            break
        elif(confirmation == 'n'):
            print("\nRename Skipped")
            break
        else:
            print("\nPlease enter a valid choice")
        
## Main Function 
if __name__ == '__main__':
    print("----Program Started----")
    while True:
        try:
            print("Use Ctrl+C to closed the Program.") 
            path = input("Enter the directory path: ") 
            if(os.path.exists(path)):
                if(os.path.isdir(path)):
                    print("It is a directory")
                    rename_files(path)
                else:
                    print("It is a file. Please enter a directory path\n\n")
            else:
                print("\nThis path doesn't exist\n\n")
        except KeyboardInterrupt:
            print("----Program closed----")
            break
        
