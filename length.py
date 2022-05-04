name = input("Enter a name: ")
count = 0
for s in name:
      count = count+1
print("Length of the name is:", count)
#----------------------------------
name1 = len([10, 20, 30])
print("The length of list is: ", name1)
#---------------------------------
def str_len(language):
      count = 0
      for i in language:
            count= count + 1
      return count

language = "JournalDev"
print("Length =", str_len(language))