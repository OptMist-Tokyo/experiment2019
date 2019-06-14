# -*- coding: utf-8 -*-
import io
import math
import os
import sys
import boto3
import pathlib
from PIL import Image


client = boto3.client('rekognition')

# concatenate a few images to reduce the number of API calls
# original images should be square. h = w is desirable.
# if h=w=2, arrange like
# |0, 1|
# |2, 3|
def concat_images(image_list, h, w):
    assert len(image_list) <= h * w
    person_list = []
    img_width = 1290 // w
    img_height = 1290 // h
    dst = Image.new('RGB', (img_width * w, img_height * h))
    for i, image_file in enumerate(image_list):
        image_file = str(image_file)
        name = os.path.splitext(image_file)[0]
        person_list.append(name)

        left = i % w
        top = i // w
        img_b = Image.open(image_file).resize((img_width, img_height))

        dst.paste(img_b, (img_width * left, img_height * top))

    img_binary = io.BytesIO()
    dst.save(img_binary, format='PNG')
    img_binary = img_binary.getvalue()
    return img_binary, person_list # pair of an image and persons list containing who's in the image


# 元が誰の画像だったかをbounding boxの位置から復元
def identify(src_b, tgt_b, person_list, h, w):
    response = client.compare_faces(
        SourceImage={'Bytes': src_b},
        TargetImage={'Bytes': tgt_b}
    )
    if len(response['FaceMatches']) == 0:
      return ('', 0.0)
    sim_score = response['FaceMatches'][0]['Similarity']
    bbox = response['FaceMatches'][0]['Face']['BoundingBox']
    center_top = bbox['Top'] + 0.5 * bbox['Height']
    center_left = bbox['Left'] + 0.5 * bbox['Width']

    i = 0
    i += math.floor(center_top * h) * w
    i += math.floor(center_left * w)

    return (person_list[i], sim_score)


# 認証の閾値はとりあえず0.95あたりを使う。後から変えるかも。
def authenticate(image_file, data_dir, h=2, w=2, threshold=0.95):
    path = pathlib.Path(data_dir)
    result = ('', 0.0)

    with open(image_file, 'rb') as src_image:
        src_b = src_image.read()
        tgt_images = list(path.glob('*.png')) + list(path.glob('*.jpg'))

        for i in range(0, len(tgt_images), h * w):
            sub_images = tgt_images[i: i + h * w]

            tgt_b, person_list = concat_images(sub_images, h, w)
            cand = identify(src_b, tgt_b, person_list, h, w)
            if cand[1] > result[1]:
                result = cand

    if result[1] < threshold:
        return ('', 0.0)

    return result


# for testing
# print(authenticate('ken.jpg', './'))
