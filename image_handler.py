import numpy as np
from collections import Counter


class ImageHandler:
    def __init__(self, image):
        img_array = np.array(image)
        reshaped_array = img_array.reshape(-1, 3)
        all_channels = [(row[0], row[1], row[2]) for row in reshaped_array]
        channels_counter = Counter(all_channels)
        sorted_channels = sorted(channels_counter, key=lambda x: x[1], reverse=True)
        self.top_channels = sorted_channels[:10]

    def get_rgb_colors(self):
        return self.top_channels
