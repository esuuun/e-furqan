import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
import os
import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
excel_src = os.path.join(BASE_DIR, 'KAMUS Harf Ghair Amil.xlsx')

wb_orig = openpyxl.load_workbook(excel_src, data_only=True)
sheet_orig = wb_orig['KAMUS KATA'] if 'KAMUS KATA' in wb_orig.sheetnames else wb_orig.active
rows = list(sheet_orig.iter_rows(values_only=True))
header = [str(c).strip() if c is not None else '' for c in rows[0]]

def standardize_cat(raw_b):
    raw_b = str(raw_b).strip() if raw_b else ''
    if raw_b.startswith('1.'): return '1. Harf Nafyi'
    if raw_b.startswith('2.'): return '2. Harf Tahqiq Taswif'
    if raw_b.startswith('3.'): return '3. Harf Syarat'
    if raw_b.startswith('4.'): return '4. Harf Mashdariyah'
    if raw_b.startswith('5.'): return '5. Harf Zaidah'
    if 'ISTIFHAM' in raw_b.upper(): return '6. Harf Istifham'
    if 'JAWAB' in raw_b.upper(): return '7. Harf Jawab'
    if 'IBTIDA' in raw_b.upper(): return '8. Harf Ibtida\''
    if 'TAFSHIL' in raw_b.upper(): return '9. Harf Tafshil'
    if 'MUFAJAAH' in raw_b.upper(): return '10. Harf Mufaja\'ah'
    if 'MUFASSIRAH' in raw_b.upper(): return '11. Harf Mufassirah'
    if 'ISTIFTAHIYAH' in raw_b.upper(): return '12. Harf Istiftahiyah'
    if 'RADA' in raw_b.upper(): return '13. Harf Rada\''
    if 'TA\'AJUB' in raw_b.upper() or 'TAAJUB' in raw_b.upper(): return '14. Harf Ta\'ajjub'
    if 'FARIQAH' in raw_b.upper(): return '15. Harf Fariqah'
    if 'MAUTHI' in raw_b.upper(): return '16. Harf Mauthi\'ah'
    if 'MABANY' in raw_b.upper(): return '17. Harf Mabany'
    return raw_b

# Parse data
data = []
unique_harfs = {}
categories_set = set()

for r in rows[1:]:
    if not any(r):
        continue
    item = dict(zip(header, r))
    raw_b = item.get('Bentuk Kata')
    nk = item.get('No kata')
    k = item.get('Kata')
    ak = item.get('Arti kata')
    fk = item.get('Frek kata')
    surat = item.get('SURAT')
    ayat = item.get('AYAT')
    
    if not raw_b or nk is None or surat is None or ayat is None:
        continue
        
    std_b = standardize_cat(raw_b)
    nk_str = str(nk).strip()
    k_str = str(k).strip() if k is not None else ''
    ak_str = str(ak).strip() if ak is not None else ''
    
    try:
        s_int = int(surat)
        a_int = int(ayat)
    except:
        continue
        
    categories_set.add(std_b)
    if nk_str not in unique_harfs:
        unique_harfs[nk_str] = {
            'Bentuk': std_b,
            'No': nk_str,
            'Kata': k_str,
            'Arti': ak_str,
            'Frek': fk if fk is not None else '-'
        }
        
    data.append({
        'Bentuk Kata': std_b,
        'No kata': int(nk_str) if nk_str.isdigit() else nk_str,
        'Kata': k_str,
        'Arti kata': ak_str,
        'Frek kata': fk,
        'SURAT': s_int,
        'AYAT': a_int
    })

wb_orig.close()

# Create new workbook
wb = openpyxl.Workbook()

# Setup sheets
ws_dashboard = wb.active
ws_dashboard.title = "Dashboard Interaktif"
ws_master = wb.create_sheet(title="Data Master")
ws_dict = wb.create_sheet(title="Daftar Harf & Surah")

# Color Styles (Emerald & Gold)
header_fill = PatternFill(start_color="064E3B", end_color="064E3B", fill_type="solid") # Dark emerald
header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")

gold_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Soft gold
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
# 2. Populate "Daftar Harf & Surah" (For Validation & Lookup)
# ----------------------------------------------------
ws_dict.append(['Bentuk Harf List', '', 'No Kata', 'Kata Arab', 'Arti Kata', 'Frekuensi', 'Kategori'])
ws_dict.cell(row=1, column=1).fill = header_fill
ws_dict.cell(row=1, column=1).font = header_font
for col in range(3, 8):
    cell = ws_dict.cell(row=1, column=col)
    cell.fill = header_fill
    cell.font = header_font

sorted_cats = sorted(list(categories_set), key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else 99)
for idx, cat in enumerate(sorted_cats, start=2):
    ws_dict.cell(row=idx, column=1, value=cat)

