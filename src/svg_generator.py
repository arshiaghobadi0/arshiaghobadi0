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

def generate_dots(text, start_x, target_x, char_width=8):
    """
    محاسبه تعداد نقطه‌ها به صورت پویا
    
    Args:
        text: متن عنوان (مثلاً "OS: ")
        start_x: موقعیت شروع عنوان
        target_x: موقعیت هدف برای مقدار
        char_width: عرض تقریبی هر کاراکتر (پیکسل)
    
    Returns:
        رشته‌ای از نقطه‌ها با طول مناسب
    """
    text_width = len(text) * char_width
    available_space = target_x - start_x - text_width
    dots_needed = max(1, available_space // char_width)  # حداقل ۱ نقطه
    return '.' * dots_needed

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
            'card_bg': '#f6f8fa'
        }
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
            'card_bg': '#161b22'
        }
    
    # ===== تعریف موقعیت‌ها =====
    label_start_x = 50      # شروع عنوان‌ها (ستون چپ)
    value_start_x = 190     # شروع مقادیر (ستون چپ)
    
    label_start_x_right = 565   # شروع عنوان‌ها (ستون راست)
    value_start_x_right = 635   # شروع مقادیر (ستون راست)
    
    # ===== محاسبه نقطه‌های پویا =====
    dots_os = generate_dots("OS: ", label_start_x, value_start_x)
    dots_uptime = generate_dots("Uptime: ", label_start_x, value_start_x)
    dots_university = generate_dots("University: ", label_start_x, value_start_x)
    dots_host = generate_dots("Host: ", label_start_x, value_start_x)
    dots_kernel = generate_dots("Kernel: ", label_start_x, value_start_x)
    dots_ide = generate_dots("IDE: ", label_start_x, value_start_x)
    
    dots_prog = generate_dots("Programming: ", label_start_x_right, value_start_x_right)
    dots_comp = generate_dots("Computer: ", label_start_x_right, value_start_x_right)
    dots_real = generate_dots("Real: ", label_start_x_right, value_start_x_right)
    
    dots_sw = generate_dots("Software: ", label_start_x, value_start_x)
    dots_hw = generate_dots("Hardware: ", label_start_x, value_start_x)
    
    dots_personal = generate_dots("Personal: ", label_start_x_right, value_start_x_right)
    dots_work = generate_dots("Work: ", label_start_x_right, value_start_x_right)
    dots_linkedin = generate_dots("LinkedIn: ", label_start_x_right, value_start_x_right)
    dots_instagram = generate_dots("Instagram: ", label_start_x_right, value_start_x_right)
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="500" viewBox="0 0 1000 500">
    <!-- پس‌زمینه اصلی -->
    <rect width="1000" height="500" fill="{colors['bg']}" rx="14" ry="14"/>
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
    
    <text x="{label_start_x}" y="130" class="label">OS: </text>
    <text x="{value_start_x}" y="130" class="value">{dots_os} {OS}</text>
    
    <text x="{label_start_x}" y="155" class="label">Uptime: </text>
    <text x="{value_start_x}" y="155" class="value">{dots_uptime} {age}</text>

    <text x="{label_start_x}" y="180" class="label">University: </text> 
    <text x="{value_start_x}" y="180" class="value">{dots_university} {UNIVERSITY}</text>
    
    <text x="{label_start_x}" y="205" class="label">Host: </text>
    <text x="{value_start_x}" y="205" class="value">{dots_host} {HOST}</text>
    
    <text x="{label_start_x}" y="230" class="label">Kernel: </text>
    <text x="{value_start_x}" y="230" class="value">{dots_kernel} {KERNEL}</text>
    
    <text x="{label_start_x}" y="255" class="label">IDE: </text>
    <text x="{value_start_x}" y="255" class="value">{dots_ide} {IDE}</text>
    
    <!-- ===== LANGUAGES (ستون راست) ===== -->
    <text x="550" y="100" class="section-title">
        <tspan class="section-icon">■</tspan> LANGUAGES
    </text>
    
    <text x="{label_start_x_right}" y="130" class="label">Programming: </text>
    <text x="{value_start_x_right}" y="130" class="value">{dots_prog} {PROG_LANGS}</text>
    
    <text x="{label_start_x_right}" y="155" class="label">Computer: </text>
    <text x="{value_start_x_right}" y="155" class="value">{dots_comp} {COMPUTER_LANGS}</text>
    
    <text x="{label_start_x_right}" y="180" class="label">Real: </text>
    <text x="{value_start_x_right}" y="180" class="value">{dots_real} {REAL_LANGS}</text>
    
    <!-- خط جداکننده -->
    <line x1="35" y1="280" x2="960" y2="280" class="separator"/>
    
    <!-- ===== HOBBIES ===== -->
    <text x="35" y="315" class="section-title">
        <tspan class="section-icon">■</tspan> HOBBIES
    </text>
    
    <text x="{label_start_x}" y="345" class="label">Software: </text>
    <text x="{value_start_x}" y="345" class="value">{dots_sw} {SOFTWARE_HOBBIES}</text>
    
    <text x="{label_start_x}" y="370" class="label">Hardware: </text>
    <text x="{value_start_x}" y="370" class="value">{dots_hw} {HARDWARE_HOBBIES}</text>
    
    <!-- ===== CONTACT ===== -->
    <text x="550" y="315" class="section-title">
        <tspan class="section-icon">■</tspan> CONTACT
    </text>
    
    <text x="{label_start_x_right}" y="345" class="label">Personal: </text>
    <text x="{value_start_x_right}" y="345" class="value">{dots_personal} {EMAIL_PERSONAL}</text>
    
    <text x="{label_start_x_right}" y="370" class="label">Work: </text>
    <text x="{value_start_x_right}" y="370" class="value">{dots_work} {EMAIL_WORK}</text>
    
    <text x="{label_start_x_right}" y="395" class="label">LinkedIn: </text>
    <text x="{value_start_x_right}" y="395" class="value">{dots_linkedin} {LINKEDIN}</text>
    
    <text x="{label_start_x_right}" y="420" class="label">Instagram: </text>
    <text x="{value_start_x_right}" y="420" class="value">{dots_instagram} {INSTAGRAM}</text>
    
    <!-- ===== FOOTER ===== -->
    <line x1="35" y1="455" x2="960" y2="455" class="separator"/>
    
    <text x="35" y="478" class="footer">
        ╰─ Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} 
        <tspan class="accent-text">♥</tspan>
    </text>
    
</svg>'''
    
    return svg_content
