import os
import re

# 获取audio目录下所有MP3文件名
audio_dir = os.path.join(os.path.dirname(__file__), 'audio')
mp3_files = sorted([f for f in os.listdir(audio_dir) if f.lower().endswith('.mp3')])

# 生成新的数组内容
new_content = 'const mp3Files = [\n    "' + '",\n    "'.join(mp3_files) + '"\n]'

# 读取并更新index.html
index_path = os.path.join(os.path.dirname(__file__), 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式替换目标内容
updated_content = re.sub(r'const mp3Files = \[\s*?\]', new_content, content, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f'成功更新 {len(mp3_files)} 首歌曲列表')