sorted_no_kata = sorted(list(unique_harfs.keys()), key=lambda x: int(x) if x.isdigit() else 999)
for r_idx, nk in enumerate(sorted_no_kata, start=2):
    info = unique_harfs.get(nk, {})
    ws_dict.cell(row=r_idx, column=3, value=int(nk) if nk.isdigit() else nk)
    ws_dict.cell(row=r_idx, column=4, value=info.get('Kata', ''))
    ws_dict.cell(row=r_idx, column=5, value=info.get('Arti', ''))
    ws_dict.cell(row=r_idx, column=6, value=info.get('Frek', '-'))
    ws_dict.cell(row=r_idx, column=7, value=info.get('Bentuk', ''))

# ----------------------------------------------------
# 3. Build "Dashboard Interaktif"
# ----------------------------------------------------
# Title
ws_dashboard.merge_cells('B2:H2')
ws_dashboard['B2'] = "DASHBOARD EKSPLORASI HARF GHAIR 'AMIL AL-QUR'AN"
ws_dashboard['B2'].font = title_font
ws_dashboard['B2'].alignment = Alignment(horizontal="center", vertical="center")

ws_dashboard.merge_cells('B3:H3')
ws_dashboard['B3'] = "Pilih 'Bentuk Harf' dan 'Nomor Kata' di bawah ini untuk melihat detail kata, arti, frekuensi, serta rujukan surat & ayatnya secara otomatis."
ws_dashboard['B3'].font = subtitle_font
ws_dashboard['B3'].alignment = Alignment(horizontal="center", vertical="center")

# Dropdown Inputs Box
ws_dashboard['B5'] = "1. PILIH BENTUK HARF:"
ws_dashboard['B5'].font = Font(name="Arial", size=10, bold=True, color="064E3B")
ws_dashboard['C5'] = "1. Harf Nafyi"
ws_dashboard['C5'].font = bold_font
ws_dashboard['C5'].fill = gold_fill
ws_dashboard['C5'].alignment = Alignment(horizontal="center", vertical="center")

ws_dashboard['E5'] = "2. PILIH NOMOR KATA:"
ws_dashboard['E5'].font = Font(name="Arial", size=10, bold=True, color="064E3B")
ws_dashboard['F5'] = 1
ws_dashboard['F5'].font = Font(name="Arial", size=12, bold=True, color="B45309")
ws_dashboard['F5'].fill = gold_fill
ws_dashboard['F5'].alignment = Alignment(horizontal="center", vertical="center")

# Add Data Validation Dropdowns
cat_max_row = len(sorted_cats) + 1
dv_bentuk = DataValidation(type="list", formula1=f"='Daftar Harf & Surah'!$A$2:$A${cat_max_row}", allow_blank=False)
ws_dashboard.add_data_validation(dv_bentuk)
dv_bentuk.add(ws_dashboard['C5'])

nk_max_row = len(sorted_no_kata) + 1
dv_nokat = DataValidation(type="list", formula1=f"='Daftar Harf & Surah'!$C$2:$C${nk_max_row}", allow_blank=False)
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
ws_dashboard['B8'] = f"=IFERROR(VLOOKUP(F5, 'Daftar Harf & Surah'!C2:F{nk_max_row}, 2, FALSE), \"-\")"
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
ws_dashboard['D8'] = f"=IFERROR(VLOOKUP(F5, 'Daftar Harf & Surah'!C2:F{nk_max_row}, 3, FALSE), \"-\")"
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
ws_dashboard['G8'] = f"=IFERROR(VLOOKUP(F5, 'Daftar Harf & Surah'!C2:F{nk_max_row}, 4, FALSE), \"-\")"
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

total_master_rows = len(data) + 1
ws_dashboard['B13'] = f"=IFERROR(FILTER('Data Master'!A2:H{total_master_rows}, 'Data Master'!C2:C{total_master_rows}=F5), \"Pilih Nomor Kata di atas untuk memuat daftar ayat\")"
ws_dashboard['B13'].font = normal_font

# Auto-adjust column widths
for ws in [ws_dashboard, ws_master, ws_dict]:
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

ws_dashboard.column_dimensions['A'].width = 4
ws_dashboard.column_dimensions['B'].width = 18
ws_dashboard.column_dimensions['C'].width = 24
ws_dashboard.column_dimensions['D'].width = 16
ws_dashboard.column_dimensions['E'].width = 20
ws_dashboard.column_dimensions['F'].width = 30
ws_dashboard.column_dimensions['G'].width = 16
ws_dashboard.column_dimensions['H'].width = 16

# Save output
output_path = os.path.join(BASE_DIR, 'Harf_Ghair_Amil_Interaktif.xlsx')
wb.save(output_path)
print(f"Berhasil membuat file Excel interaktif: {output_path}")
print(f"Total baris Data Master: {len(data)}, Total Kategori: {len(sorted_cats)}, Total Kata: {len(sorted_no_kata)}")
