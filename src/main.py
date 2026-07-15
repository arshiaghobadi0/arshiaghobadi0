import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.svg_generator import generate_svg
from src.config import USERNAME

def main():
    print(f"🔄 Generating profile for {USERNAME}...")
    
    stats = {
        'user': {'followers': 0},
        'repos': {'total': 0, 'stars': 0, 'commits': 0},
        'lines': {'total': 0, 'added': 0, 'deleted': 0}
    }
    
    print("🌙 Generating dark mode...")
    dark_svg = generate_svg(stats, theme='dark')
    with open('dark_mode.svg', 'w', encoding='utf-8') as f:
        f.write(dark_svg)
    
    print("☀️ Generating light mode...")
    light_svg = generate_svg(stats, theme='light')
    with open('light_mode.svg', 'w', encoding='utf-8') as f:
        f.write(light_svg)
    
    print("✅ Done! Files saved: dark_mode.svg, light_mode.svg")

if __name__ == '__main__':
    main()
