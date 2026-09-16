import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix search filtering in renderAyatReferences
search_old = """    } else if (state.lang === 'es') {
          sArti = occ.suratArtiES;
          tArti = occ.teksArtiES;
        }"""

search_new = """    } else if (state.lang === 'es') {
          sArti = occ.suratArtiES;
          tArti = occ.teksArtiES;
        } else if (state.lang === 'tr') {
          sArti = occ.suratArtiTR;
          tArti = occ.teksArtiTR;
        }"""

text = text.replace(search_old, search_new)

# 2. Fix activeSuratArti and activeTeksArti in renderAyatReferences
card_old = """    } else if (state.lang === 'es') {
      activeSuratArti = occ.suratArtiES || occ.suratArtiEN || '';
      activeTeksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    }"""

card_new = """    } else if (state.lang === 'es') {
      activeSuratArti = occ.suratArtiES || occ.suratArtiEN || '';
      activeTeksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'tr') {
      activeSuratArti = occ.suratArtiTR || occ.suratArtiEN || '';
      activeTeksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    }"""

text = text.replace(card_old, card_new)

# 3. Clean up the accidental topic block in buildAiPrompt variable setup
prompt_var_old = """    } else if (state.lang === 'zh') {
      teksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'tr') {
      if (topic === 'nahwu') {
        return `Lütfen Kur'an-ı Kerim ${suratNama} Suresi (${surat}), ${ayat}. Ayetinde geçen "${kata}" (${noKata}, ${bentuk}) kelimesinin Arapça Nahiv/Sarf kurallarını ve İ'rab analizini ayrıntılı olarak açıklayınız:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nLütfen şu hususları detaylandırınız:\\n1. "${kata}" kelimesinin cümle içindeki sentaktik konumu ve İ'rab alameti (Merfû / Mansûb / Mecrûr).\\n2. Morfolojik kategorisi (Dhamir / Mevsul / Şart vb. türü) ve zamir özellikleri (Munfasıl / Muttasıl vb.).\\n3. Gramer notları: ${grammarDesc || "Kur'an'daki standart kullanımı"}.`;
      } else if (topic === 'tafsir') {
        return `Lütfen ${suratNama} Suresi (${surat}), ${ayat}. Ayeti için özlü ve bağlamsal bir Tefsir açıklaması sununuz:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nÖzellikle seçilen "${kata}" kelimesine / zamirine odaklanarak; bu ayetin temel hikmeti, nüzul sebebi (varsa sebebi nüzul) ve içerdiği teolojik mesaj nedir?`;
      } else {
        return `Lütfen ${suratNama} Suresi (${surat}), ${ayat}. Ayetinde "${kata}" kelimesinin tercih edilmesindeki Kur'an Belâğatı ve edebî incelikleri açıklayınız:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nNeden özellikle bu zamir / kelime formu tercih edilmiştir? Ayetin ahengine, anlamına ve vurgusuna ne gibi bir edebî derinlik katmaktadır?`;
      }
    } else if (state.lang === 'es') {
      teksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'tr') {
      teksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }"""

prompt_var_new = """    } else if (state.lang === 'zh') {
      teksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'es') {
      teksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'tr') {
      teksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }"""

text = text.replace(prompt_var_old, prompt_var_new)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied final patch to app.js!")
