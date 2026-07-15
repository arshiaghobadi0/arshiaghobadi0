import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.svg_generator import generate_svg
from src.config import USERNAME

def main():
    print(f"🔄 Generating profile for {USERNAME}...")
    
    # اطلاعات گیت‌هاب دیگه دریافت نمیشه
    stats = {
        'user': {'followers': 0},
        'repos': {'total': 0, 'stars': 0, 'commits': 0},
        'lines': {'total': 0, 'added': 0, 'deleted': 0}
    }
    
    # تولید SVG
    print("🎨 Generating SVG...")
    svg_content = generate_svg(stats)
    
    # ذخیره فایل‌ها
    with open('dark_mode.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    # نسخه تم روشن
    light_svg = svg_content.replace('#0d1117', '#ffffff').replace('#58a6ff', '#0366d6').replace('#c9d1d9', '#24292e')
    with open('light_mode.svg', 'w', encoding='utf-8') as f:
        f.write(light_svg)
    
    print("✅ Done! Files saved: dark_mode.svg, light_mode.svg")

if __name__ == '__main__':
    main()
