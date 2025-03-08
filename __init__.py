# 文件路径: G:\ComfyUI-aki-v1.4\custom_nodes\ComfyUI-ImageUploader\__init__.py
import os
import requests
import torch
import numpy as np
from PIL import Image

# 定义节点类
class UploadImageToImageHost:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"default": None}),  # ComfyUI 的图像输入类型
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "",  # 默认值为空，用户需要填写
                    "placeholder": "Enter your imgbb API key here"
                }),  # API Key 输入参数
            }
        }

    RETURN_TYPES = ("STRING",)  # 输出类型为字符串（URL）
    RETURN_NAMES = ("image_url",)  # 输出名称
    FUNCTION = "upload_image"  # 主函数名
    CATEGORY = "Image Utilities"  # 节点类别

    def upload_image(self, image, api_key):
        """
        上传图片到图床并返回 URL
        参数:
            image: ComfyUI 的图像输入（tensor 格式）
            api_key: 用户输入的 imgbb API key
        返回:
            str: 图床返回的图片 URL
        """
        # 检查 API Key 是否为空
        if not api_key:
            raise ValueError("请在节点中输入有效的 imgbb API Key")

        # 图床 API 配置
        IMGBB_API_URL = "https://api.imgbb.com/1/upload"

        # 将 ComfyUI 的图像 tensor 转换为本地文件
        image_np = np.clip(image[0].cpu().numpy() * 255, 0, 255).astype(np.uint8)
        pil_image = Image.fromarray(image_np)

        # 保存为临时文件
        temp_file = "temp_image.png"
        pil_image.save(temp_file, format="PNG")

        # 上传到 imgbb
        try:
            with open(temp_file, "rb") as file:
                payload = {
                    "key": api_key,  # 使用用户输入的 API Key
                    "expiration": 2000000,  # 设置图片在 9000 分钟后销毁
                }
                files = {"image": file}
                response = requests.post(IMGBB_API_URL, data=payload, files=files)
                response.raise_for_status()  # 检查请求是否成功
                result = response.json()
                image_url = result["data"]["url"]
        except Exception as e:
            raise Exception(f"上传图片失败: {str(e)}")
        finally:
            # 删除临时文件
            if os.path.exists(temp_file):
                os.remove(temp_file)

        return (image_url,)

# 手动定义节点映射字典
NODE_CLASS_MAPPINGS = {
    "UploadImageToImageHost": UploadImageToImageHost
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UploadImageToImageHost": "Upload Image to Image Host"
}

# 可选：添加模块加载提示
print("ComfyUI-ImageUploader 节点已加载")