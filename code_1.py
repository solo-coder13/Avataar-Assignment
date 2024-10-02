from diffusers import StableDiffusionPipeline # type: ignore
import torch
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cuda")
pipe.set_seed(12345) # Fixed seed
from diffusers import StableDiffusionControlNetPipeline,ControlNetModel
controlnet_model = ControlNetModel.from_pretrained("controlnet-depthmodel").to("cuda")
controlnet_pipe = StableDiffusionControlNetPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", controlnet=controlnet_model).to("cuda")
from PIL import Image
depth_map = Image.open("path_to_depth_map.png")
prompt = "Your text prompt from metadata"
output = controlnet_pipe(prompt=prompt, depth_map=depth_map).images[0]
output.save("output_image.png")