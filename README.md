# ComfyUI-ImageUploader
A custom ComfyUI node to upload images to imgbb and return the URL.

## Features
- Uploads local images to imgbb.
- Returns the image URL as a string.
- Supports expiration time (e.g., 10 minutes).

## Installation
1. Navigate to your ComfyUI `custom_nodes` folder.
2. Run: `git clone https://github.com/你的用户名/ComfyUI-ImageUploader.git`
3. Install dependencies: `pip install requests`
4. Restart ComfyUI.

## Configuration
- Replace `IMGBB_API_KEY` in `__init__.py` with your imgbb API key.

## Usage
- Add the "Upload Image to Image Host" node to your workflow.
- Connect an image input and use the output URL in other nodes.