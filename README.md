# ChromaAura - Your Source of Colorful Inspiration

![ChromaAura Logo](static/img/logo.png)

ChromaAura is a web application that helps you discover the top predominant colors in your images. Whether you're seeking inspiration for your next creative project or just curious about the color palette of your favorite images, ChromaAura has you covered. Upload your image, and ChromaAura will unveil the dominant colors, ready to spark your creativity.

## How It Works

ChromaAura uses a combination of Python, Flask, Bootstrap, and color analysis logic to deliver its vibrant color insights. The following components bring ChromaAura to life:

- **Flask Web Framework:** The project is built using Flask, a popular Python web framework, enabling the creation of a seamless user experience.

- **Bootstrap Styling:** The user interface is designed with Bootstrap, ensuring a sleek and responsive layout.

- **Image Handling Logic:** The application processes uploaded images using the `PIL` (Python Imaging Library) module. Images are analyzed to identify the top 10 predominant colors.

- **Color Analysis:** The color analysis logic leverages Python's `numpy` library for efficient array manipulation, allowing the computation of the dominant colors within an image.

## Usage

1. **Upload Your Image:** Visit the ChromaAura website and upload an image of your choice.
2. **Discover Dominant Colors:** ChromaAura will process your image and reveal its top 10 predominant colors.
3. **Get Inspired:** Use the color palette to fuel your creative projects or simply admire the captivating hues.

## Acknowledgements

- Background image courtesy of [Steve Johnson](https://www.pexels.com/photo/selective-focus-photography-of-paintbrush-near-paint-pallet-1047540/) on Pexels.
- Logo created by [me](https://www.linkedin.com/in/victor-martino-446765140/).

## Installation

1. Clone the repository: `git clone https://github.com/victormartino/Portfolio_Project_11__Image_Color_Identifier_Website`
2. Navigate to the project directory: `cd ChromaAura`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`
