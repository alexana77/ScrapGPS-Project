import os
import glob
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
from pytesseract import Output
import pandas as pd


def create_key(name):
    name = name.replace('_', ' ')
    if name.find("-") == 4:
        name_parts = name.split(' ')
        date_reverse = '-'.join(name_parts[0].split('-')[::-1])
        name = date_reverse + ' ' + name_parts[1]
    if name.count('-') > 3:
        name = name[0:name.rfind('-')]
    name = ':'.join(name.rsplit('-', 2))
    return name


custom_config = r'--oem 2 --psm 6'
image_list = []
image_list = [image for image in glob.glob("C:\\Users\\User\\Desktop\\NavStar49_24hours\\together\\*.jpeg")]
print('num of images is {}'.format(len(image_list)))
# dict_img = dict.fromkeys(set(image_list), [])
texts = [(img, pytesseract.image_to_string(cv2.imread(img), lang='eng', config=custom_config)) for img in image_list]
for ind, text in enumerate(texts):
    if not text:
        print(ind)
        texts[ind] = (image_list[ind], pytesseract.image_to_string(cv2.imread(image_list[ind]), lang='eng',
                                                                   config=custom_config))

dict_img = {create_key(key.split('\\')[-1].split('.jpeg')[0]): value for key, value in texts}

params_dict = {
    "altitude": "km",
    "velocity": "km/s"
}
gps_observations_dict = dict.fromkeys(dict_img.keys(),{})


for k_img, v_img  in dict_img.items():
    local_params_dict={}
    for k_param, v_param in params_dict.items():
        first_ind = v_img.lower().find(k_param)
        last_ind = v_img.lower().find(v_param, first_ind)
        list_of_words = v_img[first_ind:last_ind].strip().split()
        if len(list_of_words) == len(params_dict):
            local_params_dict[k_param] = float(list_of_words[-1])
    if len(local_params_dict) == len(params_dict):
        gps_observations_dict[k_img] = local_params_dict
print(gps_observations_dict)

gps_observations = pd.DataFrame.from_dict(gps_observations_dict, orient='index')
# print(gps_observations_dict)
gps_observations.to_excel('C:\\Users\\User\Desktop\\NavStar49_24hours\\NAVSTAR49_observations_Jan31_Feb01.xlsx')
