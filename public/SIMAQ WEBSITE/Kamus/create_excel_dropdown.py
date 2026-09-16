import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
import json

# Load original Excel
wb_orig = openpyxl.load_workbook('d:/Dhamir/DHAMIR copy.xlsx', data_only=True)
sheet_orig = wb_orig['Sheet1']
rows = list(sheet_orig.iter_rows(values_only=True))
header = [str(c).strip() if c is not None else '' for c in rows[0]]

data = []
counts = {}
for r in rows[1:]:
    if not any(r):
        continue
    item = dict(zip(header, r))
    nk = item.get('No kata')
    if nk:
        counts[nk] = counts.get(nk, 0) + 1
        if counts[nk] <= 3:
            data.append(item)

# Lengkapi 11a, 11b, 6c agar masing-masing 3 ayat
data.append({'Bentuk Kata': '1. Dhamir', 'No kata': '11a', 'Kata': 'أَنَا', 'Arti kata': 'SAYA / AKU', 'Frek kata': 68, 'SURAT': 20, 'AYAT': 14})
data.append({'Bentuk Kata': '1. Dhamir', 'No kata': '11b', 'Kata': '..يْ', 'Arti kata': '..Ku (Aku/Saya Lk/Pr)', 'Frek kata': None, 'SURAT': 2, 'AYAT': 186})
data.append({'Bentuk Kata': '1. Dhamir', 'No kata': '6c', 'Kata': 'إِيَّاكَ', 'Arti kata': 'KEPADAMU / ENGKAU', 'Frek kata': None, 'SURAT': 28, 'AYAT': 63})

# Create new workbook
wb = openpyxl.Workbook()

# Setup sheets
ws_dashboard = wb.active
ws_dashboard.title = "Dashboard Interaktif"
ws_master = wb.create_sheet(title="Data Master")
ws_dict = wb.create_sheet(title="Daftar Dhamir & Surah")

# Color Styles
header_fill = PatternFill(start_color="064E3B", end_color="064E3B", fill_type="solid") # Dark emerald
header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")

gold_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Soft gold
gold_border_color = "D97706"

card_fill = PatternFill(start_color="F0FDF4", end_color="F0FDF4", fill_type="solid")
accent_fill = PatternFill(start_color="059669", end_color="059669", fill_type="solid")
accent_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")

title_font = Font(name="Arial", size=16, bold=True, color="064E3B")
subtitle_font = Font(name="Arial", size=10, italic=True, color="4B5563")

arabic_font_large = Font(name="Traditional Arabic", size=24, bold=True, color="B45309")
arabic_font_med = Font(name="Traditional Arabic", size=14, bold=True, color="064E3B")
bold_font = Font(name="Arial", size=11, bold=True, color="111827")
normal_font = Font(name="Arial", size=10, color="1F2937")

thin_border = Border(
    left=Side(style='thin', color='D1D5DB'),
    right=Side(style='thin', color='D1D5DB'),
    top=Side(style='thin', color='D1D5DB'),
    bottom=Side(style='thin', color='D1D5DB')
)

# ----------------------------------------------------
# 1. Populate "Data Master"
# ----------------------------------------------------
ws_master.append(['No', 'Bentuk Kata', 'No kata', 'Kata', 'Arti kata', 'Frek kata', 'SURAT', 'AYAT'])
for col in range(1, 9):
    cell = ws_master.cell(row=1, column=col)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

for idx, d in enumerate(data, start=1):
    ws_master.append([
        idx,
        d.get('Bentuk Kata'),
        d.get('No kata'),
        d.get('Kata'),
        d.get('Arti kata'),
        d.get('Frek kata'),
        d.get('SURAT'),
        d.get('AYAT')
    ])

