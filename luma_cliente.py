import os
from lumaai import LumaAI

client = LumaAI(auth_token=os.environ["LUMAAI_API_KEY"])

def get_video_links():
    generations = client.generations.list()
    return [
        gen.assets.video for gen in generations.generations
        if gen.assets and gen.assets.video
    ]
