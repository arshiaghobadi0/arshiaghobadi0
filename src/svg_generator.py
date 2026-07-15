from datetime import datetime
from dateutil import relativedelta
from src.config import *

def calculate_age():
    """محاسبه سن از تاریخ تولد"""
    diff = relativedelta.relativedelta(datetime.now(), BIRTHDAY)
    return f"{diff.years} years, {diff.months} months, {diff.days} days"

def generate_svg(stats):
    """تولید فایل SVG با اطلاعات"""
    
    age = calculate_age()
    uptime = age
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="420">
    <rect width="600" height="420" fill="#0d1117" rx="10"/>
    
    <style>
        text {{ font-family: 'Cascadia Code', 'Fira Code', monospace; }}
        .header {{ font-size: 24px; fill: #58a6ff; font-weight: bold; }}
        .label {{ font-size: 14px; fill: #8b949e; }}
        .value {{ font-size: 14px; fill: #c9d1d9; }}
        .section-title {{ font-size: 16px; fill: #f0883e; font-weight: bold; }}
    </style>
    
    <!-- Header -->
    <text x="20" y="40" class="header">{USERNAME}</text>
    
    <!-- OS & System Info -->
    <text x="20" y="70" class="label">OS:</text>
    <text x="140" y="70" class="value">...... {OS}</text>
    
    <text x="20" y="90" class="label">Uptime:</text>
    <text x="140" y="90" class="value">...... {uptime}</text>
    
    <text x="20" y="110" class="label">Host:</text>
    <text x="140" y="110" class="value">...... {HOST}</text>
    
    <text x="20" y="130" class="label">Kernel:</text>
    <text x="140" y="130" class="value">...... {KERNEL}</text>
    
    <text x="20" y="150" class="label">IDE:</text>
    <text x="140" y="150" class="value">...... {IDE}</text>
    
    <!-- Languages -->
    <text x="20" y="190" class="section-title">Languages.Programming:</text>
    <text x="230" y="190" class="value">...... {PROG_LANGS}</text>
    
    <text x="20" y="210" class="section-title">Languages.Computer:</text>
    <text x="230" y="210" class="value">...... {COMPUTER_LANGS}</text>
    
    <text x="20" y="230" class="section-title">Languages.Real:</text>
    <text x="230" y="230" class="value">...... {REAL_LANGS}</text>
    
    <!-- Hobbies -->
    <text x="20" y="270" class="section-title">Hobbies.Software:</text>
    <text x="230" y="270" class="value">...... {SOFTWARE_HOBBIES}</text>
    
    <text x="20" y="290" class="section-title">Hobbies.Hardware:</text>
    <text x="230" y="290" class="value">...... {HARDWARE_HOBBIES}</text>
    
    <!-- Contact -->
    <text x="20" y="330" class="section-title">Contact</text>
    
    <text x="20" y="350" class="label">Email.Personal:</text>
    <text x="180" y="350" class="value">...... {EMAIL_PERSONAL}</text>
    
    <text x="20" y="370" class="label">Email.Work:</text>
    <text x="180" y="370" class="value">...... {EMAIL_WORK}</text>
    
    <text x="20" y="390" class="label">LinkedIn:</text>
    <text x="180" y="390" class="value">...... {LINKEDIN}</text>
    
    <text x="20" y="410" class="label">Discord:</text>
    <text x="180" y="410" class="value">...... {DISCORD}</text>
    
</svg>'''
    
    return svg_content