# ----------------------------------------------------
# 2. Populate "Daftar Dhamir & Surah" (For Validation & Lookup)
# ----------------------------------------------------
unique_dhamirs = {}
for d in data:
    nk = d.get('No kata')
    if nk and nk not in unique_dhamirs:
        unique_dhamirs[nk] = {
            'Bentuk': d.get('Bentuk Kata'),
            'Kata': d.get('Kata'),
            'Arti': d.get('Arti kata'),
            'Frek': d.get('Frek kata')
        }

ws_dict.append(['Bentuk Kata List', '', 'No Kata', 'Kata Arab', 'Arti Kata', 'Frekuensi'])
ws_dict.cell(row=1, column=1).fill = header_fill
ws_dict.cell(row=1, column=1).font = header_font
for col in range(3, 7):
    ws_dict.cell(row=1, column=col).fill = header_fill
    ws_dict.cell(row=1, column=col).font = header_font

ws_dict.cell(row=2, column=1, value='1. Dhamir')

ordered_no_kata = ['1a', '1b', '3a', '3b', '4a', '4b', '6a', '6b', '6c', '8a', '8b', '11a', '11b', '12a', '12b']
for r_idx, nk in enumerate(ordered_no_kata, start=2):
    info = unique_dhamirs.get(nk, {})
    ws_dict.cell(row=r_idx, column=3, value=nk)
    ws_dict.cell(row=r_idx, column=4, value=info.get('Kata', ''))
    ws_dict.cell(row=r_idx, column=5, value=info.get('Arti', ''))
    ws_dict.cell(row=r_idx, column=6, value=info.get('Frek', 'Muttashil'))

# ----------------------------------------------------
# 3. Build "Dashboard Interaktif"
# ----------------------------------------------------
# Title
ws_dashboard.merge_cells('B2:H2')
ws_dashboard['B2'] = "DASHBOARD EKSPLORASI DHAMIR AL-QUR'AN"
ws_dashboard['B2'].font = title_font
ws_dashboard['B2'].alignment = Alignment(horizontal="center", vertical="center")

ws_dashboard.merge_cells('B3:H3')
ws_dashboard['B3'] = "Pilih 'Bentuk Kata' dan 'Nomor Kata' di bawah ini untuk melihat detail kata, arti, frekuensi, serta rujukan surat & ayatnya secara otomatis."
ws_dashboard['B3'].font = subtitle_font
ws_dashboard['B3'].alignment = Alignment(horizontal="center", vertical="center")

# Dropdown Inputs Box
ws_dashboard['B5'] = "1. PILIH BENTUK KATA:"
ws_dashboard['B5'].font = Font(name="Arial", size=10, bold=True, color="064E3B")
ws_dashboard['C5'] = "1. Dhamir"
ws_dashboard['C5'].font = bold_font
ws_dashboard['C5'].fill = gold_fill
ws_dashboard['C5'].alignment = Alignment(horizontal="center", vertical="center")

ws_dashboard['E5'] = "2. PILIH NOMOR KATA:"
ws_dashboard['E5'].font = Font(name="Arial", size=10, bold=True, color="064E3B")
ws_dashboard['F5'] = "1a"
ws_dashboard['F5'].font = Font(name="Arial", size=12, bold=True, color="B45309")
ws_dashboard['F5'].fill = gold_fill
ws_dashboard['F5'].alignment = Alignment(horizontal="center", vertical="center")

# Add Data Validation Dropdowns
dv_bentuk = DataValidation(type="list", formula1="='Daftar Dhamir & Surah'!$A$2", allow_blank=False)
ws_dashboard.add_data_validation(dv_bentuk)
dv_bentuk.add(ws_dashboard['C5'])

dv_nokat = DataValidation(type="list", formula1="='Daftar Dhamir & Surah'!$C$2:$C$16", allow_blank=False)
ws_dashboard.add_data_validation(dv_nokat)
dv_nokat.add(ws_dashboard['F5'])

# Output Cards Area
# Card 1: Arabic Word Display
ws_dashboard.merge_cells('B7:C7')
ws_dashboard['B7'] = "LAFAZ ARAB"
ws_dashboard['B7'].font = accent_font
ws_dashboard['B7'].fill = accent_fill
ws_dashboard['B7'].alignment = Alignment(horizontal="center", vertical="center")

