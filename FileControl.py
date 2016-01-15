import os
# os.path.join('usr', 'bin', 'spam')

# Get current directory #
os.getcwd()

# Change current directory #
os.chdir('/Users/kakeman/Documents/Python')

# Append directory to file name #
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/Users/kakeman/Documents/Python', filename))

# Make Directory #
os.makedirs('delicious/walnut/waffles')



