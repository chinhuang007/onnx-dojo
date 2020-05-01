import json
import numpy as np
import tensorflow as tf
import onnx
import onnx_tf

# convert the onnx model into Tenserflow representation
model = onnx.load('resnet152v2.onnx')
tf_rep = onnx_tf.backend.prepare(model, logging_level='WARN')

images = ['ant.jpg', 'bee.jpg']
index_json_file='imagenet_class_index.json'

# load the image classification from json file
with open(index_json_file) as f:
  class_index = json.load(f)

# central crop an image with height and width
def _central_crop(image, crop_height, crop_width):
  shape = tf.shape(image)
  height, width = shape[0], shape[1]
  crop_top = (height - crop_height) // 2
  crop_left = (width - crop_width) // 2
  image = tf.image.crop_to_bounding_box(image,
          crop_top, crop_left,
          crop_height, crop_width)
  return image

# predict one image at a time
for image_path in images:
  # load the image file, decode jpeg, and crop to the size 224x224
  img = tf.io.read_file(image_path)
  img = tf.image.decode_jpeg(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)
  img = tf.image.resize(img, (256, 256))
  img = _central_crop(img, 224, 224)
  img = tf.transpose(img, perm=[2, 0, 1])
  img = tf.expand_dims(img, 0)

  # use numpy() to produce the python input
  input_image=img.numpy()

  # run the model with the processed image
  tf_output = tf_rep.run(input_image)

  # use argmax to get the index/class ID with highest value in output
  output = np.argmax(tf_output)

  # print the input image file name
  print('The image file is ', image_path)

  # the output is the classification code
  print('predicted class ID = ', output)

  # the class name is coming from the index json file
  print('predicted class name = ', class_index[str(output)][1])
