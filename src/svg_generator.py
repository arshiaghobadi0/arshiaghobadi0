from datetime import datetime
from dateutil import relativedelta
from src.config import *

def calculate_age():
    """محاسبه سن از تاریخ تولد"""
    diff = relativedelta.relativedelta(datetime.now(), BIRTHDAY)
    return f"{diff.years}y {diff.months}m {diff.days}d"

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
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">
    <!-- پس‌زمینه اصلی -->
    <rect width="680" height="480" fill="{colors['bg']}" rx="14" ry="14"/>
    <rect width="680" height="480" fill="none" stroke="{colors['border']}" stroke-width="1.5" rx="14" ry="14"/>
    
    <style>
        text {{ 
            font-family: 'Cascadia Code', 'Fira Code', 'JetBrains Mono', monospace;
        }}
        .header {{ 
            font-size: 26px; 
            fill: {colors['header']}; 
            font-weight: 700;
            letter-spacing: 0.5px;
        }}
        .header-sub {{ 
            font-size: 14px; 
            fill: {colors['section']}; 
        }}
        .label {{ 
            font-size: 14px; 
            fill: {colors['label']}; 
            font-weight: 500;
        }}
        .value {{ 
            font-size: 14px; 
            fill: {colors['value']}; 
        }}
        .section-title {{ 
            font-size: 16px; 
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
            font-size: 11px;
            fill: {colors['section']};
        }}
        .accent-text {{
            fill: {colors['accent']};
        }}
    </style>
    
    <!-- ===== HEADER ===== -->
    <text x="28" y="45" class="header">╭─</text>
    <text x="70" y="45" class="header">{USERNAME}</text>
    <text x="{len(USERNAME)*12 + 85}" y="45" class="header-sub">// Developer</text>
    
    <!-- خط جداکننده -->
    <line x1="28" y1="55" x2="652" y2="55" class="solid-separator"/>
    
    <!-- ===== SYSTEM (ستون چپ) ===== -->
    <text x="28" y="85" class="section-title">
        <tspan class="section-icon">■</tspan> SYSTEM
    </text>
    
    <text x="42" y="112" class="label">OS</text>
    <text x="170" y="112" class="value">...... {OS}</text>
    
    <text x="42" y="134" class="label">Uptime</text>
    <text x="170" y="134" class="value">...... {age}</text>
    
    <text x="42" y="156" class="label">Host</text>
    <text x="170" y="156" class="value">...... {HOST}</text>
    
    <text x="42" y="178" class="label">Kernel</text>
    <text x="170" y="178" class="value">...... {KERNEL}</text>
    
    <text x="42" y="200" class="label">IDE</text>
    <text x="170" y="200" class="value">...... {IDE}</text>
    
    <!-- ===== LANGUAGES (ستون راست) ===== -->
    <text x="370" y="85" class="section-title">
        <tspan class="section-icon">■</tspan> LANGUAGES
    </text>
    
    <text x="384" y="112" class="label">Programming</text>
    <text x="510" y="112" class="value">...... {PROG_LANGS}</text>
    
    <text x="384" y="134" class="label">Computer</text>
    <text x="510" y="134" class="value">...... {COMPUTER_LANGS}</text>
    
    <text x="384" y="156" class="label">Real</text>
    <text x="510" y="156" class="value">...... {REAL_LANGS}</text>
    
    <!-- خط جداکننده -->
    <line x1="28" y1="222" x2="652" y2="222" class="separator"/>
    
    <!-- ===== HOBBIES ===== -->
    <text x="28" y="255" class="section-title">
        <tspan class="section-icon">■</tspan> HOBBIES
    </text>
    
    <text x="42" y="282" class="label">Software</text>
    <text x="170" y="282" class="value">...... {SOFTWARE_HOBBIES}</text>
    
    <text x="42" y="304" class="label">Hardware</text>
    <text x="170" y="304" class="value">...... {HARDWARE_HOBBIES}</text>
    
    <!-- ===== CONTACT ===== -->
    <text x="370" y="255" class="section-title">
        <tspan class="section-icon">■</tspan> CONTACT
    </text>
    
    <text x="384" y="282" class="label">Personal</text>
    <text x="510" y="282" class="value">...... {EMAIL_PERSONAL}</text>
    
    <text x="384" y="304" class="label">Work</text>
    <text x="510" y="304" class="value">...... {EMAIL_WORK}</text>
    
    <text x="384" y="326" class="label">LinkedIn</text>
    <text x="510" y="326" class="value">...... {LINKEDIN}</text>
    
    <text x="384" y="348" class="label">Discord</text>
    <text x="510" y="348" class="value">...... {DISCORD}</text>
    
    <!-- ===== FOOTER ===== -->
    <line x1="28" y1="440" x2="652" y2="440" class="separator"/>
    
    <text x="28" y="462" class="footer">
        ╰─ updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} 
        <tspan class="accent-text">♥</tspan>
    </text>
    
</svg>'''
    
    return svg_content
