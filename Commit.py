import os
import subprocess
from datetime import datetime

def git_add_commit_push():
    try:
        # 检查是否有更改
        status_result = subprocess.run(["git", "status", "--porcelain"], check=True, stdout=subprocess.PIPE, text=True)
        
        if not status_result.stdout.strip():
            print("没有更改，未执行提交。")
            return
        
        # 获取当前时间作为提交信息
        commit_message = f"Auto commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # 执行 git add .
        subprocess.run(["git", "add", "."], check=True)
        
        # 执行 git commit -m "commit_message"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 执行 git push
        subprocess.run(["git", "push"], check=True)
        
        print(f"成功执行 git add, commit 和 push 操作。\n提交信息: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"执行过程中出现错误: {e}")

if __name__ == "__main__":
    git_add_commit_push()