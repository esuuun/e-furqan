import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the broken titlePrefix block
broken_mawshul = """        if (group.bentuk && group.bentuk.includes('Mawshul')) {
          if (state.lang === 'en') titlePrefix = 'Quranic Relative Pronoun (Mawshul)';
    } else if (state.lang === 'ms') titlePrefix = 'Isim Mawshul Al-Qur\\'an';
    } else if (state.lang === 'fr') titlePrefix = 'Pronom Relatif du Coran (Isim Mawshul)';
    } else if (state.lang === 'de') titlePrefix = 'Koranisches Relativpronomen (Mawshul)';
    } else if (state.lang === 'ur') titlePrefix = 'قرآنی اسم موصول (Mawshul)';
    } else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी संबंधवाचक सर्वनाम (Mawshul)';
    } else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সম্বন্ধবাচক সর্বনাম (Mawshul)';
    } else if (state.lang === 'ru') titlePrefix = 'Коранические относительные местоимения (Mawshul)';
    } else if (state.lang === 'zh') titlePrefix = '古兰经关系代词 (Mawshul)';
    } else if (state.lang === 'es') titlePrefix = 'Pronombre Relativo del Corán (Mawshul)';
    } else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim İsmi Mevsul (Mawshul)';
          else titlePrefix = 'Isim Mawshul Al-Qur\\'an';
        } else {
          if (state.lang === 'en') titlePrefix = 'Quranic Pronoun (Dhamir)';
    } else if (state.lang === 'ms') titlePrefix = 'Dhamir Al-Qur\\'an';
    } else if (state.lang === 'fr') titlePrefix = 'Pronom du Coran (Dhamir)';
    } else if (state.lang === 'de') titlePrefix = 'Koranisches Pronomen (Dhamir)';
    } else if (state.lang === 'ur') titlePrefix = 'قرآنی ضمیر (Dhamir)';
    } else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी सर्वनाम (Dhamir)';
    } else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সর্বনাম (Dhamir)';
    } else if (state.lang === 'ru') titlePrefix = 'Коранические местоимения (Dhamir)';
    } else if (state.lang === 'zh') titlePrefix = '古兰经人称代词 (Dhamir)';
    } else if (state.lang === 'es') titlePrefix = 'Pronombre del Corán (Dhamir)';
    } else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim Zamirleri (Dhamir)';
          else titlePrefix = 'Dhamir Al-Qur\\'an';
        }"""

clean_mawshul = """        if (group.bentuk && group.bentuk.includes('Mawshul')) {
          if (state.lang === 'en') titlePrefix = 'Quranic Relative Pronoun (Mawshul)';
          else if (state.lang === 'ms') titlePrefix = 'Isim Mawshul Al-Qur\\'an';
          else if (state.lang === 'fr') titlePrefix = 'Pronom Relatif du Coran (Isim Mawshul)';
          else if (state.lang === 'de') titlePrefix = 'Koranisches Relativpronomen (Mawshul)';
          else if (state.lang === 'ur') titlePrefix = 'قرآنی اسم موصول (Mawshul)';
          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी संबंधवाचक सर्वनाम (Mawshul)';
          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সম্বন্ধবাচক সর্বনাম (Mawshul)';
          else if (state.lang === 'ru') titlePrefix = 'Коранические относительные местоимения (Mawshul)';
          else if (state.lang === 'zh') titlePrefix = '古兰经关系代词 (Mawshul)';
          else if (state.lang === 'es') titlePrefix = 'Pronombre Relativo del Corán (Mawshul)';
          else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim İsmi Mevsul (Mawshul)';
          else titlePrefix = 'Isim Mawshul Al-Qur\\'an';
        } else {
          if (state.lang === 'en') titlePrefix = 'Quranic Pronoun (Dhamir)';
          else if (state.lang === 'ms') titlePrefix = 'Dhamir Al-Qur\\'an';
          else if (state.lang === 'fr') titlePrefix = 'Pronom du Coran (Dhamir)';
          else if (state.lang === 'de') titlePrefix = 'Koranisches Pronomen (Dhamir)';
          else if (state.lang === 'ur') titlePrefix = 'قرآنی ضمیر (Dhamir)';
          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी सर्वनाम (Dhamir)';
          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সর্বনাম (Dhamir)';
          else if (state.lang === 'ru') titlePrefix = 'Коранические местоимения (Dhamir)';
          else if (state.lang === 'zh') titlePrefix = '古兰经人称代词 (Dhamir)';
          else if (state.lang === 'es') titlePrefix = 'Pronombre del Corán (Dhamir)';
          else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim Zamirleri (Dhamir)';
          else titlePrefix = 'Dhamir Al-Qur\\'an';
        }"""

text = text.replace(broken_mawshul, clean_mawshul)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced titlePrefix cleanly!")
