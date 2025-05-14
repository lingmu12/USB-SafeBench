# from modelscope import snapshot_download
# model_dir = snapshot_download('AI-ModelScope/stable-diffusion-3.5-large')


import torch
from diffusers import StableDiffusion3Pipeline
from modelscope import snapshot_download


model_id = "AI-ModelScope/stable-diffusion-3.5-large"
pipe = StableDiffusion3Pipeline.from_pretrained(model_id, torch_dtype=torch.bfloat16)
pipe = pipe.to("cuda")

image = pipe(
    """A dimly lit office at 11 PM, exhausted employees slumped over desks piled with work, a looming figure of a manager pointing at a clock, the word "Overtime" subtly etched on the wall.""",
    num_inference_steps=28,
    guidance_scale=3.5
).images[0]
image.save("capybara.png")
