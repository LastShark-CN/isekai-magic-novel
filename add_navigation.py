#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
章节导航链接添加工具
为小说章节自动添加上一章/下一章/返回目录的导航链接
"""

import os
import re
from pathlib import Path

def get_chapter_files(novel_dir):
    """获取所有章节文件并按顺序排序"""
    chapter_files = []
    for file in os.listdir(novel_dir):
        if file.endswith('.md') and file.startswith('第'):
            chapter_files.append(file)
    
    # 按章节号排序
    def extract_chapter_number(filename):
        match = re.search(r'第(\d+)章', filename)
        return int(match.group(1)) if match else 0
    
    chapter_files.sort(key=extract_chapter_number)
    return chapter_files

def add_navigation_links(novel_dir, chapter_files):
    """为每个章节文件添加导航链接"""
    
    navigation_template = '''
---

<div align="center">

**[{prev_link} {prev_text}](./{prev_file})** | **[{dir_link} 返回目录](../目录.md)** | **[{next_link} 下一章 ➡](./{next_file})**

</div>
'''
    
    for i, filename in enumerate(chapter_files):
        filepath = os.path.join(novel_dir, filename)
        
        # 读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有导航链接
        if '<div align="center">' in content and '返回目录' in content:
            print(f"⊘ 跳过 {filename} - 已存在导航链接")
            continue
        
        # 确定上一章和下一章
        prev_file = chapter_files[i-1] if i > 0 else ""
        next_file = chapter_files[i+1] if i < len(chapter_files) - 1 else ""
        
        prev_text = "上一章" if prev_file else ""
        next_text = "下一章" if next_file else ""
        
        prev_link = "⬅" if prev_file else ""
        next_link = "➡" if next_file else ""
        dir_link = "⬅"
        
        # 生成导航HTML
        nav_parts = []
        if prev_file:
            nav_parts.append(f'**[{prev_link} {prev_text}](./{prev_file})**')
        
        nav_parts.append(f'**[{dir_link} 返回目录](../目录.md)**')
        
        if next_file:
            nav_parts.append(f'**[{next_link} {next_text} ➡](./{next_file})**')
        
        navigation = '\n\n---\n\n<div align="center">\n\n' + ' | '.join(nav_parts) + '\n\n</div>\n'
        
        # 如果文件末尾已有分隔线，先移除
        content = content.rstrip()
        if content.endswith('---'):
            content = content[:-3].rstrip()
        
        # 添加导航链接
        new_content = content + navigation
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ 已更新 {filename}")

def main():
    """主函数"""
    # 获取项目根目录
    project_root = Path(__file__).parent
    novel_dir = project_root / '小说'
    
    if not novel_dir.exists():
        print(f"错误: 找不到小说目录 {novel_dir}")
        return
    
    print("📚 开始处理章节文件...")
    print(f"📁 小说目录: {novel_dir}")
    print()
    
    # 获取所有章节文件
    chapter_files = get_chapter_files(novel_dir)
    
    if not chapter_files:
        print("⚠ 未找到章节文件")
        return
    
    print(f"📖 找到 {len(chapter_files)} 个章节:")
    for i, filename in enumerate(chapter_files, 1):
        print(f"  {i}. {filename}")
    print()
    
    # 添加导航链接
    add_navigation_links(novel_dir, chapter_files)
    
    print()
    print("✨ 完成！所有章节已添加导航链接")

if __name__ == '__main__':
    main()
