with open('scratch/apply_updates.py', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if "Al-Qur'an" in line or "Al-Qur\'an" in line:
            print(f"{i+1}: {line.strip()}")
