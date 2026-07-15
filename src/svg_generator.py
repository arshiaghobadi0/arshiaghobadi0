from datetime import datetime
from dateutil import relativedelta
from src.config import *

def calculate_age():
    """محاسبه سن از تاریخ تولد با ساعت، دقیقه و ثانیه"""
    now = datetime.now()
    diff = relativedelta.relativedelta(now, BIRTHDAY)
    
    total_seconds = int((now - BIRTHDAY).total_seconds())
    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours = (total_seconds // 3600) % 24
    
    return f"{diff.years}y {diff.months}m {diff.days}d {hours:02d}:{minutes:02d}:{seconds:02d}"

def generate_svg(stats, theme='dark'):
    """
    تولید فایل SVG با اطلاعات و تم دلخواه
    theme: 'dark' یا 'light'
    """
    
    age = calculate_age()
    
    # ===== تنظیم رنگ‌ها بر اساس تم =====
    if theme == 'light':
        colors = {
            'bg': '#ffffff',
            'text': '#24292f',
            'header': '#0969da',
            'label': '#d45a0c',
            'value': '#24292f',
            'section': '#57606a',
            'accent': '#cf222e',
            'separator': '#d0d7de',
            'border': '#d0d7de',
            'card_bg': '#f6f8fa',
            'grid': '#d0d7de'
        }
        grid_opacity = '0.25'
    else:  # dark (پیش‌فرض)
        colors = {
            'bg': '#0d1117',
            'text': '#c9d1d9',
            'header': '#58a6ff',
            'label': '#f0883e',
            'value': '#c9d1d9',
            'section': '#8b949e',
            'accent': '#f78166',
            'separator': '#30363d',
            'border': '#30363d',
            'card_bg': '#161b22',
            'grid': '#30363d'
        }
        grid_opacity = '0.12'
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="500" viewBox="0 0 1000 500">
    <!-- ===== تعریف الگوی گرید ===== -->
    <defs>
        <!-- گرید ریز (۲۰×۲۰) -->
        <pattern id="grid-small" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{colors['grid']}" stroke-width="0.5" stroke-opacity="{grid_opacity}"/>
        </pattern>
        <!-- گرید درشت (۱۰۰×۱۰۰) با خطوط پررنگ‌تر -->
        <pattern id="grid-large" width="100" height="100" patternUnits="userSpaceOnUse">
            <rect width="100" height="100" fill="url(#grid-small)"/>
            <path d="M 100 0 L 0 0 0 100" fill="none" stroke="{colors['grid']}" stroke-width="1.2" stroke-opacity="{grid_opacity}"/>
        </pattern>
    </defs>
    
    <!-- ===== پس‌زمینه با گرید ===== -->
    <rect width="1000" height="500" fill="{colors['bg']}" rx="14" ry="14"/>
    <rect width="1000" height="500" fill="url(#grid-large)" rx="14" ry="14"/>
    <rect width="1000" height="500" fill="none" stroke="{colors['border']}" stroke-width="1.5" rx="14" ry="14"/>
    
    <style>
        text {{ 
            font-family: 'Cascadia Code', 'Fira Code', 'JetBrains Mono', monospace;
        }}
        .header {{ 
            font-size: 28px; 
            fill: {colors['header']}; 
            font-weight: 700;
            letter-spacing: 0.5px;
        }}
        .header-sub {{ 
            font-size: 15px; 
            fill: {colors['section']}; 
        }}
        .label {{ 
            font-size: 15px; 
            fill: {colors['label']}; 
            font-weight: 500;
        }}
        .value {{ 
            font-size: 15px; 
            fill: {colors['value']}; 
        }}
        .section-title {{ 
            font-size: 18px; 
            fill: {colors['section']}; 
            font-weight: 700;
            letter-spacing: 0.3px;
        }}
        .section-icon {{
            fill: {colors['header']};
        }}
        .separator {{
            stroke: {colors['separator']};
            stroke-width: 1;
            stroke-dasharray: 4,4;
        }}
        .solid-separator {{
            stroke: {colors['separator']};
            stroke-width: 1.5;
        }}
        .footer {{
            font-size: 12px;
            fill: {colors['section']};
        }}
        .accent-text {{
            fill: {colors['accent']};
        }}
    </style>

    <!-- ===== HEADER ===== -->
    <text x="35" y="52" class="header">╭─</text>
    <text x="80" y="52" class="header">{USERNAME}</text>
    <text x="{len(USERNAME)*14 + 120}" y="52" class="header-sub">// Developer</text>
    
    <!-- خط جداکننده -->
    <line x1="35" y1="66" x2="960" y2="66" class="solid-separator"/>
    
    <!-- ===== SYSTEM (ستون چپ) ===== -->
    <text x="35" y="100" class="section-title">
        <tspan class="section-icon">■</tspan> SYSTEM
    </text>
    
    <text x="50" y="130" class="label">OS: </text>
    <text x="160" y="130" class="value"> {OS}</text>
    
    <text x="50" y="155" class="label">Uptime: </text>
    <text x="160" y="155" class="value"> {age}</text>

    <text x="50" y="180" class="label">University: </text> 
    <text x="160" y="180" class="value"> {UNIVERSITY}</text>
    
    <text x="50" y="205" class="label">Host: </text>
    <text x="160" y="205" class="value"> {HOST}</text>
    
    <text x="50" y="230" class="label">Kernel: </text>
    <text x="160" y="230" class="value"> {KERNEL}</text>
    
    <text x="50" y="255" class="label">IDE: </text>
    <text x="160" y="255" class="value"> {IDE}</text>
    
    <!-- ===== LANGUAGES (ستون راست) ===== -->
    <text x="500" y="100" class="section-title">
        <tspan class="section-icon">■</tspan> LANGUAGES
    </text>
    
    <text x="515" y="130" class="label">Programming: </text>
    <text x="635" y="130" class="value"> {PROG_LANGS}</text>
    
    <text x="515" y="155" class="label">Computer: </text>
    <text x="635" y="155" class="value"> {COMPUTER_LANGS}</text>
    
    <text x="515" y="180" class="label">Real: </text>
    <text x="635" y="180" class="value"> {REAL_LANGS}</text>
    
    <!-- خط جداکننده -->
    <line x1="35" y1="270" x2="960" y2="270" class="separator"/>
    
    <!-- ===== HOBBIES ===== -->
    <text x="35" y="300" class="section-title">
        <tspan class="section-icon">■</tspan> HOBBIES
    </text>
    
    <text x="50" y="330" class="label">Software: </text>
    <text x="160" y="330" class="value"> {SOFTWARE_HOBBIES}</text>
    
    <text x="50" y="355" class="label">Hardware: </text>
    <text x="160" y="355" class="value"> {HARDWARE_HOBBIES}</text>

    <text x="50" y="380" class="label">RealLife: </text>
    <text x="160" y="380" class="value"> {REALLIFE_HOBBIES}</text>
    
    <!-- ===== CONTACT ===== -->
    <text x="500" y="300" class="section-title">
        <tspan class="section-icon">■</tspan> CONTACT
    </text>
    
    <text x="515" y="330" class="label">Personal: </text>
    <text x="635" y="330" class="value"> {EMAIL_PERSONAL}</text>
    
    <text x="515" y="355" class="label">Work: </text>
    <text x="635" y="355" class="value"> {EMAIL_WORK}</text>
    
    <text x="515" y="380" class="label">LinkedIn: </text>
    <text x="635" y="380" class="value"> {LINKEDIN}</text>
    
    <text x="515" y="405" class="label">Instagram: </text>
    <text x="635" y="405" class="value"> {INSTAGRAM}</text>
    
    <!-- ===== FOOTER ===== -->
    <line x1="35" y1="450" x2="960" y2="450" class="separator"/>
    
    <text x="35" y="478" class="footer">
        ╰─ Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} 
        <tspan class="accent-text">♥</tspan>
    </text>
    
</svg>'''
    return svg_content
