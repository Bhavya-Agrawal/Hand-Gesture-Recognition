""" Main file to run hand gesture recognition """
import os
import cv2
sign_dict = {}
main_folder = os.listdir('.Indian')

############## ----- To get the files from respective folders ---- ##########
# # get signs in respective folders
# for sign_folder in main_folder:
#     # path = os.path.join(main_folder, sign_folder)
#     for file in os.listdir('.Indian/{sign_folder}'.format(sign_folder=sign_folder)):
#         # print(file)
#         if not sign_dict.get(sign_folder):
#             sign_dict[sign_folder] = []
#         folder = sign_dict.get(sign_folder)
#         folder.append(file)
# # for k, v in sign_dict.items():
# #     print(k, len(v))
#
# labels = sign_dict.keys()
# # print(labels)
# # print(len(sign_dict.get('1')))


######### ---------- Spliiting the actual dataset into train, test, validation dataset --------- #########3
# split files as training, testing, validation sets
# import splitfolders
# splitfolders.ratio('../Indian',
#                    output = 'ISL',
#                    seed = 22, ratio = (.7,.2,.1))


###### --------- pre-processing the images in train and validation folders ------- #######
learning_folders = ['./ISL/train', './ISL/val']
for folder in learning_folders:
    for numerical_folder in os.listdir(folder):
        image_folder=os.path.join(folder, numerical_folder)
        for image_file in os.listdir(image_folder):
            # print(image_files)
            # convert all images to grayscale
            image_path = os.path.join(image_folder, image_file)
            frame = cv2.imread(image_path)
            # print(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5,5), 2)
            th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            ret, res = cv2.threshold(th3, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            if os.path.exists(image_file):
                os.path.remove(image_file)
            cv2.imwrite(image_path, res)

