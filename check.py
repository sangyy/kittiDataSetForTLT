import os
count=0
path1 = os.path.expandvars('$HOME')+"/kittiDataSetForTLT/kittiDataset/training/images/"
for i, filename in enumerate(os.listdir(path1)):
    with open(os.path.join(path1,filename), 'rb') as imageFile:
        if imageFile.read().startswith(b'BM'):
            print(f"{i}: {filename} - found!")
        else:
            count=count+1
            
        #print("***")
print(count,"ok!")