def getEbookContent(file):
  openedFile = open(file)
  lines = openedFile.readlines()
  book = isolateBook(lines)
  return book

def isolateBook(lines, bookStarted = False, book = []):
 for x in range(len(lines)): 
    if bookStarted == True:
      book.append(lines[x])
    if checkForStart(lines[x]) == True:
      bookStarted = True
      print("True")
    if checkForEnd(lines[x]) == True:
      bookStarted = False
      print("True")
 return book
      
def checkForStart(line):
  if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:
    return True
  return False

def checkForEnd(line):
  if "*** END OF THIS PROJECT GUTENBERG EBOOK" in line:
    return True
  return False

