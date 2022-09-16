import os
from glob import glob
import cv2

# trydataset = glob(r'D:\dataset try2\2\*')
# # print(len(trydataset))
# final = []
# for i in trydataset:
#     img1 = cv2.imread(i)
#     print(i)
#     # print(img1)
#     k = i.split('\\')[-2] + '_' + i.split('\\')[-1]
#     l = i.split('\\')[0:-1]
#     r = '\\'.join(l)
#     new_name = r + '\\' + k
#     print(new_name)
#     final.append(new_name)
#     cv2.imwrite(new_name, img1)
#     os.remove(i)


# D:\HAND RECOGNITION SYSTEMS\Datasets\TRY DATASET\Labels
tryLabels = glob(r'D:\dataset try2\Labels\2\*')

finalLabels = []
for i in tryLabels:
    print(i)
    k = i.split('\\')[-2] + '_' + i.split('\\')[-1]
    l = i.split('\\')[0:-1]
    r = '\\'.join(l)
    new_name = r + '\\' + k
    print(new_name)
    finalLabels.append(new_name)
    print()
    with open(i, 'r') as firstfile, open(new_name, 'a') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    os.remove(i)
