# Deforum Stable Diffusion for Huggingface Gradio spaces
# TODO

import gradio as gr

def predict(image):
    print('test')
    return {}

gr.Interface(
    predict,
    inputs=gr.inputs.Image(label="Test image", type="filepath"),
    outputs=[],
    title="Test",
).launch()
