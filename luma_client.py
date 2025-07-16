import os
from lumaai import LumaAI
from dotenv import load_dotenv

load_dotenv()

client = LumaAI(auth_token=os.environ["LUMAAI_API_KEY"])

def get_video_links():
    generations = client.generations.list(limit=200)
    return [
        gen.assets.video for gen in generations.generations
        if gen.assets and gen.assets.video
    ]
