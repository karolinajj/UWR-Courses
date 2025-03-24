import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def make_happier(image_path, output_path):
    original_image = Image.open(image_path)
    pixels = np.array(original_image)

    happiness_factor = 1.5

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            if np.all(np.isclose(pixels[i, j], pixels[i, j, 0], atol=5)):
                # Use a complementary color to gray for more vibrancy
                pixels[i, j] = (1 - happiness_factor) * pixels[i, j] + happiness_factor * (255 - pixels[i, j])

    modified_image = Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8))
    modified_image.save(output_path)

def make_sadder(image_path, output_path):
    original_image = Image.open(image_path)
    pixels = np.array(original_image)

    sadness_factor = 1

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            # Convert pixel to grayscale
            gray_value = np.mean(pixels[i, j])
            # Add more gray tones to make the image sadder
            pixels[i, j] = pixels[i, j] + sadness_factor * np.array([gray_value, gray_value, gray_value])

    modified_image = Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8))
    modified_image.save(output_path)

def display_images(original_image, modified_image):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(np.array(original_image))
    axes[0].set_title('Obraz pierwotny')
    axes[0].axis('off')

    axes[1].imshow(np.array(modified_image))
    axes[1].set_title('Obraz zmodyfikowany')
    axes[1].axis('off')

    plt.show()

# Przykładowe użycie
input_image_path = "input_image.jpg"
output_happy_image_path = "output_happy_image.jpg"
output_sad_image_path = "output_sad_image.jpg"

make_happier(input_image_path, output_happy_image_path)
make_sadder(input_image_path, output_sad_image_path)

original_image = Image.open(input_image_path)
happy_image = Image.open(output_happy_image_path)
sad_image = Image.open(output_sad_image_path)

# Wyświetl obrazy na jednym wykresie
display_images(original_image, happy_image)
display_images(original_image, sad_image)
