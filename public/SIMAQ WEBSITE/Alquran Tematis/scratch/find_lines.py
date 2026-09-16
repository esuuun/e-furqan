with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '</style>' in line:
            print('End of style line:', i+1)
        elif 'mode-nav-tabs' in line:
            print('mode-nav-tabs line:', i+1)
        elif 'id="search-nav-container"' in line:
            print('search-nav-container line:', i+1)
        elif 'id="search-view-wrapper"' in line:
            print('search-view-wrapper line:', i+1)
        elif 'function buildVerseIndex(' in line:
            print('buildVerseIndex line:', i+1)
        elif 'function switchMainMode(' in line:
            print('switchMainMode line:', i+1)
        elif 'function tanyaAI(' in line:
            print('tanyaAI line:', i+1)
