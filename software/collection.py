# -*- coding: utf-8 -*-
import json
import os
import sys
import boto3
import pathlib


client = boto3.client('rekognition')


def create_collection(name='face_db', path='./'):
    response = client.create_collection(CollectionId=name)
    with open(path + 'arn.txt', 'w') as f:
        f.write(response['CollectionArn'] + '\n')
    return response


def delete_collection(name='face_db'):
    response = client.delete_collection(CollectionId=name)
    return response


def register_face(image_file, collection_id='face_db'):
    image_file = str(image_file)
    with open(image_file, 'rb') as f:
        img_b = f.read()
    response = client.index_faces(
        CollectionId=collection_id,
        Image={'Bytes': img_b},
        ExternalImageId=os.path.splitext(os.path.basename(image_file))[0],
        MaxFaces=1
    )
    if len(response['UnindexedFaces']) > 0:
        print('{} contains multiple faces. But some faces weren\'t registered.'.format(image_file), file=sys.stderr)

    if len(response['FaceRecords']) == 0:
        print('{} contains no faces.'.format(image_file), file=sys.stderr)
        return None

    face_id = response['FaceRecords'][0]['Face']['FaceId']
    image_id = response['FaceRecords'][0]['Face']['ImageId']
    ex_image_id = response['FaceRecords'][0]['Face']['ExternalImageId']

    return {image_file: {
        'FaceId': face_id,
        'ImageId': image_id,
        'ExternalImageId': ex_image_id
    }}


def delete_face(face_id, collection_id='face_db'):
    client.delete_faces(
        CollectionId=collection_id,
        FaceIds=[face_id]
    )


def update_db(data_dir, collection_id='face_db'):
    # TODO: if the faces of the same person are already registered, don't register the face or not?
    path = pathlib.Path(data_dir)
    images = list(path.glob('*.png')) + list(path.glob('*.jpg'))

    for image_file in images:
        image_file = str(image_file)
        if not os.path.exists(os.path.splitext(image_file)[0] + '.json'):
            response = register_face(image_file, collection_id)
            if response is None:
                continue
            with open(os.path.splitext(image_file)[0] + '.json', 'w') as f:
                json.dump(response, f)


def authenticate(image_file, collection_id='face_db', threshold=0.95):
    image_file = str(image_file)
    with open(image_file, 'rb') as f:
        img_b = f.read()
    try:
      response = client.search_faces_by_image(
          CollectionId=collection_id,
          Image={'Bytes': img_b},
          MaxFaces=1,
          FaceMatchThreshold=threshold
      )
    except:
      return ('', 0.0)

    if len(response['FaceMatches']) == 0:
        return ('', 0.0)

    return (response['FaceMatches'][0]['Face']['ExternalImageId'], response['FaceMatches'][0]['Similarity'])


# for testing
def main():
    print(delete_collection(), flush=True)
    print(create_collection(), flush=True)
    update_db('/home/pi/workspace/software/db')
    print('DB constructed', flush=True)
    print(authenticate('/home/pi/workspace/software/db/abe.jpg'))


if __name__ == '__main__':
    main()
