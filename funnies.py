# Created by MindaMan in 2026, subject to the MIT License. Github found at MindaManOfficial/funnies

import random # Import base library to shuffle the array's contents
import operator # dont know if this is relevant, just remember that it was important at one point

# Delete past file contents
f = open('funnies.txt', 'r+') # Open the file
f.truncate(0) # Remove all contents
f.close() # Close the file

# Create list of the "funnies"
# Each entry should have ""s around it, and a comma to prevent issues
# Emojis are supported, please use a font that has emoji support in OBS
# For entries with ""s in the actual funny, use ''s then embed with ""s
array = ([
"this is an example funny",
"you can do all kinds of things with this script!",
"emoji's are supported! 😀😀",
"Created by MindaMan because he is a super cool guy",
'"Subscribe to mindaman i guess" -MindaMan',
    ])

random.shuffle(array) # Randomly shuffles the array of funnies
arrayFull = '       •       '.join(array) # Adds a divider inbetween the funnies entries, make them look better in production

output = arrayFull[:3000] # Limits the total output to 3000 characters to not break OBS text sources (Limited to ~3299 Characters)

# Attempts to cut out any potentially cut off entries | BROKEN
for i in output:
  if not output.endswith("•"):
    output = output[:-1]
  else:
    break

output = str(output) + "       "

# Writes output to file 
f = open('funnies.txt', 'w', encoding="utf-8") #Opens the file, with emoji output support
f.write(output) # Writes the file contentes
f.close() #Closes the file

# Created, Designed, and Maintained by MindaMan in 2026
# Open sourced with the MIT License
# Created for the OBS Text Source
# Github: https://github.com/MindaManOfficial/funnies
# Website: https://mindaman.com
# More Projects: https://projects.mindaman.com
# YouTube: https://youtube.com/@mindaman?sub_confirmation=1
