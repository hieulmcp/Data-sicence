
from PIL import Image

def upload_img_video(icon, image, video, audio_file, choose_rb = "rb"):
    lists = []
    icon = Image.open(icon)
    image = Image.open(image)
    video_file = open(video, choose_rb)
    video = video_file.read()
    audio_file = open(audio_file, choose_rb)
    audio = audio_file.read()
    lists.append(icon)
    lists.append(image)
    lists.append(video)
    lists.append(audio)

    return lists
    