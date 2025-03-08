import os
import requests
from comfyui import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 图床 API 配置（这里以 imgbb 为例）
IMGBB_API_KEY = "你的_imgbb_API_key"  # 需要替换为实际的 API key
IMGBB_API_URL = "https://api.imgbb.com/1/upload"

class UploadImageToImageHost:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"default": None}),  # ComfyUI 的图像输入类型
            }
        }

    RETURN_TYPES = ("STRING",)  # 输出类型为字符串（URL）
    RETURN_NAMES = ("image_url",)  # 输出名称
    FUNCTION = "upload_image"  # 主函数名
    CATEGORY = "Image Utilities"  # 节点类别

    def upload_image(self, image):
        """
        上传图片到图床并返回 URL
        参数:
            image: ComfyUI 的图像输入（tensor 格式）
        返回:
            str: 图床返回的图片 URL
        """
        # 将 ComfyUI 的图像 tensor 转换为本地文件
        import torch
        import numpy as np
        from PIL import Image
        import io

        # 将 tensor 转换为 PIL 图像
        image_np = np.clip(image[0].cpu().numpy() * 255, 0, 255).astype(np.uint8)
        pil_image = Image.fromarray(image_np)

        # 保存为临时文件
        temp_file = "temp_image.png"
        pil_image.save(temp_file, format="PNG")

        # 上传到 imgbb
        try:
            with open(temp_file, "rb") as file:
                payload = {
                    "key": IMGBB_API_KEY,
                    "expiration": 600,  # 设置图片在 10 分钟（600秒）后销毁
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

# 注册节点到 ComfyUI
NODE_CLASS_MAPPINGS["UploadImageToImageHost"] = UploadImageToImageHost
NODE_DISPLAY_NAME_MAPPINGS["UploadImageToImageHost"] = "Upload Image to Image Host"