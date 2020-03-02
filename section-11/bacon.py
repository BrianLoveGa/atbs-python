# use python to do what i've been typing into terminal on mac
# perhaps easier than windows shell / command line

# >> > baconFile = open('bacon.txt', 'w')
# >> > baconFile.write('Hello, world!\n')
# 13
# >> > baconFile.close()
# >> > baconFile = open('bacon.txt', 'a')
# >> > baconFile.write('Bacon is not a vegetable.')
# 25
# >> > baconFile.close()
# >> > baconFile = open('bacon.txt')
# >> > content = baconFile.read()
# >> > baconFile.close()
# >> > print(content)
# Hello, world!
# Bacon is not a vegetable.

# >> > import shelve
# >> > shelfFile = shelve.open('mydata')
# >> > cats = ['Zophie', 'Pooka', 'Simon']
# >> > shelfFile['cats'] = cats
# >> > shelfFile.close()

# To read and write data using the shelve module, you first import shelve. Call shelve.open() and pass it a filename, and then store the returned shelf value in a variable. You can make changes to the shelf value as if it were a dictionary. When you’re done, call close() on the shelf value. Here, our shelf value is stored in shelfFile. We create a list cats and write shelfFile['cats'] = cats to store the list in shelfFile as a value associated with the key 'cats' (like in a dictionary). Then we call close() on shelfFile. Note that as of Python 3.7, you have to pass the open() shelf method filenames as strings. You can’t pass it Path object.

# After running the previous code on Windows, you will see three new files in the current working directory: mydata.bak, mydata.dat, and mydata.dir. On macOS, only a single mydata.db file will be created.

#/<--! lots of tiny little differences on MAC vs Windows machines, wonder which I'll have at work



# can also zip and unzip in python
# For example, enter the following into the interactive shell:

#    >> > import zipfile, os

#    >> > from pathlib import Path
#    >> > p = Path.home()
#    >> > exampleZip = zipfile.ZipFile(p / 'example.zip')
#    >> > exampleZip.namelist()
#    ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
#    >> > spamInfo = exampleZip.getinfo('spam.txt')
#    >> > spamInfo.file_size
#    13908
#    >> > spamInfo.compress_size
#    3828
# ➊ >> > f'Compressed file is {round(spamInfo.file_size / spamInfo
#                                    .compress_size, 2)}x smaller!'
# )
#     'Compressed file is 3.63x smaller!'
#     >> > exampleZip.close()

#########################################

#   >> > import zipfile, os
#   >> > from pathlib import Path
#   >> > p = Path.home()
#   >> > exampleZip = zipfile.ZipFile(p / 'example.zip')
# ➊ >> > exampleZip.extractall()
# >> > exampleZip.close()
