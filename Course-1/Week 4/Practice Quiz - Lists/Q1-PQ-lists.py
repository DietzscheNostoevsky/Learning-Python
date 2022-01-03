filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []

for file in filenames :
	if file.endswith('.hpp') : 

		l = len(file)
		newfile = file[:l-2]
		newfilenames.append(newfile)

	else : 
		newfilenames.append(file)
			

# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
  

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]