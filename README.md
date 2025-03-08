# ComfyUI-ImageUploader
A custom ComfyUI node to upload images to imgbb and return the URL.

## Features
- Uploads local images to imgbb.
- Returns the image URL as a string.
- Supports expiration time (e.g., 10 minutes).
- Allows users to input their imgbb API Key directly in the node.

## Installation
1. Navigate to your ComfyUI `custom_nodes` folder.
2. Run: `git clone https://github.com/你的用户名/ComfyUI-ImageUploader.git`
3. Install dependencies: `pip install requests`
4. Restart ComfyUI.

## Configuration
- Get your imgbb API Key from [imgbb.com](https://imgbb.com/) by registering an account.
- Input the API Key in the node's `api_key` field.

## Usage
- Add the "Upload Image to Image Host" node to your workflow.
- Connect an image input.
- Enter your imgbb API Key in the `api_key` field.
- Use the output URL in other nodes.

### ComfyUI-ImageUploader  
一个用于上传图片到 imgbb 并返回 URL 的自定义 ComfyUI 节点。  

## 功能  
- 将本地图片上传至 imgbb。  
- 返回图片的 URL（字符串格式）。  
- 支持设置图片的过期时间（如 10 分钟）。  
- 允许用户直接在节点中输入 imgbb API Key。  

## 安装方法  
1. 进入你的 ComfyUI `custom_nodes` 目录。  
2. 运行以下命令克隆仓库：  
   ```bash
   git clone https://github.com/你的用户名/ComfyUI-ImageUploader.git
   ```
3. 安装依赖：  
   ```bash
   pip install requests
   ```
4. 重启 ComfyUI。  

## 配置  
- 在 [imgbb.com](https://imgbb.com/) 注册账户并获取 API Key。  
- 在节点的 `api_key` 字段中输入你的 API Key。  

## 使用方法  
1. 在 ComfyUI 中添加 **"Upload Image to Image Host"** 节点。  
2. 连接一个图片输入。  
3. 在 `api_key` 字段中输入你的 imgbb API Key。  
4. 该节点将返回图片的 URL，可用于其他节点。