
file_path = 'example_file.txt'

data = (1,2,3,4,5,6,7)







   
#Open the file and write the lines
with open(file_path, 'w') as file:
     for line in data:
         file.write(str(line) + '\n')
        
#Close the file?
 
print(f"Lines added to {file_path}")



