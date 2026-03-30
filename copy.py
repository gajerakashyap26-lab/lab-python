#copy
src=open("two.txt","r")
data=src.read()

dst=open("one.txt.","w")
dst.write(data)
dst.close()
print("File copied successfully.")