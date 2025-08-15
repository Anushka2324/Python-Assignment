def copy_file(source,destination):
    try:
        with open(source,'r') as src:
            contents=src.read()
        with open(destination,'w') as des:
            des.write(contents)  
        print("Contents have been copied")     
    except FileNotFoundError:
        print("File not found")
    except IOError as e:
        print(e)    
            
source=input("Enter source file: ")  
destination=input("Enter destination file: ") 
 
copy_file(source,destination)     
      