ws_dashboard.merge_cells('B8:C9')
ws_dashboard['B8'] = "=IFERROR(VLOOKUP(F5, 'Daftar Dhamir & Surah'!C2:F16, 2, FALSE), \"-\")"
ws_dashboard['B8'].font = arabic_font_large
ws_dashboard['B8'].fill = card_fill
ws_dashboard['B8'].alignment = Alignment(horizontal="center", vertical="center")

# Card 2: Arti Kata
ws_dashboard.merge_cells('D7:F7')
ws_dashboard['D7'] = "ARTI / MAKNA KATA"
ws_dashboard['D7'].font = accent_font
ws_dashboard['D7'].fill = accent_fill
ws_dashboard['D7'].alignment = Alignment(horizontal="center", vertical="center")

ws_dashboard.merge_cells('D8:F9')
ws_dashboard['D8'] = "=IFERROR(VLOOKUP(F5, 'Daftar Dhamir & Surah'!C2:F16, 3, FALSE), \"-\")"
ws_dashboard['D8'].font = Font(name="Arial", size=14, bold=True, color="111827")
ws_dashboard['D8'].fill = card_fill
ws_dashboard['D8'].alignment = Alignment(horizontal="center", vertical="center")

# Card 3: Frekuensi Al-Qur'an
ws_dashboard.merge_cells('G7:H7')
ws_dashboard['G7'] = "FREKUENSI AL-QUR'AN"
ws_dashboard['G7'].font = accent_font
ws_dashboard['G7'].fill = accent_fill
ws_dashboard['G7'].alignment = Alignment(horizontal="center", vertical="center")

ws_dashboard.merge_cells('G8:H9')
ws_dashboard['G8'] = "=IFERROR(VLOOKUP(F5, 'Daftar Dhamir & Surah'!C2:F16, 4, FALSE), \"-\")"
ws_dashboard['G8'].font = Font(name="Arial", size=14, bold=True, color="047857")
ws_dashboard['G8'].fill = card_fill
ws_dashboard['G8'].alignment = Alignment(horizontal="center", vertical="center")

# References Table Header
ws_dashboard['B11'] = "DAFTAR RUJUKAN SURAT & AYAT AL-QUR'AN"
ws_dashboard['B11'].font = Font(name="Arial", size=12, bold=True, color="064E3B")

table_cols = [('B', 'No'), ('C', 'Bentuk Kata'), ('D', 'No Kata'), ('E', 'Kata Arab'), ('F', 'Arti Kata'), ('G', 'No. SURAT'), ('H', 'No. AYAT')]
for col_letter, title in table_cols:
    cell = ws_dashboard[f"{col_letter}12"]
    cell.value = title
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Insert dynamic FILTER formula for Excel 365 / modern Excel, with fallback helper
ws_dashboard['B13'] = "=IFERROR(FILTER('Data Master'!A2:H130, 'Data Master'!C2:C130=F5), \"Pilih Nomor Kata di atas untuk memuat daftar ayat\")"
ws_dashboard['B13'].font = normal_font

# Auto-adjust column widths
for ws in [ws_dashboard, ws_master, ws_dict]:
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

ws_dashboard.column_dimensions['A'].width = 4
ws_dashboard.column_dimensions['B'].width = 18
ws_dashboard.column_dimensions['C'].width = 18
ws_dashboard.column_dimensions['D'].width = 16
ws_dashboard.column_dimensions['E'].width = 18
ws_dashboard.column_dimensions['F'].width = 24
ws_dashboard.column_dimensions['G'].width = 16
ws_dashboard.column_dimensions['H'].width = 16

# Save output
wb.save('d:/Dhamir/DHAMIR_Interaktif.xlsx')
print("Berhasil membuat file Excel interaktif: d:/Dhamir/DHAMIR_Interaktif.xlsx")
