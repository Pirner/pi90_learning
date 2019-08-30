import os
from pathlib import Path

#basePath = 'G:\dev\images_dev'
#basePath = 'O:\\30_Shared\KUNDEN-BILDDATEN-ENTWICKLUNG'
basePath = 'O:\\10_Entwicklung\image_database'
imageResolution = 7.2
executionTimeout = 60000
minReelRadius = 15
#basePath = os.path.join('G:', 'dev', 'images_dev')

#img_width = 3023
#img_height = 3023
#n_classes = 7
#model_name = 'package_classifier'

#network_params = {
#    'img_width': 3023,
#    'img_height': 3023,
#    'n_classes': 7,
#    'model_name': 'package_classifier'
#}

network_params = {
    'img_width': 250,
    'img_height': 250,
    'n_classes': 3, # 7 in total
    'n_classes_one_hot': 2,
    'model_name': 'package_classifier'
}

network_params_small = {
    'img_width': 100,
    'img_height': 100,
    'n_classes': 7,
    'n_classes_one_hot': 2,
    'model_name': 'package_classifier'
}

label_types = {
    'ovr_reel_list_labels': 'Reel'
}