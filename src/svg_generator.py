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
            'grid': '#d0d7de',
            'ascii': '#57606a'
        }
        grid_opacity = '0.35'
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
            'grid': '#30363d',
            'ascii': '#58a6ff'
        }
        grid_opacity = '0.30'
    
    # ===== عکس ASCII شما =====
    ascii_art = r'''
++++++xxXX888888888888888888888880000000000000000000S#@@@@@@@###SSSSSS0SSSSSSSSSSSSSS#####
++++xxxxX888888888888888888888880000000000000000000SS#@@@@@@@@@@###SSSSSSSSSSSSSSSS##@@@@@
xxxxxxxxX8888888888888888888888000000000000000000SSSS#@@@@@@@@@@@@@#SSSSSSSSSSSSSSS#@@@@@@
xxxxxxxxX88888888888888888888000000000008x+++++xX80SS#@@@@@@@@@@@@@#SSSSSSSSSSSSSSS#@@@@@@
xxxxxxxxX8888888888888888888000000000X=--:::::::;-=++X880SS#@@@@@@@#SSSSSSSSSSSSSSS#@@@@@@
xxxxxxxxX88888888888888880000008X+==-;;::::::,,:--=+==+xxxxX88S@@@@#SSSSSSSSSSSSSSS#@@@@@@
xxxxxxxxX8888888888888880S##S8=;:;--;;;;;----;;;:,::;;;;;-xxXXx0#@@#SSSSSSSSSSSSSSS#@@@@@@
xxxxxxxXX888888888888880S#SX-:,,,;;;:,;--;----=++;:::,,::----=xX0@@#SSSSSSSSSSSSSSS#@@@@@@
xxxxxxxXX8888888888888800x=:,,.,,:;-;:,,,,::::::-====-;::,::-xx+x8##SSSSSSSSSSSSSSS#@@@@@@
xxxxxxxXX88888888888888X-,....,:::::,:::,,,,,,,:;:,,,;;--;:,,;xxXx8##SSSSSSSSSSSSSS#@@@@@@
xxxxxxxX8888888888888+;,.....,::,,,:;----;;;::::,,:::::::;:;;;;=+x++80SSSSSSSSSSSSS#@@@@@@
xxxxxxxXX8888888888x--,.......,::-+xxXXXXXxxx+++==+++x+==-;;:;-;;-=-=+8SSSSSSSSSSS##@@@@@@
xxxxxxxXX888888888x=;,.......,;=+XXX888800000S00000000008Xx=;;-:::;;-=+XSSSSSS######@@@@@@
xxxxxxxXX88888888X+-,.......,-+xXXXX88800000SSS000000000088X-;::,,,:;=+XSSSSSS######@@@@@@
xxxxxxxX8888888888+:.. ....,-=+xxXXX8880000000SS00000000008X+:,,,,,:;-=x8SSS########@@@@@@
xxxxxxxX8888888888x:.......,-=++xXX8880000000SSSSSSS0000088Xx;,,,,,:;--=+0SSSS######@@@@@@
xxxxxxxX8888888888X:.......,-==+xXX888800SSSSSSSSSSS0000008XXx-,,::;-=++XSSSS#######@@@@@@
xxxxxxxX88888888888=.......,===------=+xX8800000008888X8888XXX+:....,,:=0SSSSS######@@@@@@
xxxxxxxX888888888888=......;=-::::::,,:;-+xXXXXXx+-;;;;;;-==+xx;,,::::-8SSSSSSSSSS##@@@@@@
xxxxxxxX888888888888X,....,-=;;;;;---;::;-+XXXX+=;;::;;----=-xX=,,,,:-xSSSSSSSSSSS##@@@@@@
xxxxxxxX888888888888=:,...,===--;;-;;-x=--+8S08+--=x-::----++xXx:.,::;=0SSSSSSSSSSS#@@@@@@
xxxxxxxX88888888888888X=;,;=+++-;-=++xxxxxx8008XxxXxXxxx=;=+XXXx-,;=x-XSSSSSSSSSSSS#@@@@@@
xxxxxxxX8888888888888008-;;+xxXx++xxXXXXxxX0S08XXX8888XxxxX8888X-=+Xx0SSSSSSSSSSSSS###@###
xxxxxxxX888888800000000x+=-++xXX8XXX88Xx++X0S08XXx8800888000888X=X00SSSSSSSSSSSSSSSS######
xxxxxxxX888888000000000Xx+==+xXX888888Xx+x80SS0XxxX8000000008XXXX808SSSSSSSSSSSSSSSSS#####
xxxxxxxX8888800000000000=====+xXXX8888Xx+x80S08XXXX8000008888Xxx800SSSSSSSSSSSSSSSSSS#####
xxxxxxxX88880000000000008-+==+xxXXX888X+-;-xXx=;-=X800088888XxxX0SSSSSSSSSSSSSSSSSSSS#####
xxxxxxxX88880000000000000S0+==+xXXXXXXXx+-;:;;--=x888888888XXxx0SSSSSS0SSSSSSSSSSSSSSS###S
xxxxxxxX88888000000000000S#S+=+xxxXxx===-===-=======+XX88XXxx+-+0SSSS0000SSSSSSSSSSSSSSSSS
xxxxxxxX88880000000000000S###X=++xx+=====+++xXx+===--+XXXXxxX00SSSSSS00000000000SSSSSSSS##
xxxxxxxX88888000000000000S####x===++=+++xxXXXXXXXXxxXxxxxxxx0SSSSSSS000000000000000SSSS###
xxxxxxxX88888800000000000S####8---===+xx++=+=====+XXxx++=++8SSSS0000000000000000000SSS####
xxxxxxxX88888800000000000S####0=:;--=++xx+=---=+xxxxxx=--;x0SSSSSSS0000000000000000SSS####
xxxxxxxX88888888800000000S####S+-::;=+xxxXXX888XXXXXx=;;;+XS0S000000000000000000000SSS####
xxxxxxxX88888888800000000S####Sx=-:,:-=++xxXX8XXx+++=:,-+x8S000000000000000000000000SSS###
xxxxxxxX88888888888880000S#####x==-;,,:;;;-=+++==--:,:=+xX8S000000000000000000000000SSSSSS
xxxxxxxX88888888888880000S####Sx+++=;::,,,,,:,,,,,::-=xXX88SS00000000000000000000000SSSSSS
xxxxxxxX88888888888888000S####Sx+x++=-;;::::::::::;=+xX88880S00000000000000000000000SSSSSS
xxxxxxxX88888888888888000SSX+X+++xxx+==--;;;;----==+xX8888880SXX00000000000000000000SSSSSS
xxxxxxxX8888888888888888Xx+Xx+++xxxxxx+========++++xX888888880SSX80SS000000000000000SSSSSS
xxxxxxxX88888888888X+==--;;+x+++xxxxxxxx++++xxxxxxXX8888888000S8++xxxXXX800000000000SSSSSS
xxxxxxxX88888888x==----;;:::+xxxxxxxxXXXxxxxxXXXXXX8888880000S8=-=++++++xxx800000000SSSSSS
xxxxxxxX808xx==----;;;;;;::::-xXXXXXxXXXXXXXXXXXXX888XX8000S8=;---=++++++++++xXxX80SSSSSSS
xxxXXX8x===----;;;;;;;:::::::::;+X8XXXXXXXXXXXXXXXXXXX8000X-;;;---==========++++++++x80SSS
XXX+=-------;;;;;;;;:::::::::::,:::-+xXXXXXxxxxxXX88XXx=;:;;;;;-------=========+++++++++xx
--;-;;;;;;;;;;;;;;;:::::::::::::::::::::::;------;:::::::;;;;;;;;;--------==========++++++
;;;;;;;;;;;;;;;::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;---------==============
;;:;;:::::::;::::::::::::::::::::::::::::::::::::::::;::;;;;;;;;;;;;;-------------========
::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;-------=--------
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;-----------
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;--;;;;;;;;;
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;
:::::,,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;:;;;;;;;;;;;;;;
    '''
    
    # ===== تنظیمات عکس ASCII (سمت چپ، فول سایز) =====
    ascii_lines = ascii_art.strip('\n').split('\n')
    
    # ===== تنظیمات جدید برای جلوگیری از خروج عکس =====
    ascii_start_x = 20       # فاصله از لبه چپ (کمتر)
    ascii_start_y = 85       # شروع از بالاتر
    line_height = 8          # فاصله کمتر بین خطوط
    font_size = 7.5          # سایز فونت کوچکتر
    
    ascii_elements = ""
    for i, line in enumerate(ascii_lines):
        if line.strip():
            clean_line = line.rstrip()
            ascii_elements += f'    <text x="{ascii_start_x}" y="{ascii_start_y + i*line_height}" class="ascii-art" font-size="{font_size}">{clean_line}</text>\n'
    
    # ===== محاسبه ارتفاع برای تعیین خط جداکننده =====
    total_ascii_height = len([l for l in ascii_lines if l.strip()]) * line_height
    separator_y = ascii_start_y + total_ascii_height + 15
    
    # ===== تنظیم ارتفاع SVG بر اساس عکس =====
    svg_height = max(750, separator_y + 80)
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{svg_height}" viewBox="0 0 1100 {svg_height}">
    <!-- ===== تعریف الگوی گرید ===== -->
    <defs>
        <pattern id="grid-small" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{colors['grid']}" stroke-width="0.5" stroke-opacity="{grid_opacity}"/>
        </pattern>
        <pattern id="grid-large" width="100" height="100" patternUnits="userSpaceOnUse">
            <rect width="100" height="100" fill="url(#grid-small)"/>
            <path d="M 100 0 L 0 0 0 100" fill="none" stroke="{colors['grid']}" stroke-width="1.2" stroke-opacity="{grid_opacity}"/>
        </pattern>
    </defs>
    
    <!-- ===== پس‌زمینه با گرید ===== -->
    <rect width="1100" height="{svg_height}" fill="{colors['bg']}" rx="14" ry="14"/>
    <rect width="1100" height="{svg_height}" fill="url(#grid-large)" rx="14" ry="14"/>
    <rect width="1100" height="{svg_height}" fill="none" stroke="{colors['border']}" stroke-width="1.5" rx="14" ry="14"/>
    
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
        .ascii-art {{
            fill: {colors['ascii']};
            font-family: 'Cascadia Code', 'Fira Code', monospace;
            white-space: pre;
            opacity: 0.7;
            letter-spacing: 0.2px;
        }}
        .vertical-line {{
            stroke: {colors['separator']};
            stroke-width: 1;
            stroke-dasharray: 4,4;
        }}
    </style>

    <!-- ===== HEADER ===== -->
    <text x="40" y="52" class="header">╭─</text>
    <text x="85" y="52" class="header">{USERNAME}</text>
    <text x="{len(USERNAME)*14 + 125}" y="52" class="header-sub">// Developer</text>
    
    <!-- خط جداکننده بالایی -->
    <line x1="40" y1="66" x2="1060" y2="66" class="solid-separator"/>
    
    <!-- ===== ASCII ART (سمت چپ، فول سایز) ===== -->
{ascii_elements}
    
    <!-- ===== خط جداکننده عمودی ===== -->
    <line x1="420" y1="85" x2="420" y2="{separator_y}" class="vertical-line"/>
    
    <!-- ===== اطلاعات (سمت راست) ===== -->
    <!-- SYSTEM -->
    <text x="450" y="100" class="section-title">
        <tspan class="section-icon">■</tspan> SYSTEM
    </text>
    
    <text x="470" y="130" class="label">OS: </text>
    <text x="580" y="130" class="value"> {OS}</text>
    
    <text x="470" y="155" class="label">Uptime: </text>
    <text x="580" y="155" class="value"> {age}</text>

    <text x="470" y="180" class="label">University: </text> 
    <text x="580" y="180" class="value"> {UNIVERSITY}</text>
    
    <text x="470" y="205" class="label">Host: </text>
    <text x="580" y="205" class="value"> {HOST}</text>
    
    <text x="470" y="230" class="label">Kernel: </text>
    <text x="580" y="230" class="value"> {KERNEL}</text>
    
    <text x="470" y="255" class="label">IDE: </text>
    <text x="580" y="255" class="value"> {IDE}</text>
    
    <!-- خط جداکننده افقی -->
    <line x1="450" y1="280" x2="1060" y2="280" class="separator"/>
    
    <!-- LANGUAGES -->
    <text x="450" y="310" class="section-title">
        <tspan class="section-icon">■</tspan> LANGUAGES
    </text>
    
    <text x="470" y="340" class="label">Programming: </text>
    <text x="580" y="340" class="value"> {PROG_LANGS}</text>
    
    <text x="470" y="365" class="label">Computer: </text>
    <text x="580" y="365" class="value"> {COMPUTER_LANGS}</text>
    
    <text x="470" y="390" class="label">Real: </text>
    <text x="580" y="390" class="value"> {REAL_LANGS}</text>
    
    <!-- خط جداکننده افقی -->
    <line x1="450" y1="410" x2="1060" y2="410" class="separator"/>
    
    <!-- HOBBIES -->
    <text x="450" y="435" class="section-title">
        <tspan class="section-icon">■</tspan> HOBBIES
    </text>
    
    <text x="470" y="460" class="label">Software: </text>
    <text x="580" y="460" class="value"> {SOFTWARE_HOBBIES}</text>
    
    <text x="470" y="485" class="label">Hardware: </text>
    <text x="580" y="485" class="value"> {HARDWARE_HOBBIES}</text>

    <text x="470" y="510" class="label">RealLife: </text>
    <text x="580" y="510" class="value"> {REALLIFE_HOBBIES}</text>

    <!-- خط جداکننده افقی -->
    <line x1="450" y1="530" x2="1060" y2="530" class="separator"/>
    
    <!-- ===== CONTACT ===== -->
    <text x="450" y="555" class="section-title">
        <tspan class="section-icon">■</tspan> CONTACT
    </text>
    
    <text x="470" y="580" class="label">Personal: </text>
    <text x="580" y="580" class="value"> {EMAIL_PERSONAL}</text>
    
    <text x="470" y="605" class="label">Work: </text>
    <text x="580" y="605" class="value"> {EMAIL_WORK}</text>
    
    <text x="470" y="630" class="label">LinkedIn: </text>
    <text x="580" y="630" class="value"> {LINKEDIN}</text>
    
    <text x="470" y="655" class="label">Instagram: </text>
    <text x="580" y="655" class="value"> {INSTAGRAM}</text>
    
    <!-- ===== FOOTER ===== -->
    <line x1="35" y1="{svg_height - 40}" x2="1060" y2="{svg_height - 40}" class="separator"/>
    
    <text x="35" y="{svg_height - 15}" class="footer">
        ╰─ Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} 
        <tspan class="accent-text">♥</tspan>
    </text>
    
</svg>'''
    return svg_content
