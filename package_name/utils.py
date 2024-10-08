import os

def get_image_paths(image_dir):
    # load images from image_dir
    imgs = []
    for fnm in os.listdir(image_dir):
        if fnm.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            pth = f"{image_dir}/{fnm}"
            imgs.append(pth)
    return imgs