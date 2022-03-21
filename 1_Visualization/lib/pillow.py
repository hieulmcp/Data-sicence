from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFilter, ImageEnhance
import pandas as pd


# Hàm
# Load file dữ liệu
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def pillow(image, icon, option="Show Image", width=12, height=10, size1=300, size2=300, rotate=90, box = (50, 100, 200, 200), position = (0, 300), enhance=2, axis="off", name_save="defaut.png"):
    option = [
            "Show Image",
            "Rotate Image",
            "Create Thumbnail",
            "Crop Image",
            "Merge Images",
            "Flip Image",
            "Black & White",
            "Filters - Sharpen",
            "Filters - Edge Enhance",
            "Contrast Image"]

    image = Image.open(image)

    plt.figure(figsize=(width, height))

    if option == "Show Image":
        chart = plt.imshow(image)
        plt.axis(axis)
        plt.show()
        return chart
    elif option == "Rotate Image":
        rotated_image = image.rotate(rotate)
        chart = plt.imshow(rotated_image)
        plt.axis(axis)
        plt.show()
        return chart
    elif option == "Create Thumbnail":
        size = size1, size2
        chart = image.thumbnail(size)
        image.save(name_save)
        plt.imshow(image)
        plt.axis(axis)
        plt.show()
        return chart
    elif option == "Crop Image":
        box = box
        cropped_image = image.crop(box)
        plt.imshow(cropped_image)
        plt.axis(axis)
        plt.show()
        return cropped_image
    elif option == "Merge Images":
        logo = Image.open(icon)
        position = position
        chart = image.paste(logo, position, logo)
        plt.imshow(image)
        plt.axis(axis)
        plt.show()
        return chart
    elif option == "Flip Image":
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        plt.imshow(flipped_image)
        plt.axis(axis)
        plt.show()
        return flipped_image
    elif option == "Black & White":
        bw = image.convert("1")
        plt.imshow(bw)
        plt.axis(axis)
        plt.show()
        return bw
    elif option == "Filters - Sharpen":
        sharp = image.filter(ImageFilter.SHARPEN)
        plt.imshow(sharp)
        plt.axis(axis)
        plt.show()
        return sharp
    elif option == "Filters - Edge Enhance":
        edge = image.filter(ImageFilter.EDGE_ENHANCE)
        plt.imshow(edge)
        plt.axis(axis)
        plt.show()
        return edge
    elif option == "Contrast Image":
        contrast = ImageEnhance.Contrast(image).enhance(enhance)
        plt.axis(axis)
        plt.show()
        return contrast