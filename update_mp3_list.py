import os
import re

def get_mp3_files(audio_dir):
    """获取audio目录下所有MP3文件并按字母顺序排序"""
    mp3_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]
    return sorted(mp3_files)

def update_index_html(index_path, mp3_files):
    """更新index.html中的mp3Files数组"""
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到mp3Files数组的开始和结束位置
    start_pattern = r'const mp3Files = \['
    end_pattern = r'\];'
    
    # 构建新的mp3Files数组内容
    new_mp3_list = ',\n                '.join(f"'{file}'" for file in mp3_files)
    new_content = f"const mp3Files = [\n                {new_mp3_list}\n            ]"
    
    # 使用正则表达式替换原有内容
    updated_content = re.sub(
        f"{start_pattern}.*?{end_pattern}",
        new_content,
        content,
        flags=re.DOTALL
    )
    
    # 写入更新后的内容
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_dir = os.path.join(script_dir, 'audio')
    index_path = os.path.join(script_dir, 'index.html')
    
    if not os.path.exists(audio_dir):
        print(f"错误：找不到audio目录：{audio_dir}")
        return
    
    if not os.path.exists(index_path):
        print(f"错误：找不到index.html文件：{index_path}")
        return
    
    try:
        mp3_files = get_mp3_files(audio_dir)
        update_index_html(index_path, mp3_files)
        print(f"成功更新！共处理了 {len(mp3_files)} 个MP3文件。")
    except Exception as e:
        print(f"更新过程中发生错误：{str(e)}")

if __name__ == '__main__':
    main()