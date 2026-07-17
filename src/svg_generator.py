from datetime import datetime, timezone
from dateutil import relativedelta
from src.config import *
import pytz

def calculate_age(timezone_mode='local'):
    """
    محاسبه سن از تاریخ تولد با ساعت، دقیقه و ثانیه
    timezone_mode: 'local' (تهران) یا 'utc' (جهانی)
    """
    # تنظیم تایم‌زون
    if timezone_mode == 'utc':
        tz = pytz.UTC
    else:  # local (تهران)
        tz = pytz.timezone('Asia/Tehran')
    
    now = datetime.now(tz)
    
    # تبدیل BIRTHDAY به تایم‌زون مورد نظر
    birthday = BIRTHDAY
    if birthday.tzinfo is None:
        birthday = tz.localize(birthday)
    
    diff = relativedelta.relativedelta(now, birthday)
    
    total_seconds = int((now - birthday).total_seconds())
    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours = (total_seconds // 3600) % 24
    
    return f"{diff.years}y {diff.months}m {diff.days}d {hours:02d}:{minutes:02d}:{seconds:02d}"

def get_current_time(timezone_mode='local'):
    """
    دریافت زمان فعلی با تایم‌زون مشخص
    timezone_mode: 'local' (تهران) یا 'utc' (جهانی)
    """
    if timezone_mode == 'utc':
        tz = pytz.UTC
        tz_name = 'UTC'
    else:  # local (تهران)
        tz = pytz.timezone('Asia/Tehran')
        tz_name = 'IRST'
    
    now = datetime.now(tz)
    return now, tz_name

def generate_svg(stats, theme='dark'):
    """
    تولید فایل SVG با اطلاعات و تم دلخواه
    theme: 'dark' یا 'light'
    """
    
    # ===== محاسبه سن در دو تایم‌زون =====
    age_local = calculate_age('local')
    age_utc = calculate_age('utc')
    
    # ===== دریافت زمان فعلی در دو تایم‌زون =====
    now_local, tz_local = get_current_time('local')
    now_utc, tz_utc = get_current_time('utc')
    
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
+++++++++++xxXXX88888888888888888888888888888888888888888000000000000000000000000000000SS#@@@@@@@@@#####SSSSSSSSSSSS000SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
x++++++++++xxXXX88888888888888888888888888888888888888800000000000000000000000000000000SS#@@@@@@@@@@@@######SSSSSSSS00SSSSSSSSSSSSSSSSSSSSSSS#########
++++++++++xxxXXX88888888888888888888888888888888888888800000000000000000000000000000000SS#@@@@@@@@@@@@@@@@#####SSSSSSSSSSSSSSSSSSSSSSSSSSSS###@@@@@@@@
xx+++++++xxxxXX88888888888888888888888888888888888888880000000000000000000000000000SSSSSS#@@@@@@@@@@@@@@@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@
xxxxxxxxxxxxxXX888888888888888888888888888888888888880000000000000000000000000000SSSSSSSS#@@@@@@@@@@@@@@@@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSSS#@@@@@@@@@@
xxxxxxxxxxxxxXX888888888888888888888888888888888888000000000000000000000088888880SSSSSSSS#@@@@@@@@@@@@@@@@@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSS#@@@@@@@@@@
xxxxxxxxxxxxxXX8888888888888888888888888888888880000000000000000008x++-=+==+++++xxxx80SS##@@@@@@@@@@@@@@@@@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSS#@@@@@@@@@@
xxxxxxxxxxxxxXX888888888888888888888888888888000000000000000008++---;;;;:::;;;;;;;-+++=+8000S#@@@@@@@@@@@@@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSS#@@@@@@@@@@
xxxxxxxxxxxxxXX888888888888888888888888888880000000008xXX8888x-;---:,::::::,,::;-=---=++++xxxxXX88000#@@@@@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSS#@@@@@@@@@@
xxxxxxxxxxxxxXX8888888888888888888888888800000000008808xx=-=;;;;-:,,::,:::::,,:;;-==++=-=+++XXxxx=+X0SX0#@@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSS#@@@@@@@@@@
xxxxxxxxxxxxxXX888888888888888888888888800SSSSSS0088+-;;;;-;;--;:,:;;:;;;-;::::::,:::;;-=-===-=XX08x=xxXXS@@@@@@##SSSSSSSSSSSSSSSSSSSSSSSSS#@@@@@@@@@@
xxxxxxxxxxxxxX888888888888888888888888800SS###SS0x;::::;----;;;-;;----=-;------;;,,,:,::;;;---::-+++X8Xxx80@@@@@##SSSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888888888880SS###S0=;::,,:,:;--;:,,-;-----==;-=-=++x==;,,::,,.,,,,;-==---;=xX8X0@@@###SSSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888888888880SS#0+-;:,,,,,,::;;;;::.::;;::::-;:---+---=-===-;:;;;;:::--:;+=+==xX8S@@###SSSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888888888880S0+x-::,,...,,,:;;---;,,,,,,,,,:,,:;::::;=++==++=-;;:,:,,:::;+Xxxx+xXS@@##SSSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX888888888888888888888888808=;,,......,,:::;;:;:::::,..,,,,,,,,,,:,;-;:,:::;+-+=-:,..,:::+xXXxXxX0S##SSSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX888888888888888888888888X+:,,.......,;;;;:,,,,,,::;;:,,,,,,,,,,,::::,,,,,,:::;-===+=;,.:;+xxxx8xx0###SSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX8888888888888888888888X-:,,,.......:;::,.,,,,,:;;;=;-;;:;::::::::::,,,,,,,,,,:,:;;;;;;;:;;===+x8xxX8SSSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888888+-;;,..........,,:,,,.,:;-==+++=+===----;;;;;;:::;;:;;;;;;::::,::;;;-;;;--+++-=-=xSSSSSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxxXX888888888888888888x--=:,............,,,::-=+xxxXXXXXXX8XXxx++x++=+======++xx+++==-;;;;:;;---;;;-=-====x8S##SSSSSSSSSSSSSSSS###@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888+;=-::........  ...,:;-+xXxXXX888888000000000000088888888000088Xx+=;-;,;=--::::-=---+==xS##SSSSSSSS##SSS#####@@@@@@@@@@
xxxxxxxxxxxxXX8888888888888888x-x-;,...... .  ..,:--=+xXXXXX8888888000000000S0S000SSS0000000008888x-;:;=;::,,,:;;;--=Xxx0SSSSSSSSSSS#S##S###@@@@@@@@@@
xxxxxxxxxxxxXX8888888888888888===;.......    ..,;-=++xXXXXXX888880000000000SSS0000S000000000000888Xx-:;;::::,,,:;;-==+x8SSSSSSSSSSSS########@@@@@@@@@@
xxxxxxxxxxxxXX888888888888888X;+:,....  ......,;===+xxXXXXXXX8888000000000SSSSSS0S00000000000000888X+-::,,,::.,,,:---=+8SSSSSSSSSSS########@@@@@@@@@@@
xxxxxxxxxxxxXX8888888888888888+-:....   .. ...;-==++xxxXXXXX8888800000000000SSS00000000000000000888Xx-:,,..,,,,,,:;-===XxSSSSSSSSS#########@@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888=,....... ....,:-==+++xxXXXX888800000000000S0SSSSS000000000000888888Xx-,,.,,..,,,:;-=++++xxSSSSSSSS#########@@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888+,............,:-===++xxXXX88888000000000SSSSSSSSSSSSSSS000000008888XXx-,,,,,,,,,,:;;;;==+x0SSSSSSS#########@@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888x,............,:-===++xXXX8888808000SSSSSSSSSSSSSSSSSSSS000000000088XXxx+;,,,::-;;;-=-=+=x00SSSSS###########@@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888x;.............:-====+xxxxxXXX8888880000SSSSSSSSSSSS0000000000000008XXXXx-:,.,:::;-==-;;=xSSSSSSSS#SSSS#####@@@@@@@@@@@
xxxxxxxxxxxxXX888888888888888888=,...........,;=====---;-;;;-===+xXX888000000000080888888XXXX888888XxXXx=:,.......,,::;x8SSSSSSSSSSSS#######@@@@@@@@@@
xxxxxxxxxxxxXX8888888888888888888=,..........,-==-::;;::,,:,:,,::;=+xXX8888888888XXXxx+==-----+++++xxxxx+;,,.,:::...,;=8SSSSSSSSSSSS####SS##@@@@@@@@@@
xxxxxxxxxxxXXX88888888888888888888-,.........:===::;;::::::::::,:::-=++xxxXXXXXxx+=-::,:,::::;;--==--+xXx=:..;::::;-:+XSSSSSSSSSSSSSSS#SSS##@@@@@@@@@@
xxxxxxxxxxxXXX88888888888888888888+,.........-==-;;;-;;;;;;;;;:,,:;;;=++xxXxXXx+=-;;;;:::;;----;;-----xXXx;..,,,,:;;=x0SSSSSSSSSSSSSSSSSS###@@@@@@@@@@
xxxxxxxxxxxxXX88888888888888888888+:........,-==-----;:-==;,;;,;;;;;;;=x80008Xx=--;:::;;:;-==-;-====-=xXXX-,.,,,:,:;=X8SSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxXXX8888888888888888888+:,,,......:=+==-=-;-;,;+;:::;xXx=---=x80SS08+=---;=xX-:,,:=;;=-=++++xXXX=:,.,:,,:;--8SSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxXXX88888888888888888888888x-;:,.,;=++++==-::-=xXXxXXXXx+++++X800008xx++xXXXXXx==X8+-:;++xxxxXXX+:,::;;;;-=+0SSSSSSSSSSSSSSSSSSS##@@@@@@@@@@
xxxxxxxxxxxXXX8888888888888888888888888--;,,-+++xxx+=---==+++++xxXxxxxxX000088XXXxXXXxxxxxx+++=-=++xXXXXXX+-:,:=xX8;-XSSSSSSSSSSSSSSSSSSSS###@@@@@@@@#
xxxxxxxxxxxXXX8888888888888888888888000X;-;:=+++xxxxx++=+++xxXXXXXxxxxX800S088XXXXXX8888Xx++++++xXX8888XXXx;;-=xxX-+SSSSSSSSSSSSSSSSSSSSSSS###@@@@####
xxxxxxxxxxxXXX88888888888888080080000008+=-:=++xxXXXXXXXXXXXXXX8XXxxx+x80SS088XXXXXX888888888888888888888XX;-+XX8S#SSSSSSSSSSSSSSSSSSSSSSSSS##########
xxxxxxxxxxxXXX8888888888888800000000000=++=-=+++xxXXX888XXXX888XXXx+++xX0SS08XXxXxxX8880888008800080888888X-x88S0S#SSSSSSSSSSSSSSSSSSSSSSSSSS#########
xxxxxxxxxxxXXX8888888888880000000000000xx+=-==+++xXX88X888888888Xx+++xX80SS008XxxxxX8800080000000000888XXXx+X800XSSSSSSSSSSSSSSSSSSSSSSSSSSSS#########
xxxxxxxxxxxXXX88888888888800000000000008+x+=-==++xXXX8X888888888XX+=xX80SSSS0088Xx+X880000000000000888XXXXx880SX8SSSSSSSSSSSSSSSSSSSSSSSSSSSSS########
xxxxxxxxxxxXXX88888888808000000000000000+=x=--==+xxxXXX888888888XXxxxX800SSS0088XXXX88000000080088888XXxxxx88SS#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS########
xxxxxxxxxxxxXX888888888800000000000000008:=Xx-==++xxXXXXXX8888888x++=+x888088Xx++xxx80000000000888888XXxx=XS0X+SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS########
xxxxxxxxxxxxXX888888800800000000000000000+:+=-===+xxXXXXXX888888Xx=-;:;=xXXX+=:,;==x8808000088888888XXxx+X000SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS#######
xxxxxxxxxxxxXX8888880000000000000000000000S0x+--=+xxxXXXXX888X88Xx=-;:;::---;;-;;-+X888888888888888XXxxx+88#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS#######
xxxxxxxxxxxxXX8888888800000000000000000000S##x====++xxXXXXXXXXXXXXx++-;;;;;;---=xXX888888888888888Xxxx+X0S#SSSSSSSSS0SSSSSSSSSSSSSSSSSSSSSSSSS######SS
xxxxxxxxxxxxXX888888888000000000000000000SS###x===+++xxxXXxXXxx+===;--;-----------===+xX8XX88888XXXxxx+=x8XSSSSSSSSS00SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
xxxxxxxxxxxxXX888888888800000000000000000SS###@#x===+xxxXxxx+=====+++xxxxxxxXXXxxx++--;;=xXX888XXXxxxX=;=-8SSSSSSSSS00000000SSSSSSSSSSSSSSSSSSSSSSSSSS
xxxxxxxxxxxxXX888800000000000000000000000SS#####S+==+++xxxx==-=======+++++xXx+++==-=-;;-=+xXXXXXXXxxXXS0SSSSSSSSSS0000000000000S00S0SSSSSSSSSSSSSSSS#S
xxxxxxxxxxxxXX888800008080000000000000000SS######8===++++++==++=========-----==xxXxx++xx++xXXxxxxxxxXSSSSSSSSSSSSS000000000000000000000SSSSSSSSSSS#S#S
xxxxxxxxxxxxXX888088888880000000000000000SS#######X======++==++xxxxxxxX88888888XXXXxxXXXX+xxxx+xxx+x0SSSSSSSSSSSSS000000000000000000000000SSSSSSS#####
xxxxxxxxxxxxXX8888008888000000000000000000S########=-----===+++xxx+++++xxXxxxxx++++xXXXXxxx++++++++SSSSSSSSS0SSS000000000000000000000000000SSSSS######
xxxxxxxxxxxxXX8888880800000000000000000000S########x;:;---====++++++==-;;;;:;---=+xxxxxxx+=======-8SSSSSSSSSSSSS000000000000000000000000000SSSSS######
xxxxxxxxxxxXXX8888888800000000000000000000SS#######X-;::----==+++xx+++==-----==+xxxxxxxxxx==---;-x00SSSSSSSSSSS0000000000000000000000000000SSSSS######
xxxxxxxxxxxxXX8888888000000000000000000000SS#######X=-:,::;-=+xxxxxxxxXXxxXxXXXxXXXXXXXX+=-=;-;-+XS000000S0SSS00000000000000000000000000000SSSSSS#####
xxxxxxxxxxxxXX8888888888888800000000000000SS#######8=--;,,:-==+xxxxXXX88888888XXXXXXXXx+=-::::-+xXS0000000000000000000000000000000000000000SSSSS######
xxxxxxxxxxxXXX8888888888880000000000000000SS#######0+=--;:,:;-==++x+xxxX8888888Xxx++++==-:,,;=+xxX#00000000000000000000000000000000000000000SSSSSS####
xxxxxxxxxxxxXX8888888888888888800000000000SS#######S+==--;:,,:;---=-=+xxXXXXXXxxx++==--;:.:-=+xxXX#0000000000000000000000000000000000000000SSSSSSS####
xxxxxxxxxxxxXX8888888888888888888000000000SS#######Sx====--;:,,:;;;;;--==+x++=====---:,,,;-++xXXXX#00000000000000000000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX8888888888888888888888000000S########S+++++=--;::,.,,:::;;;;;---;;;;;:,,:;;=+xxXXXX8S00000000000000000000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX8888888888888888888888000000SS#######S++++++==-;::::,,.....,,,,,....,::;;-=+xXXX88880#0000000000000000000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX8888888888888888888888800000SS#######8+++++++==-;;;::::::::::::::::::;;-==+xXX8888888#0000000000000000000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX8888888888888888888888800000SS######Sx+++xxx+++==-;;;;:;;:;;;;;;;;;;;--=++xXX888888880#SS0000000000000000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX8888888888888888888888800000SS#S=:x8++++xxxxx+++===---;;;;;;;-;;----===+xxXXX8888888888S#X;=SS00000000000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX8888888888888888888888800000S0X+0Xx+++++xxxxxxx+++======------=======++xxxX88888888888880S#SX0S#S00000000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX888888888888888888888000XX++=--xXx+++++xxxxxxxxxxx++====+=====++++++xxxxX8888888888888880SS#Sx+X800S#0000000000000000000000000SSSSSSSSSS
xxxxxxxxxxxxXX88888888888888888888x==+-=--;;;+Xxx++++xxxxxxxxxxxxx++++++xxxxxxxxxx+xxXX88888888888888000SS8==+xxxxX8XX8000000000000000000000SSSSSSSSSS
xxxxxxxxxxxXX888888888888888008+=--==---;;;::;xxx+xxxxxxxxxxxxXxxxxxxx++xxxxxxxxXXXXX888888888880000000SS8===+++x+xxxxxxxx8SS000000000000000SSSSSSSSSS
xxxxxxxxxxxXX88888888888088x===--------;;::::::+xxxxxxxxxxxxxxXXXXXxxxxxxxxXxxXXXXXX888888888880000000SSX---===+++++++++xxxxxX080S0000000000SSSSSSSSSS
xxxxxxxxxxxXX88800808x+X+===------;;;;;;;;::::::=XXxxXXXXxxxxxXXXXXXXXXXXxXXXXXXXXX8888888X888000000SS0=---=====+++++++++++++++x8XXXX0S00000SSSSSSSSSS
xxxxxxxxxxxXX8800++xx=---------;;;;;;;;;;;::::::::+xXXXXXXXXxxxXXXXXXXXXXXXXXXXXXX88XX8XXXX8800000SS0-;;;----===++=++++++++++++++xxxxxxxX8#SSSSSSSSSSS
xxxxxxxxxxX00x+=++=----------;;;;;;;;;:;;;::,::::,,:-xXX88XXXXxXXXXXXXXXXXXXXXXXXXXXXXXXXX88800S00X-;;;;;---=-================+++++++++++x+xX8###SSSSS
xxxXXX800x====----------;;;;;;;;;;;:::::::::::::::,,,::-X88XXXXXXXXXXXXXXxxxxxxXXXXXXX8XXX88000x;;;;;;;;;;-----==================++++++++++++++xxx8###
XXXX8x=--------------;;;;;;;;;;;;:::::::::::::::::::,,:::::;xXXXXXX8XXXXxxxxxxxxXXX888XXX88+;;;::;;;;;;;-;------------===============+++++++++++++++xx
X+=-----;;;;-;;;;;;;;;;;;;;;;;;;;::::::::::::::::::::::::::::::::;-+X8XXXXXXXXXXXX88x=;:::::::::;;;;;;;;;;;;;-----------================++++++++++++++
-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;---------------================+==++=++++
;;;;;;;;;;;;;;;;;;;:;;;;;;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;--------------===-======================
;;;;;;;;;;::::::::;:;;;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;:;;;;;;;;;;;;;;;;;;;;;---------------=-----================
;;;;:;;;;:::::::::::;:::::::::::::::::::::::::::::::::::::::::::::::::::;:::::;::::::::;;;::::;;;;;;;;;;;;;;;;;;;;;;;------------------=-=============
::;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-----------------==--==========
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-----;;;----==-------------
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;------------------
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-----------------;-
::::::::::,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;:::;:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-;-;;;;;;;;;--;;;;
::::::::::,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;--;;;;;;;;;;;;;;;;;
::::::::::,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;:;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;
::::::::::,,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;::::;:;::;;;::;;;;;;;;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;;
::::::::,,,,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;:::::;::::;;::;;;;;;;:;;;;;;;;;;;:;;:;;;;:;;;;
::::::::,:,,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;:;;;;::;;;;;;;;;;;;;::;;;::::::
:::::::::,,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;::::::::;:;:::;;;;;;;;;;;;:::;;:::::::
,::::::,,,,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;:;;;;;;;;:::;;::::::::
    '''
    
    # ===== تنظیمات عکس ASCII (سمت چپ، فول سایز) =====
    ascii_lines = ascii_art.strip('\n').split('\n')
    
    # ===== تنظیمات جدید بر اساس خروجی مورد نظر =====
    ascii_start_x = 20       # فاصله از لبه چپ
    ascii_start_y = 85       # شروع از بالا
    line_height = 8          # فاصله بین خطوط
    font_size = 5.5          # سایز فونت
    
    ascii_elements = ""
    for i, line in enumerate(ascii_lines):
        if line.strip():
            clean_line = line.rstrip()
            ascii_elements += f'    <text x="{ascii_start_x}" y="{ascii_start_y + i*line_height}" class="ascii-art" font-size="{font_size}">{clean_line}</text>\n'
    
    # ===== محاسبه ارتفاع برای تعیین خط جداکننده =====
    total_ascii_height = len([l for l in ascii_lines if l.strip()]) * line_height
    separator_y = ascii_start_y + total_ascii_height + 15
    
    # ===== تنظیم عرض و ارتفاع SVG بر اساس خروجی مورد نظر =====
    svg_width = 1000
    svg_height = max(875, separator_y + 60)
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">
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
    <rect width="1000" height="{svg_height}" fill="{colors['bg']}" rx="20" ry="20"/>
    <rect width="1000" height="{svg_height}" fill="url(#grid-large)" rx="20" ry="20"/>
    <rect width="1000" height="{svg_height}" fill="none" stroke="{colors['border']}" stroke-width="1.5" rx="20" ry="20"/>
    
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
        .timezone-tag {{
            font-size: 11px;
            fill: {colors['section']};
            opacity: 0.6;
        }}
    </style>

    <!-- ===== HEADER ===== -->
    <text x="30" y="52" class="header">╭─</text>
    <text x="75" y="52" class="header">{USERNAME}</text>
    <text x="{75 + len(USERNAME)*14 + 44}" y="52" class="header-sub">// Developer</text>
    
    <!-- خط جداکننده بالایی -->
    <line x1="38" y1="66" x2="960" y2="66" class="solid-separator"/>
    
    <!-- ===== ASCII ART (سمت چپ، فول سایز) ===== -->
{ascii_elements}
    
    <!-- ===== خط جداکننده عمودی ===== -->
    <line x1="540" y1="80" x2="540" y2="830" class="vertical-line"/>
    
    <!-- ===== اطلاعات (سمت راست) ===== -->
    <!-- SYSTEM -->
    <text x="550" y="100" class="section-title">
        <tspan class="section-icon">■</tspan> SYSTEM
    </text>
    
    <text x="570" y="130" class="label">OS: </text>
    <text x="680" y="130" class="value"> {OS}</text>
    
    <text x="570" y="155" class="label">Uptime (IRST): </text>
    <text x="680" y="155" class="value"> {age_local}</text>

    <text x="570" y="180" class="label">Uptime (UTC): </text>
    <text x="680" y="180" class="value"> {age_utc}</text>

    <text x="570" y="205" class="label">University: </text> 
    <text x="680" y="205" class="value"> {UNIVERSITY}</text>
    
    <text x="570" y="230" class="label">Host: </text>
    <text x="680" y="230" class="value"> {HOST}</text>
    
    <text x="570" y="255" class="label">Kernel: </text>
    <text x="680" y="255" class="value"> {KERNEL}</text>
    
    <text x="570" y="280" class="label">IDE: </text>
    <text x="680" y="280" class="value"> {IDE}</text>
    
    <!-- خط جداکننده افقی -->
    <line x1="550" y1="305" x2="960" y2="305" class="separator"/>
    
    <!-- LANGUAGES -->
    <text x="550" y="330" class="section-title">
        <tspan class="section-icon">■</tspan> LANGUAGES
    </text>
    
    <text x="570" y="360" class="label">Programming: </text>
    <text x="680" y="360" class="value"> {PROG_LANGS}</text>
    
    <text x="570" y="385" class="label">Computer: </text>
    <text x="680" y="385" class="value"> {COMPUTER_LANGS}</text>
    
    <text x="570" y="410" class="label">Real: </text>
    <text x="680" y="410" class="value"> {REAL_LANGS}</text>
    
    <!-- خط جداکننده افقی -->
    <line x1="550" y1="435" x2="960" y2="435" class="separator"/>
    
    <!-- HOBBIES -->
    <text x="550" y="460" class="section-title">
        <tspan class="section-icon">■</tspan> HOBBIES
    </text>
    
    <text x="570" y="485" class="label">Software: </text>
    <text x="680" y="485" class="value"> {SOFTWARE_HOBBIES}</text>
    
    <text x="570" y="510" class="label">Hardware: </text>
    <text x="680" y="510" class="value"> {HARDWARE_HOBBIES}</text>

    <text x="570" y="535" class="label">RealLife: </text>
    <text x="680" y="535" class="value"> {REALLIFE_HOBBIES}</text>

    <!-- خط جداکننده افقی -->
    <line x1="550" y1="560" x2="960" y2="560" class="separator"/>
    
    <!-- ===== CONTACT ===== -->
    <text x="550" y="585" class="section-title">
        <tspan class="section-icon">■</tspan> CONTACT
    </text>
    
    <text x="570" y="610" class="label">Personal: </text>
    <text x="680" y="610" class="value"> {EMAIL_PERSONAL}</text>
    
    <text x="570" y="635" class="label">Work: </text>
    <text x="680" y="635" class="value"> {EMAIL_WORK}</text>
    
    <text x="570" y="660" class="label">LinkedIn: </text>
    <text x="680" y="660" class="value"> {LINKEDIN}</text>
    
    <text x="570" y="685" class="label">Instagram: </text>
    <text x="680" y="685" class="value"> {INSTAGRAM}</text>
    
    <!-- ===== FOOTER با دو تایم‌زون ===== -->
    <line x1="30" y1="830" x2="960" y2="830" class="separator"/>
    
    <text x="30" y="850" class="footer">
        ╰─ Last Updated: {now_local.strftime('%Y-%m-%d %H:%M')} IRST (Local)
        <tspan class="accent-text"> | </tspan>
        {now_utc.strftime('%Y-%m-%d %H:%M')} UTC (Global)
        <tspan class="accent-text"> | By Arshia Ghobadi ♥</tspan>
    </text>
    
</svg>'''
    return svg_content
