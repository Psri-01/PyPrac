filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
#newfilenames = [x for x in filenames if x.endswith('.hpp')]
newfilenames = [x.replace('.hpp', '.h') if x.endswith('.hpp') else x for x in filenames]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
