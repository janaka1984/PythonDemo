import os,glob

os.chdir("C:\Users\Janaka\Pictures\kidStore\post")

for file in glob.glob("*.jpg"):
    print file

