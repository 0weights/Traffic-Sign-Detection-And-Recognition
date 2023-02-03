import os

image_files = []
# os.chdir(os.path.join("data", "obj"))
for filename in os.listdir('E:/programs/lab/Images'):
    if filename.endswith(".jpeg"):
        image_files.append("data/obj/" + filename)
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()