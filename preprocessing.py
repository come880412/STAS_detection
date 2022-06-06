import xml.etree.ElementTree as ET

import random
import numpy as np
import shutil
import os
import tqdm

from sklearn.model_selection import train_test_split

seed = 20220428

np.random.seed(seed)
random.seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)
if __name__ == '__main__':
    save_dir = '../../../dataset/yolo_0.95/lung_cancer'
    train_size_ratio = 0.95
    os.makedirs(os.path.join(save_dir, 'images/train'), exist_ok=True)
    os.makedirs(os.path.join(save_dir, 'labels/train'), exist_ok=True)
    os.makedirs(os.path.join(save_dir, 'images/valid'), exist_ok=True)
    os.makedirs(os.path.join(save_dir, 'labels/valid'), exist_ok=True)

    data_path = '../../../dataset'

    data_list = os.listdir(os.path.join(data_path, 'Train_Annotations_OBJ'))                                                                                                   

    train_data, valid_data = train_test_split(data_list, random_state=seed, train_size=train_size_ratio)
    
    class_type = 0                                                                                                          
    for name in tqdm.tqdm(data_list):
        data_name = name[:-4]

        tree = ET.parse(os.path.join(data_path, 'Train_Annotations_OBJ', name))
        root = tree.getroot()

        for neighbor in root.iter('size'):
            img_width, img_height = int(neighbor[0].text), int(neighbor[1].text)

        obj_bbx = []
        for neighbor in root.iter('object'):
            tmp_bbx = []
            obj_name = neighbor[0].text
            for i in range(len(neighbor[4])):
                tmp_bbx.append(int(neighbor[4][i].text))
            x_min, y_min, x_max, y_max = tmp_bbx
            x_center, y_center = (x_max + x_min) / 2, (y_max + y_min) / 2
            normalized_width, normalized_height = str((x_max - x_min) / img_width), str((y_max - y_min) / img_height)
            normalized_x_center, normalized_y_center = str(x_center / img_width), str(y_center / img_height)

            obj_bbx.append([str(class_type), normalized_x_center, normalized_y_center, normalized_width, normalized_height]) # (x_min, y_min, x_max, y_max)
        # image = cv2.imread(os.path.join(data_path, 'Train_Images', data_name+'.jpg'))

        if name in train_data:
            shutil.copyfile(os.path.join(data_path, 'Train_Images', data_name+'.jpg'), os.path.join(save_dir, 'images', 'train', data_name+'.jpg'))
            # cv2.imwrite(os.path.join(save_dir, 'images', 'train', data_name+'.png'), image)
            np.savetxt(os.path.join(save_dir, 'labels', 'train', data_name+'.txt'),  obj_bbx, fmt='%s', delimiter=' ')
        elif name in valid_data:
            shutil.copyfile(os.path.join(data_path, 'Train_Images', data_name+'.jpg'), os.path.join(save_dir, 'images', 'valid', data_name+'.jpg'))
            # cv2.imwrite(os.path.join(save_dir, 'images', 'valid', data_name+'.png'), image)
            np.savetxt(os.path.join(save_dir, 'labels', 'valid', data_name+'.txt'),  obj_bbx, fmt='%s', delimiter=' ')
    
    print('---------------------Statistics---------------------')
    print('Number of training data: ', len(train_data))
    print('Number of validation data: ', len(valid_data))
        
        
        

    

