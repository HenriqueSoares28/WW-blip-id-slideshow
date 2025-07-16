import time
import json
from luma_client import get_video_links

INTERVALO = 30

def atualizar_continuamente():
    while True:
        links = get_video_links()
        with open("lista.json", "w") as f:
            json.dump(links, f)
        print(f"[✓] Atualizado com {len(links)} vídeos.")
        time.sleep(INTERVALO)

if __name__ == "__main__":
    atualizar_continuamente()
