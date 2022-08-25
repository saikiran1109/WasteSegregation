import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflow.keras as keras
import keras.applications.xception as xception
from tensorflow.keras.models import load_model
 
# load model
model = load_model('model804.h5')

classnames = ['battery','cardboard','clothes','food','glass','medical','metal','paper','plastic','shoes']



def predict_image(img):
  img_4d=img.reshape(-1,320, 320,3)
  prediction=model.predict(img_4d)[0]
  return {classnames[i]: float(prediction[i]) for i in range(10)}

image = gr.inputs.Image(shape=(320, 320))
label = gr.outputs.Label(num_top_classes=3)
enable_queue=True
examples = ['battery.jpg','cardboard.jpeg','clothes.jpeg','glass.jpg','metal.jpg','plastic.jpg','shoes.jpg']
article="<p style='text-align: center'>Made by Aditya Narendra with 🖤</p>"

gr.Interface(fn=predict_image, inputs=image,  title="Garbage Classifier",
    description="This is a Garbage Classification Model Trained using Xception Net on DS11 Mod(Seg10 V4).Deployed to Hugging Faces using Gradio.",outputs=label,article=article,enable_queue=enable_queue,examples=examples,interpretation='default').launch(share="True")