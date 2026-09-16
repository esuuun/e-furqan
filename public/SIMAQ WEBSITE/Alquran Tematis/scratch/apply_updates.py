import re
import os
import shutil

def main():
    html_file = 'index.html'
    backup_file = 'scratch/index.html.bak'
    
    # 1. Create backup
    shutil.copy2(html_file, backup_file)
    print(f"Backup created at {backup_file}")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # -------------------------------------------------------------
    # CSS to inject before </style>
    # -------------------------------------------------------------
    css_additions = """
        /* ==========================================================================
           Fitur Smart Search, Keyword Search & Tanya AI (Zero Hallucination) Styling
           ========================================================================== */
        /* Smart Search Input & Suggestions */
        .smart-search-box-wrap {
            position: relative;
            width: 100%;
            margin-bottom: 1.25rem;
        }
        .smart-search-input-inner {
            position: relative;
            display: flex;
            align-items: center;
            width: 100%;
        }
        .smart-search-input-inner .search-icon {
            position: absolute;
            left: 1.1rem;
            color: var(--accent);
            pointer-events: none;
        }
        .smart-search-input {
            width: 100%;
            background: #0f172a;
            color: #f8fafc;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 0.95rem 3rem 0.95rem 3.2rem;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 500;
            outline: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
            box-sizing: border-box;
        }
        .smart-search-input:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px rgba(20, 184, 166, 0.2), 0 6px 20px rgba(0, 0, 0, 0.35);
            background: #111e33;
        }
        .btn-clear-input {
            position: absolute;
            right: 1rem;
            background: rgba(100, 116, 139, 0.25);
            color: #94a3b8;
            border: none;
            width: 26px;
            height: 26px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 700;
            transition: all 0.2s;
        }
        .btn-clear-input:hover {
            background: #ef4444;
            color: #fff;
        }
        .smart-suggestions-dropdown {
            position: absolute;
            top: calc(100% + 6px);
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.98);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(20, 184, 166, 0.45);
            border-radius: 12px;
            max-height: 320px;
            overflow-y: auto;
            z-index: 1000;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
            padding: 0.4rem;
        }
        .suggestion-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.15s ease;
            color: #cbd5e1;
            font-size: 0.95rem;
            border-bottom: 1px solid rgba(30, 41, 59, 0.5);
        }
        .suggestion-item:last-child {
            border-bottom: none;
        }
        .suggestion-item:hover, .suggestion-item.active {
            background: rgba(20, 184, 166, 0.15);
            color: #5eead4;
            transform: translateX(3px);
        }
        .suggestion-left {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            font-weight: 600;
        }
        .suggestion-badge {
            background: rgba(59, 130, 246, 0.15);
            border: 1px solid rgba(59, 130, 246, 0.35);
            color: #93c5fd;
            font-size: 0.75rem;
            padding: 0.15rem 0.5rem;
            border-radius: 6px;
            font-weight: 700;
        }
        .suggestion-arabic {
            font-family: 'Amiri', serif;
            font-size: 1.25rem;
            color: #fbbf24;
            direction: rtl;
        }

        /* Popular Quick Verses / Chips */
        .popular-verses-row {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }
        .popular-label {
            font-size: 0.85rem;
            font-weight: 600;
            color: #94a3b8;
            margin-right: 0.25rem;
        }
        .popular-verse-chip {
            background: rgba(30, 41, 59, 0.7);
            color: #cbd5e1;
            border: 1px solid #334155;
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }
        .popular-verse-chip:hover {
            background: rgba(20, 184, 166, 0.2);
            border-color: var(--accent);
            color: #5eead4;
            transform: translateY(-2px);
        }

        /* Keyword Search Mode Styling */
        .btn-keyword-submit {
            position: absolute;
            right: 0.4rem;
            background: linear-gradient(135deg, #14b8a6, #0d9488);
            color: #0b0f19;
            border: none;
            padding: 0.55rem 1.25rem;
            border-radius: 8px;
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-keyword-submit:hover {
            background: linear-gradient(135deg, #2dd4bf, #14b8a6);
            box-shadow: 0 4px 15px rgba(20, 184, 166, 0.4);
        }
        .keyword-filters-row {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            flex-wrap: wrap;
            margin-top: 1.1rem;
            padding-top: 1.1rem;
            border-top: 1px solid rgba(30, 41, 59, 0.7);
        }
        .filter-label {
            font-size: 0.85rem;
            font-weight: 600;
            color: #94a3b8;
            margin-right: 0.25rem;
        }
        .filter-pill-btn {
            background: #1e293b;
            color: #94a3b8;
            border: 1px solid #334155;
            padding: 0.4rem 0.95rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .filter-pill-btn:hover {
            border-color: #475569;
            color: #f8fafc;
        }
        .filter-pill-btn.active {
            background: rgba(20, 184, 166, 0.2);
            border-color: var(--accent);
            color: #5eead4;
            box-shadow: 0 0 15px rgba(20, 184, 166, 0.25);
        }

        /* Keyword Results Layout */
        .keyword-stats-banner {
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.9), rgba(15, 23, 42, 0.95));
            border: 1px solid rgba(20, 184, 166, 0.3);
            border-radius: 14px;
            padding: 1.1rem 1.5rem;
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            text-align: left;
        }
        .keyword-stats-info {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            color: #cbd5e1;
            font-size: 1rem;
        }
        .keyword-stats-info strong {
            color: #fbbf24;
        }
        .keyword-stats-badges {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        .keyword-section-title {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 1.25rem;
            font-weight: 700;
            color: #f8fafc;
            margin: 2.5rem 0 1.25rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(30, 41, 59, 0.8);
            text-align: left;
        }
        .keyword-section-title span.badge {
            background: rgba(20, 184, 166, 0.15);
            color: #5eead4;
            font-size: 0.82rem;
            font-weight: 700;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            border: 1px solid rgba(20, 184, 166, 0.3);
        }
        .keyword-uraian-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.25rem;
        }
        .keyword-uraian-card {
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.85), rgba(15, 23, 42, 0.9));
            border: 1px solid rgba(30, 41, 59, 0.9);
            border-radius: 14px;
            padding: 1.5rem;
            transition: all 0.25s ease;
            text-align: left;
        }
        .keyword-uraian-card:hover {
            border-color: rgba(20, 184, 166, 0.5);
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35);
        }
        .keyword-uraian-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 0.85rem;
            flex-wrap: wrap;
        }
        .keyword-uraian-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #5eead4;
            line-height: 1.4;
            flex: 1;
        }
        .keyword-verse-count-badge {
            background: rgba(245, 158, 11, 0.15);
            border: 1px solid rgba(245, 158, 11, 0.35);
            color: #fbbf24;
            padding: 0.2rem 0.65rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
            white-space: nowrap;
        }
        .keyword-uraian-path {
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
            font-size: 0.88rem;
            color: #94a3b8;
            margin-bottom: 1.25rem;
            background: rgba(11, 15, 25, 0.5);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border: 1px solid #1e293b;
        }
        .keyword-uraian-path strong {
            color: #cbd5e1;
        }

        /* Keyword Highlights */
        mark.search-highlight {
            background: rgba(245, 158, 11, 0.35);
            color: #fef08a;
            font-weight: 700;
            border-radius: 4px;
            padding: 0.05rem 0.3rem;
            box-shadow: 0 0 8px rgba(245, 158, 11, 0.3);
        }

        /* Keyword Verse Card */
        .keyword-verse-card {
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.85), rgba(15, 23, 42, 0.95));
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 1.75rem;
            margin-bottom: 1.5rem;
            text-align: left;
            transition: all 0.25s ease;
        }
        .keyword-verse-card:hover {
            border-color: rgba(20, 184, 166, 0.4);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
        }
        .keyword-verse-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-bottom: 1.25rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid rgba(30, 41, 59, 0.8);
        }
        .keyword-verse-title {
            font-size: 1.18rem;
            font-weight: 700;
            color: #fbbf24;
        }

        /* ==========================================================================
           Zero-Hallucination AI Modal & Dialog Styling
           ========================================================================== */
        .ai-modal-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(4, 7, 15, 0.85);
            backdrop-filter: blur(10px);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1.5rem 1rem;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0.3s ease;
        }
        .ai-modal-backdrop.active {
            opacity: 1;
            visibility: visible;
        }
        .ai-modal-window {
            background: linear-gradient(145deg, #111827, #0b1120);
            border: 1px solid rgba(20, 184, 166, 0.45);
            border-radius: 20px;
            max-width: 840px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            padding: 2.2rem;
            box-shadow: 0 25px 60px -10px rgba(0, 0, 0, 0.85), 0 0 30px rgba(20, 184, 166, 0.15);
            position: relative;
            transform: translateY(20px) scale(0.97);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: left;
            box-sizing: border-box;
        }
        .ai-modal-backdrop.active .ai-modal-window {
            transform: translateY(0) scale(1);
        }
        .ai-modal-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1.25rem;
            border-bottom: 1px solid rgba(30, 41, 59, 0.8);
        }
        .ai-header-left {
            flex: 1;
        }
        .ai-modal-title-row {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
            margin-bottom: 0.35rem;
        }
        .ai-modal-title {
            font-size: 1.45rem;
            font-weight: 700;
            color: #f8fafc;
            margin: 0;
        }
        .ai-badge-zero {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.45);
            color: #34d399;
            font-size: 0.8rem;
            font-weight: 700;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
        }
        .ai-modal-subtitle {
            font-size: 0.9rem;
            color: #94a3b8;
            margin: 0;
            line-height: 1.5;
        }
        .ai-modal-close-btn {
            background: rgba(30, 41, 59, 0.7);
            color: #94a3b8;
            border: 1px solid #334155;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
            font-weight: 700;
            transition: all 0.2s;
            flex-shrink: 0;
        }
        .ai-modal-close-btn:hover {
            background: #ef4444;
            color: #ffffff;
            border-color: #ef4444;
            transform: scale(1.08);
        }

        /* Context Card in Modal */
        .ai-context-card {
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(30, 41, 59, 0.8);
            border-radius: 14px;
            padding: 1.4rem;
            margin-bottom: 1.5rem;
        }
        .ai-context-verse-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.85rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .ai-context-verse-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #fbbf24;
        }
        .ai-context-arabic {
            font-family: 'Amiri', serif;
            font-size: 1.65rem;
            line-height: 2.2;
            color: #f8fafc;
            direction: rtl;
            text-align: right;
            background: rgba(11, 15, 25, 0.6);
            padding: 1rem 1.25rem;
            border-radius: 10px;
            margin-bottom: 0.85rem;
            border: 1px solid rgba(30, 41, 59, 0.5);
        }
        .ai-context-translation {
            font-size: 0.98rem;
            line-height: 1.7;
            color: #cbd5e1;
            margin-bottom: 0.85rem;
        }
        .ai-context-thematic-tag {
            font-size: 0.82rem;
            color: #5eead4;
            background: rgba(20, 184, 166, 0.12);
            border: 1px solid rgba(20, 184, 166, 0.3);
            padding: 0.35rem 0.75rem;
            border-radius: 8px;
            display: inline-block;
        }

        /* Study Mode Tabs inside Modal */
        .ai-section-label {
            font-size: 0.85rem;
            font-weight: 700;
            color: #e2e8f0;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.6rem;
            display: block;
        }
        .ai-mode-tabs {
            display: flex;
            gap: 0.6rem;
            flex-wrap: wrap;
            margin-bottom: 1.25rem;
        }
        .ai-mode-tab {
            background: #1e293b;
            color: #94a3b8;
            border: 1px solid #334155;
            padding: 0.55rem 1.1rem;
            border-radius: 999px;
            font-size: 0.88rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .ai-mode-tab:hover {
            border-color: #64748b;
            color: #f8fafc;
        }
        .ai-mode-tab.active {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(124, 58, 237, 0.35));
            border-color: #8b5cf6;
            color: #c4b5fd;
            box-shadow: 0 0 15px rgba(139, 92, 246, 0.25);
        }
        .ai-custom-input {
            width: 100%;
            background: #0f172a;
            color: #f8fafc;
            border: 1px solid #475569;
            border-radius: 10px;
            padding: 0.8rem 1rem;
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            outline: none;
            transition: border-color 0.2s;
            box-sizing: border-box;
        }
        .ai-custom-input:focus {
            border-color: #8b5cf6;
            box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.25);
        }

        /* Prompt Box & Preview */
        .ai-prompt-preview-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .btn-toggle-prompt-view {
            background: none;
            border: none;
            color: var(--accent);
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: underline;
        }
        .ai-prompt-box {
            background: rgba(11, 15, 25, 0.7);
            border: 1px solid #1e293b;
            border-radius: 10px;
            padding: 1rem;
            font-family: 'Inter', monospace, sans-serif;
            font-size: 0.85rem;
            color: #94a3b8;
            line-height: 1.6;
            max-height: 140px;
            overflow-y: auto;
            white-space: pre-wrap;
            margin-bottom: 1.5rem;
            transition: max-height 0.3s ease;
        }
        .ai-prompt-box.expanded {
            max-height: 380px;
            border-color: #475569;
            color: #cbd5e1;
        }

        /* Summary Card */
        .ai-summary-card {
            background: rgba(20, 184, 166, 0.1);
            border: 1px solid rgba(20, 184, 166, 0.35);
            border-radius: 12px;
            padding: 1.25rem;
            margin-bottom: 1.5rem;
        }
        .ai-summary-title {
            font-size: 0.95rem;
            font-weight: 700;
            color: #5eead4;
            margin-bottom: 0.5rem;
        }
        .ai-summary-text {
            font-size: 0.92rem;
            color: #cbd5e1;
            line-height: 1.7;
        }

        /* Modal Actions Row */
        .ai-actions-row {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            align-items: center;
        }
        .ai-btn-action {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.75rem 1.25rem;
            border-radius: 10px;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.25s ease;
            user-select: none;
            border: 1px solid transparent;
        }
        .ai-btn-action.copy-prompt-btn {
            background: linear-gradient(135deg, #10b981, #059669);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
        }
        .ai-btn-action.copy-prompt-btn:hover {
            background: linear-gradient(135deg, #34d399, #10b981);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45);
        }
        .ai-btn-action.chatgpt-btn {
            background: rgba(16, 185, 129, 0.15);
            border-color: rgba(16, 185, 129, 0.4);
            color: #34d399;
        }
        .ai-btn-action.chatgpt-btn:hover {
            background: rgba(16, 185, 129, 0.3);
            transform: translateY(-2px);
        }
        .ai-btn-action.gemini-btn {
            background: rgba(59, 130, 246, 0.15);
            border-color: rgba(59, 130, 246, 0.4);
            color: #93c5fd;
        }
        .ai-btn-action.gemini-btn:hover {
            background: rgba(59, 130, 246, 0.3);
            transform: translateY(-2px);
        }
        .ai-btn-action.claude-btn {
            background: rgba(245, 158, 11, 0.15);
            border-color: rgba(245, 158, 11, 0.4);
            color: #fbbf24;
        }
        .ai-btn-action.claude-btn:hover {
            background: rgba(245, 158, 11, 0.3);
            transform: translateY(-2px);
        }
        .ai-btn-action.summary-btn {
            background: rgba(20, 184, 166, 0.12);
            border-color: rgba(20, 184, 166, 0.35);
            color: #5eead4;
        }
        .ai-btn-action.summary-btn:hover {
            background: rgba(20, 184, 166, 0.25);
            transform: translateY(-2px);
        }

        /* Toast Notification */
        .ai-toast {
            position: fixed;
            bottom: 2.5rem;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: linear-gradient(135deg, #10b981, #059669);
            color: #ffffff;
            padding: 0.85rem 1.75rem;
            border-radius: 999px;
            font-size: 0.95rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 25px rgba(16, 185, 129, 0.4);
            z-index: 100000;
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .ai-toast.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
    """

    # Inject CSS before </style>
    if '</style>' in content:
        content = content.replace('    </style>', css_additions + '\n    </style>', 1)
        print("Injected CSS styles successfully.")
    else:
        print("ERROR: </style> not found!")
        return

    # -------------------------------------------------------------
    # HTML Mode Tabs Update
    # -------------------------------------------------------------
    old_tabs = """        <!-- Mode Navigation Tabs -->
        <div class="mode-nav-tabs">
            <button id="tab-btn-thematic" class="mode-tab-btn active" onclick="switchMainMode('thematic')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                <span id="tab-text-thematic" data-i18n-orig="Jelajah Tematis">Jelajah Tematis</span>
            </button>
            <button id="tab-btn-search" class="mode-tab-btn" onclick="switchMainMode('search')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <span id="tab-text-search" data-i18n-orig="Cari Surat & Ayat">Cari Surat & Ayat</span>
            </button>
        </div>"""

    new_tabs = """        <!-- Mode Navigation Tabs -->
        <div class="mode-nav-tabs">
            <button id="tab-btn-thematic" class="mode-tab-btn active" onclick="switchMainMode('thematic')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                <span id="tab-text-thematic" data-i18n-orig="Jelajah Tematis">Jelajah Tematis</span>
            </button>
            <button id="tab-btn-search" class="mode-tab-btn" onclick="switchMainMode('search')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <span id="tab-text-search" data-i18n-orig="Cari Surat & Ayat">Cari Surat & Ayat</span>
            </button>
            <button id="tab-btn-keyword" class="mode-tab-btn" onclick="switchMainMode('keyword')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                <span id="tab-text-keyword" data-i18n-orig="Cari Kata (Uraian & Ayat)">Cari Kata (Uraian & Ayat)</span>
            </button>
        </div>"""

    if old_tabs in content:
        content = content.replace(old_tabs, new_tabs, 1)
        print("Updated mode-nav-tabs successfully.")
    else:
        print("ERROR: old_tabs not found!")
        return

    # -------------------------------------------------------------
    # HTML Search Nav Container (Smart Search & Quick Chips)
    # -------------------------------------------------------------
    old_search_nav_header = """            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                    <span data-i18n-orig="Pilih Surat & Nomor Ayat">Pilih Surat & Nomor Ayat</span>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan">Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan</div>
            </div>"""

    new_search_nav_header = """            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                    <span data-i18n-orig="Cari Surat & Nomor Ayat">Cari Surat & Nomor Ayat</span>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan">Ketik nama surat & ayat langsung atau pilih dari daftar untuk melihat klasifikasi tematiknya secara instan</div>
            </div>

            <!-- Smart Direct Search Input Bar -->
            <div class="smart-search-box-wrap">
                <div class="smart-search-input-inner">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <input type="text" id="smart-surah-ayat-input" class="smart-search-input" placeholder="Ketik nama surat & ayat (contoh: Al-Baqarah 255, 36:82, Yasin 82, Kahfi 10, An-Nas)..." oninput="onSmartSearchInput(this.value)" onkeydown="onSmartSearchKeydown(event)" autocomplete="off">
                    <button id="btn-clear-smart-search" class="btn-clear-input" onclick="clearSmartSearch()" style="display: none;" title="Hapus pencarian">✕</button>
                </div>
                <div id="smart-search-suggestions" class="smart-suggestions-dropdown" style="display: none;"></div>
            </div>

            <!-- Quick Access Popular Verses -->
            <div class="popular-verses-row">
                <span class="popular-label">⚡ Akses Cepat:</span>
                <button class="popular-verse-chip" onclick="selectQuickVerse(2, 255)">Ayat Kursi (2:255)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(1, 1)">Al-Fatihah (1:1)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(18, 10)">Al-Kahfi (18:10)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(36, 82)">Yasin (36:82)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(67, 1)">Al-Mulk (67:1)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(3, 190)">Ali 'Imran (3:190)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(112, 1)">Al-Ikhlas (112:1)</button>
            </div>"""

    if old_search_nav_header in content:
        content = content.replace(old_search_nav_header, new_search_nav_header, 1)
        print("Updated search_nav_header with Smart Search & Quick Chips successfully.")
    else:
        print("ERROR: old_search_nav_header not found!")
        return

    # -------------------------------------------------------------
    # HTML Keyword Nav Container & View Wrapper & Modal
    # -------------------------------------------------------------
    target_after_search_view = """        <!-- Search Verse Content View (Mode 2) -->
        <div id="search-view-wrapper" style="display: none;">
            <div id="search-content-area">
                <div class="empty-state">Silakan pilih Surat dan Nomor Ayat di atas untuk melihat klasifikasi tematiknya.</div>
            </div>
        </div>
    </div>"""

    new_keyword_and_modal_html = """        <!-- Search Verse Content View (Mode 2) -->
        <div id="search-view-wrapper" style="display: none;">
            <div id="search-content-area">
                <div class="empty-state">Silakan pilih Surat dan Nomor Ayat di atas untuk melihat klasifikasi tematiknya.</div>
            </div>
        </div>

        <!-- Keyword Search Navigation (Mode 3) -->
        <div id="keyword-nav-container" class="search-nav-card" style="display: none;">
            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <span data-i18n-orig="Pencarian Kata: Uraian & Ayat">Pencarian Kata: Uraian & Ayat</span>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Cari topik uraian tematis dan teks terjemahan ayat secara instan">Cari topik bahasan/uraian tematis dan teks terjemahan ayat berdasarkan kata kunci secara instan</div>
            </div>

            <!-- Keyword Search Input -->
            <div class="smart-search-box-wrap">
                <div class="smart-search-input-inner">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <input type="text" id="keyword-search-input" class="smart-search-input" placeholder="Ketik kata pencarian (contoh: sabar, riba, shalat, taubat, rezeki, surga)..." oninput="onKeywordInput(this.value)" onkeydown="if(event.key==='Enter')executeKeywordSearch()" autocomplete="off">
                    <button id="btn-clear-keyword-search" class="btn-clear-input" onclick="clearKeywordSearch()" style="display: none;" title="Hapus pencarian">✕</button>
                    <button class="btn-keyword-submit" onclick="executeKeywordSearch()">Cari</button>
                </div>
            </div>

            <!-- Filter Chips -->
            <div class="keyword-filters-row">
                <span class="filter-label">Filter Hasil:</span>
                <button id="filter-pill-all" class="filter-pill-btn active" onclick="setKeywordFilter('all')">Semua Hasil</button>
                <button id="filter-pill-uraian" class="filter-pill-btn" onclick="setKeywordFilter('uraian')">Hanya Uraian Tematis</button>
                <button id="filter-pill-ayat" class="filter-pill-btn" onclick="setKeywordFilter('ayat')">Hanya Teks Terjemahan Ayat</button>
            </div>

            <!-- Popular Search Keywords -->
            <div class="popular-verses-row" style="margin-top: 1rem;">
                <span class="popular-label">💡 Kata Kunci Populer:</span>
                <button class="popular-verse-chip" onclick="searchKeywordTag('sabar')">Sabar</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('riba')">Riba</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('shalat')">Shalat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('taubat')">Taubat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('rezeki')">Rezeki</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('surga')">Surga</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('neraka')">Neraka</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('orang tua')">Orang Tua</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('sedekah')">Sedekah</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('kiamat')">Kiamat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('syukur')">Syukur</button>
            </div>
        </div>

        <!-- Keyword Search Content View (Mode 3) -->
        <div id="keyword-view-wrapper" style="display: none;">
            <div id="keyword-content-area">
                <div class="empty-state">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem; display: block; color: var(--accent); opacity: 0.8;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    Ketik kata kunci di atas atau pilih salah satu kata populer untuk mencari uraian tematis dan ayat Al-Qur'an.
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Tanya AI (Zero Hallucination Guaranteed) -->
    <div id="modal-tanya-ai" class="ai-modal-backdrop" onclick="closeTanyaAIModalOnBackdrop(event)">
        <div class="ai-modal-window">
            <div class="ai-modal-header">
                <div class="ai-header-left">
                    <div class="ai-modal-title-row">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #8b5cf6;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                        <h2 class="ai-modal-title">Tanya AI Al-Qur'an</h2>
                        <span class="ai-badge-zero">🛡️ Zero Hallucination Guaranteed</span>
                    </div>
                    <p class="ai-modal-subtitle">Sistem Tanya AI bergaransi bebas halusinasi, berlandaskan rujukan mutlak nash ayat Al-Qur'an, terjemahan resmi Kemenag RI, dan kitab tafsir mu'tabar Ahlussunnah.</p>
                </div>
                <button class="ai-modal-close-btn" onclick="closeTanyaAIModal()" title="Tutup Modal">✕</button>
            </div>

            <!-- Verse Context Card -->
            <div id="ai-verse-context" class="ai-context-card">
                <!-- Injected dynamically -->
            </div>

            <!-- Study Mode Selector -->
            <div class="ai-section-label">Pilih Jenis Kajian / Pertanyaan:</div>
            <div class="ai-mode-tabs">
                <button id="ai-tab-tadabbur" class="ai-mode-tab active" onclick="setAIMode('tadabbur')">
                    💡 Tadabbur Tematis
                </button>
                <button id="ai-tab-asbab" class="ai-mode-tab" onclick="setAIMode('asbab')">
                    📜 Asbabun Nuzul Shahih
                </button>
                <button id="ai-tab-mufradat" class="ai-mode-tab" onclick="setAIMode('mufradat')">
                    🔍 Makna Kosakata (Mufradat)
                </button>
                <button id="ai-tab-custom" class="ai-mode-tab" onclick="setAIMode('custom')">
                    ❓ Ajukan Pertanyaan Sendiri
                </button>
            </div>

            <!-- Custom Question Input (shown when custom selected) -->
            <div id="ai-custom-input-wrap" style="display: none; margin-bottom: 1.25rem;">
                <input type="text" id="ai-custom-question-input" class="ai-custom-input" placeholder="Tuliskan pertanyaan spesifik Anda tentang ayat ini..." oninput="updateAIPromptPreview()">
            </div>

            <!-- Prompt Preview Box -->
            <div class="ai-prompt-preview-header">
                <span class="ai-section-label">📋 Format Prompt Anti-Halusinasi (System & Grounding Guardrails):</span>
                <button class="btn-toggle-prompt-view" onclick="togglePromptPreview()">Tampilkan/Sembunyikan Teks Lengkap</button>
            </div>
            <div id="ai-prompt-preview-box" class="ai-prompt-box"></div>

            <!-- Instant In-App Verified Summary (Tadabbur Singkat) -->
            <div id="ai-instant-summary-card" class="ai-summary-card" style="display: none;">
                <div class="ai-summary-title">📖 Catatan Tematis Terverifikasi dari Data:</div>
                <div id="ai-instant-summary-text" class="ai-summary-text"></div>
            </div>

            <!-- Action Buttons -->
            <div class="ai-actions-row">
                <button class="ai-btn-action copy-prompt-btn" onclick="copyAIPrompt()">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    Salin Prompt Anti-Halusinasi
                </button>
                <button class="ai-btn-action chatgpt-btn" onclick="openAIPlatform('chatgpt')">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="m8 12 3 3 5-5"></path></svg>
                    Tanya ChatGPT
                </button>
                <button class="ai-btn-action gemini-btn" onclick="openAIPlatform('gemini')">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    Tanya Google Gemini
                </button>
                <button class="ai-btn-action claude-btn" onclick="openAIPlatform('claude')">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 14h-2v-2h2zm0-4h-2V7h2z"></path></svg>
                    Tanya Claude
                </button>
                <button class="ai-btn-action summary-btn" onclick="toggleInstantSummary()">
                    📖 Tadabbur Cepat
                </button>
            </div>
        </div>
    </div>

    <!-- Copy Toast Notification -->
    <div id="ai-toast" class="ai-toast">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        <span id="ai-toast-message">Prompt Zero-Hallucination Berhasil Disalin!</span>
    </div>"""

    if target_after_search_view in content:
        content = content.replace(target_after_search_view, new_keyword_and_modal_html, 1)
        print("Injected keyword view and modal HTML successfully.")
    else:
        print("ERROR: target_after_search_view not found!")
        return

    # -------------------------------------------------------------
    # JavaScript logic updates:
    # 1. buildVerseIndex enhancement (index uraian and verses for keyword search)
    # 2. switchMainMode update
    # 3. Smart Search & Autocomplete
    # 4. Keyword Search engine
    # 5. Zero-Hallucination AI modal & prompt generator
    # 6. updated tanyaAI
    # -------------------------------------------------------------

    old_build_verse_index = """        function buildVerseIndex() {
            verseThematicIndex = {};
            if (!quranData) return;
            for (const [tema, pbs] of Object.entries(quranData)) {
                for (const [pb, spbs] of Object.entries(pbs)) {
                    for (const [spb, urs] of Object.entries(spbs)) {
                        for (const [ur, urData] of Object.entries(urs)) {
                            if (urData && urData.verses) {
                                urData.verses.forEach(v => {
                                    const key = `${v.surah_num}:${v.ayat_num}`;
                                    if (!verseThematicIndex[key]) {
                                        verseThematicIndex[key] = {
                                            surah_name: v.surah_name,
                                            surah_num: v.surah_num,
                                            ayat_num: v.ayat_num,
                                            arab: v.arab,
                                            indo: v.indo,
                                            audio: v.audio,
                                            topics: []
                                        };
                                    }
                                    verseThematicIndex[key].topics.push({
                                        tema: tema,
                                        pokok: pb,
                                        sub: spb,
                                        uraian: ur
                                    });
                                });
                            }
                        }
                    }
                }
            }
            console.log(`[VerseIndex] Indexed ${Object.keys(verseThematicIndex).length} unique verses across all themes.`);
        }"""

    new_build_verse_index = """        let allThematicUraianList = [];
        let allThematicVersesList = [];

        function buildVerseIndex() {
            verseThematicIndex = {};
            allThematicUraianList = [];
            if (!quranData) return;
            for (const [tema, pbs] of Object.entries(quranData)) {
                for (const [pb, spbs] of Object.entries(pbs)) {
                    for (const [spb, urs] of Object.entries(spbs)) {
                        for (const [ur, urData] of Object.entries(urs)) {
                            const vList = (urData && urData.verses) ? urData.verses : [];
                            allThematicUraianList.push({
                                tema: tema,
                                pokok: pb,
                                sub: spb,
                                uraian: ur,
                                verseCount: vList.length,
                                sampleVerses: vList.slice(0, 3)
                            });
                            if (vList.length > 0) {
                                vList.forEach(v => {
                                    const key = `${v.surah_num}:${v.ayat_num}`;
                                    if (!verseThematicIndex[key]) {
                                        verseThematicIndex[key] = {
                                            surah_name: v.surah_name,
                                            surah_num: v.surah_num,
                                            ayat_num: v.ayat_num,
                                            arab: v.arab,
                                            indo: v.indo,
                                            audio: v.audio,
                                            topics: []
                                        };
                                    }
                                    verseThematicIndex[key].topics.push({
                                        tema: tema,
                                        pokok: pb,
                                        sub: spb,
                                        uraian: ur
                                    });
                                });
                            }
                        }
                    }
                }
            }
            allThematicVersesList = Object.values(verseThematicIndex);
            console.log(`[VerseIndex] Indexed ${allThematicVersesList.length} unique verses and ${allThematicUraianList.length} thematic topics.`);
        }"""

    if old_build_verse_index in content:
        content = content.replace(old_build_verse_index, new_build_verse_index, 1)
        print("Updated buildVerseIndex successfully.")
    else:
        print("ERROR: old_build_verse_index not found!")
        return

    # Update switchMainMode
    old_switch_main_mode = """        function switchMainMode(mode) {
            stopTTS();
            activeMainMode = mode;
            const tabThematic = document.getElementById('tab-btn-thematic');
            const tabSearch = document.getElementById('tab-btn-search');
            const thematicNav = document.getElementById('thematic-nav-container');
            const searchNav = document.getElementById('search-nav-container');
            const thematicView = document.getElementById('thematic-view-wrapper');
            const searchView = document.getElementById('search-view-wrapper');

            if (mode === 'thematic') {
                if (tabThematic) tabThematic.classList.add('active');
                if (tabSearch) tabSearch.classList.remove('active');
                if (thematicNav) thematicNav.style.display = 'flex';
                if (searchNav) searchNav.style.display = 'none';
                if (thematicView) thematicView.style.display = 'block';
                if (searchView) searchView.style.display = 'none';
            } else {
                if (tabThematic) tabThematic.classList.remove('active');
                if (tabSearch) tabSearch.classList.add('active');
                if (thematicNav) thematicNav.style.display = 'none';
                if (searchNav) searchNav.style.display = 'block';
                if (thematicView) thematicView.style.display = 'none';
                if (searchView) searchView.style.display = 'block';

                // Render current search verse if not already rendered
                if (!document.getElementById('current-rendered-verse')) {
                    renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
                }
            }
        }"""

    new_switch_main_mode = """        function switchMainMode(mode) {
            stopTTS();
            activeMainMode = mode;
            const tabThematic = document.getElementById('tab-btn-thematic');
            const tabSearch = document.getElementById('tab-btn-search');
            const tabKeyword = document.getElementById('tab-btn-keyword');
            const thematicNav = document.getElementById('thematic-nav-container');
            const searchNav = document.getElementById('search-nav-container');
            const keywordNav = document.getElementById('keyword-nav-container');
            const thematicView = document.getElementById('thematic-view-wrapper');
            const searchView = document.getElementById('search-view-wrapper');
            const keywordView = document.getElementById('keyword-view-wrapper');

            // Reset all active states
            [tabThematic, tabSearch, tabKeyword].forEach(t => t && t.classList.remove('active'));
            [thematicNav, searchNav, keywordNav, thematicView, searchView, keywordView].forEach(el => el && (el.style.display = 'none'));

            if (mode === 'thematic') {
                if (tabThematic) tabThematic.classList.add('active');
                if (thematicNav) thematicNav.style.display = 'flex';
                if (thematicView) thematicView.style.display = 'block';
            } else if (mode === 'search') {
                if (tabSearch) tabSearch.classList.add('active');
                if (searchNav) searchNav.style.display = 'block';
                if (searchView) searchView.style.display = 'block';

                // Render current search verse if not already rendered
                if (!document.getElementById('current-rendered-verse')) {
                    renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
                }
            } else if (mode === 'keyword') {
                if (tabKeyword) tabKeyword.classList.add('active');
                if (keywordNav) keywordNav.style.display = 'block';
                if (keywordView) keywordView.style.display = 'block';
                const kwInput = document.getElementById('keyword-search-input');
                if (kwInput && !kwInput.value.trim()) {
                    kwInput.focus();
                }
            }
        }"""

    if old_switch_main_mode in content:
        content = content.replace(old_switch_main_mode, new_switch_main_mode, 1)
        print("Updated switchMainMode successfully.")
    else:
        print("ERROR: old_switch_main_mode not found!")
        return

    # Update tanyaAI function and insert Smart Search, Keyword Search, and AI modal engine
    old_tanya_ai = """        function tanyaAI(button, event, uraianTitle) {
            if (event) event.stopPropagation(); // Mencegah flip card
            stopTTS();
            const card = button.closest('.flip-card-front');
            const surah = card.getAttribute('data-surah');
            const ayat = card.getAttribute('data-ayat');
            const langSelect = document.getElementById('tts-language');
            const selectedLang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[selectedLang] || LANG_CONFIG['id-ID'];

            const textEl = card.querySelector('.translation-text');
            const currentText = textEl ? textEl.textContent.trim() : decodeURIComponent(card.getAttribute('data-indo'));
            
            const groupCard = button.closest('.uraian-group-card');
            let titleToUse = uraianTitle;
            if (groupCard) {
                const titleEl = groupCard.querySelector('.group-title');
                if (titleEl && titleEl.textContent) {
                    titleToUse = titleEl.textContent.trim();
                }
            }

            const prompt = cfg.aiPrompt ? cfg.aiPrompt(surah, ayat, titleToUse, currentText) : `Jelaskan singkat QS. ${surah}:${ayat} terkait "${titleToUse}": "${currentText}"`;
            
            const url = `https://chatgpt.com/?q=${encodeURIComponent(prompt)}`;
            window.open(url, '_blank');
        }"""

    new_features_js = """        /* ==========================================================================
           TANYA AI: Zero-Hallucination Guided Quran Assistant Implementation
           ========================================================================== */
        let currentAIContext = {
            surahNum: 2,
            surahName: "Al-Baqarah",
            ayatNum: 255,
            arabText: "",
            indoText: "",
            tema: "Nama dan Sifat Allah",
            pokok: "Kekuasaan Allah",
            sub: "Ayat Kursi",
            uraian: "Keagungan Allah Meliputi Langit dan Bumi"
        };
        let currentAIMode = 'tadabbur';

        function tanyaAI(button, event, customTitle) {
            if (event) event.stopPropagation();
            stopTTS();

            let surahNum = 1, ayatNum = 1, surahName = "", arabText = "", indoText = "";
            let tema = elTema ? elTema.value : "";
            let pokok = elPokok ? elPokok.value : "";
            let sub = elSub ? elSub.value : "";
            let uraian = customTitle || "";

            // Check where the click came from:
            const flipFront = button ? button.closest('.flip-card-front') : null;
            const searchCard = button ? button.closest('.search-verse-card') : null;
            const keywordCard = button ? button.closest('.keyword-verse-card') : null;

            if (flipFront) {
                surahNum = parseInt(flipFront.getAttribute('data-surah')) || 1;
                ayatNum = parseInt(flipFront.getAttribute('data-ayat')) || 1;
                indoText = decodeURIComponent(flipFront.getAttribute('data-indo') || "");
                const textEl = flipFront.querySelector('.translation-text');
                if (textEl) indoText = textEl.textContent.trim();

                const flipBack = flipFront.parentElement ? flipFront.parentElement.querySelector('.flip-card-back') : null;
                if (flipBack) arabText = flipBack.textContent.trim();

                const groupCard = button.closest('.uraian-group-card');
                if (groupCard) {
                    const tEl = groupCard.querySelector('.group-title');
                    if (tEl) uraian = tEl.textContent.trim();
                }
            } else if (searchCard) {
                surahNum = currentSearchSurah;
                ayatNum = currentSearchAyat;
                const arabEl = searchCard.querySelector('.search-arabic-box');
                const transEl = searchCard.querySelector('.search-translation-box');
                if (arabEl) arabText = arabEl.textContent.trim();
                if (transEl) indoText = transEl.textContent.trim();

                const key = `${surahNum}:${ayatNum}`;
                if (verseThematicIndex[key] && verseThematicIndex[key].topics && verseThematicIndex[key].topics.length > 0) {
                    const top = verseThematicIndex[key].topics[0];
                    tema = top.tema;
                    pokok = top.pokok;
                    sub = top.sub;
                    uraian = top.uraian;
                }
            } else if (keywordCard) {
                surahNum = parseInt(keywordCard.getAttribute('data-surah')) || 1;
                ayatNum = parseInt(keywordCard.getAttribute('data-ayat')) || 1;
                const arabEl = keywordCard.querySelector('.keyword-arabic-box');
                const transEl = keywordCard.querySelector('.keyword-trans-box');
                if (arabEl) arabText = arabEl.textContent.trim();
                if (transEl) indoText = transEl.textContent.trim();

                const key = `${surahNum}:${ayatNum}`;
                if (verseThematicIndex[key] && verseThematicIndex[key].topics && verseThematicIndex[key].topics.length > 0) {
                    const top = verseThematicIndex[key].topics[0];
                    tema = top.tema;
                    pokok = top.pokok;
                    sub = top.sub;
                    uraian = top.uraian;
                }
            }

            const surahInfo = SURAH_LIST.find(s => s.no == surahNum);
            surahName = surahInfo ? surahInfo.name : `Surat ${surahNum}`;

            if (!arabText && verseThematicIndex[`${surahNum}:${ayatNum}`]) {
                arabText = verseThematicIndex[`${surahNum}:${ayatNum}`].arab;
            }
            if (!indoText && verseThematicIndex[`${surahNum}:${ayatNum}`]) {
                indoText = verseThematicIndex[`${surahNum}:${ayatNum}`].indo;
            }

            openTanyaAIModal({
                surahNum,
                surahName,
                ayatNum,
                arabText: arabText || "Teks Arab Al-Qur'an",
                indoText: indoText || "Terjemahan ayat Al-Qur'an",
                tema: tema || "Al-Qur'an Tematis",
                pokok: pokok || "Kandungan Al-Qur'an",
                sub: sub || "Tadabbur Ayat",
                uraian: uraian || `Kajian QS. ${surahName}: ${ayatNum}`
            });
        }

        function openTanyaAIModal(context) {
            currentAIContext = context;
            const modal = document.getElementById('modal-tanya-ai');
            if (!modal) return;

            // Render verse context
            const ctxEl = document.getElementById('ai-verse-context');
            if (ctxEl) {
                ctxEl.innerHTML = `
                    <div class="ai-context-verse-header">
                        <div class="ai-context-verse-title">QS. ${context.surahName} [${context.surahNum}] : Ayat ${context.ayatNum}</div>
                        <span class="thematic-match-badge" style="font-size: 0.78rem;">🏷️ ${context.tema || "Al-Qur'an Tematis"}</span>
                    </div>
                    <div class="ai-context-arabic">${context.arabText}</div>
                    <div class="ai-context-translation">"${context.indoText}"</div>
                    <div class="ai-context-thematic-tag">
                        📂 <strong>Topik Bahasan:</strong> ${context.uraian || context.sub || context.pokok}
                    </div>
                `;
            }

            // Set default mode
            setAIMode('tadabbur');

            // Render instant summary text
            const sumTextEl = document.getElementById('ai-instant-summary-text');
            if (sumTextEl) {
                sumTextEl.innerHTML = `
                    Ayat <strong>QS. ${context.surahName}: ${context.ayatNum}</strong> terklasifikasi secara shahih dalam tema <em>"${context.tema}"</em> pada bahasan <em>"${context.uraian}"</em>. Intisari ayat menegaskan petunjuk keimanan, keteladanan, serta hukum yang kokoh bagi umat beriman tanpa keraguan.
                `;
            }

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeTanyaAIModal() {
            const modal = document.getElementById('modal-tanya-ai');
            if (modal) modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        function closeTanyaAIModalOnBackdrop(e) {
            if (e.target && e.target.id === 'modal-tanya-ai') {
                closeTanyaAIModal();
            }
        }

        function setAIMode(mode) {
            currentAIMode = mode;
            const tabs = ['tadabbur', 'asbab', 'mufradat', 'custom'];
            tabs.forEach(t => {
                const btn = document.getElementById(`ai-tab-${t}`);
                if (btn) {
                    if (t === mode) btn.classList.add('active');
                    else btn.classList.remove('active');
                }
            });

            const customWrap = document.getElementById('ai-custom-input-wrap');
            if (customWrap) {
                customWrap.style.display = (mode === 'custom') ? 'block' : 'none';
                if (mode === 'custom') {
                    const inp = document.getElementById('ai-custom-question-input');
                    if (inp) inp.focus();
                }
            }

            updateAIPromptPreview();
        }

        function generateZeroHallucinationPrompt() {
            const ctx = currentAIContext;
            let specificInstruction = "";

            if (currentAIMode === 'tadabbur') {
                specificInstruction = `FOKUS KAJIAN: Tadabbur Tematis & Pelajaran Hidup\\nJelaskan secara mendalam hikmah, tadabbur, dan pelajaran praktis dari QS. ${ctx.surahName}:${ctx.ayatNum} dalam konteks tema '${ctx.tema}' dan uraian '${ctx.uraian}'. Sertakan aplikasi konkret dalam kehidupan seorang mukmin masa kini.`;
            } else if (currentAIMode === 'asbab') {
                specificInstruction = `FOKUS KAJIAN: Asbabun Nuzul Shahih\\nSebutkan sebab turunnya (Asbabun Nuzul) QS. ${ctx.surahName}:${ctx.ayatNum} HANYA jika bersumber dari riwayat yang shahih/hasan (sebutkan nama perawi haditsnya, misal Bukhari, Muslim, Ahmad, atau At-Tirmidzi). JIKA ayat ini tidak memiliki asbabun nuzul riwayat shahih khusus, nyatakan secara tegas bahwa ayat ini turun secara ibtida'i (permulaan) tanpa sebab riwayat khusus.`;
            } else if (currentAIMode === 'mufradat') {
                specificInstruction = `FOKUS KAJIAN: Analisis Kebahasaan & Mufradat (Kosakata)\\nBedah kosakata kunci dalam teks Arab QS. ${ctx.surahName}:${ctx.ayatNum} secara morfologis (akar kata/wazan/makna asal) dan terangkan keindahan balaghah (keagungan bahasa Al-Qur'an) yang terkandung di dalamnya.`;
            } else if (currentAIMode === 'custom') {
                const customInput = document.getElementById('ai-custom-question-input');
                const customQ = (customInput && customInput.value.trim()) ? customInput.value.trim() : `Jelaskan penjelasan komprehensif QS. ${ctx.surahName}:${ctx.ayatNum}`;
                specificInstruction = `PERTANYAAN PENGGUNA TENTANG AYAT INI:\\n"${customQ}"\\nJawab pertanyaan di atas dengan berlandaskan secara mutlak pada dalil nash ayat ini dan tafsir mu'tabar.`;
            }

            return `[SISTEM AL-QUR'AN BERINTEGRITAS ILMIAH TINGGI - PROTOKOL ZERO HALLUCINATION]
Anda adalah asisten Al-Qur'an terpercaya yang beroperasi dengan PRINSIP ZERO HALLUCINATION (Bebas Halusinasi & Nol Spekulasi).

DATA RUJUKAN RESMI:
- Surat & Ayat: QS. ${ctx.surahName} [Surat Ke-${ctx.surahNum}] : Ayat ${ctx.ayatNum}
- Teks Arab Asli: ${ctx.arabText}
- Terjemahan Resmi Kemenag RI: "${ctx.indoText}"
- Klasifikasi Al-Qur'an Tematis:
  * Tema Besar: ${ctx.tema}
  * Pokok Bahasan: ${ctx.pokok}
  * Sub Pokok Bahasan: ${ctx.sub}
  * Uraian Khusus: ${ctx.uraian}

ATURAN KETAT ZERO-HALLUCINATION:
1. RUJUKAN MUTLAK: Seluruh jawaban WAJIB bersumber secara ketat dari nash ayat di atas, hadits-hadits shahih/hasan mu'tabar (Shahih Bukhari, Shahih Muslim, Sunan Abu Dawud, Jami At-Tirmidzi), dan kitab tafsir mu'tabar (Tafsir Ibnu Katsir, Tafsir At-Thabari, Tafsir Al-Qurthubi, Tafsir Al-Jalalain, atau Tafsir Tematis Kemenag RI).
2. DILARANG MENGARANG: Dilarang keras mengarang riwayat, asbabun nuzul fiktif, sanad palsu, atau nomor ayat lain yang tidak pasti. Jika suatu riwayat tidak memiliki dalil shahih, nyatakan secara transparan: "Tidak terdapat riwayat shahih mengenai hal ini, Wallahu a'lam".
3. KONSISTENSI TEMATIK: Hubungkan penafsiran dengan konteks tema "${ctx.tema}" dan uraian khusus "${ctx.uraian}".
4. SISTEMATIKA JAWABAN:
   a. Makna Ringkas & Kosakata Kunci (Mufradat Arab)
   b. Asbabun Nuzul (Hanya jika riwayat shahih; jika tidak ada, tegaskan tidak ada sebab khusus)
   c. Intisari Petunjuk Hukum / Akidah / Akhlak
   d. Faidah Praktis & Tadabbur Tematis untuk Kehidupan
   e. Penutup: Wallahu A'lam Bish-Shawab

${specificInstruction}`;
        }

        function updateAIPromptPreview() {
            const previewBox = document.getElementById('ai-prompt-preview-box');
            if (previewBox) {
                previewBox.textContent = generateZeroHallucinationPrompt();
            }
        }

        function togglePromptPreview() {
            const previewBox = document.getElementById('ai-prompt-preview-box');
            if (previewBox) {
                previewBox.classList.toggle('expanded');
            }
        }

        function toggleInstantSummary() {
            const card = document.getElementById('ai-instant-summary-card');
            if (card) {
                card.style.display = (card.style.display === 'none' || !card.style.display) ? 'block' : 'none';
            }
        }

        function showAIToast(message) {
            const toast = document.getElementById('ai-toast');
            const msgEl = document.getElementById('ai-toast-message');
            if (!toast) return;
            if (msgEl) msgEl.textContent = message;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2800);
        }

        function copyAIPrompt() {
            const prompt = generateZeroHallucinationPrompt();
            navigator.clipboard.writeText(prompt).then(() => {
                showAIToast("Prompt Zero-Hallucination Berhasil Disalin!");
            }).catch(err => {
                console.error("Gagal menyalin prompt:", err);
            });
        }

        function openAIPlatform(platform) {
            const prompt = generateZeroHallucinationPrompt();
            const encoded = encodeURIComponent(prompt);

            if (platform === 'chatgpt') {
                window.open(`https://chatgpt.com/?q=${encoded}`, '_blank');
            } else if (platform === 'gemini') {
                // Copy to clipboard for easy pasting and open Gemini
                navigator.clipboard.writeText(prompt);
                showAIToast("Prompt disalin ke clipboard! Membuka Google Gemini...");
                setTimeout(() => {
                    window.open('https://gemini.google.com/app', '_blank');
                }, 400);
            } else if (platform === 'claude') {
                navigator.clipboard.writeText(prompt);
                showAIToast("Prompt disalin ke clipboard! Membuka Claude...");
                setTimeout(() => {
                    window.open('https://claude.ai/new', '_blank');
                }, 400);
            }
        }

        /* ==========================================================================
           FITUR 1: Smart Search Bar & Autocomplete (Cari Surat & Ayat)
           ========================================================================== */
        let smartSearchDebounceTimer = null;

        function normalizeSearchText(str) {
            return (str || '')
                .toLowerCase()
                .replace(/['’`-]/g, '')
                .replace(/\\s+/g, ' ')
                .trim();
        }

        function onSmartSearchInput(query) {
            const clearBtn = document.getElementById('btn-clear-smart-search');
            if (clearBtn) clearBtn.style.display = query.trim() ? 'flex' : 'none';

            clearTimeout(smartSearchDebounceTimer);
            smartSearchDebounceTimer = setTimeout(() => {
                processSmartSearchQuery(query);
            }, 180);
        }

        function clearSmartSearch() {
            const inp = document.getElementById('smart-surah-ayat-input');
            const dropdown = document.getElementById('smart-search-suggestions');
            const clearBtn = document.getElementById('btn-clear-smart-search');
            if (inp) {
                inp.value = '';
                inp.focus();
            }
            if (clearBtn) clearBtn.style.display = 'none';
            if (dropdown) dropdown.style.display = 'none';
        }

        function processSmartSearchQuery(query) {
            const dropdown = document.getElementById('smart-search-suggestions');
            if (!dropdown) return;

            const q = query.trim();
            if (!q) {
                dropdown.style.display = 'none';
                return;
            }

            // Patterns:
            // 1. "2:255" or "2 255" or "2-255"
            const numMatch = q.match(/^(\\d+)\\s*[:\\s-]\\s*(\\d+)$/);
            // 2. "Al-Baqarah 255" or "Baqarah:255"
            const nameNumMatch = q.match(/^([a-zA-Z'’`\\s-]+?)\\s*[:\\s-]\\s*(\\d+)$/);

            let suggestions = [];

            if (numMatch) {
                const sNum = parseInt(numMatch[1]);
                const aNum = parseInt(numMatch[2]);
                const sInfo = SURAH_LIST.find(s => s.no == sNum);
                if (sInfo && aNum >= 1 && aNum <= sInfo.ayat) {
                    suggestions.push({
                        surahNum: sNum,
                        surahName: sInfo.name,
                        ayatNum: aNum,
                        arab: sInfo.arab,
                        badge: `${sInfo.ayat} Ayat`,
                        label: `QS. ${sInfo.name} [${sNum}] : Ayat ${aNum}`
                    });
                }
            } else if (nameNumMatch) {
                const rawName = normalizeSearchText(nameNumMatch[1]);
                const aNum = parseInt(nameNumMatch[2]);
                const matchedSurahs = SURAH_LIST.filter(s => {
                    const norm = normalizeSearchText(s.name);
                    return norm.includes(rawName);
                });

                matchedSurahs.forEach(s => {
                    if (aNum >= 1 && aNum <= s.ayat) {
                        suggestions.push({
                            surahNum: s.no,
                            surahName: s.name,
                            ayatNum: aNum,
                            arab: s.arab,
                            badge: `Ayat ${aNum}`,
                            label: `QS. ${s.name} [${s.no}] : Ayat ${aNum}`
                        });
                    }
                });
            } else {
                // Just text or single number
                const rawQ = normalizeSearchText(q);
                const asNumber = parseInt(q);

                // Check surah matches
                SURAH_LIST.forEach(s => {
                    const norm = normalizeSearchText(s.name);
                    const matchName = norm.includes(rawQ);
                    const matchNo = (asNumber && s.no === asNumber);
                    if (matchName || matchNo) {
                        suggestions.push({
                            surahNum: s.no,
                            surahName: s.name,
                            ayatNum: 1,
                            arab: s.arab,
                            badge: `${s.ayat} Ayat`,
                            label: `QS. ${s.name} [${s.no}] — Ayat 1 s/d ${s.ayat}`
                        });
                        // Also suggest Ayat Kursi if Al-Baqarah
                        if (s.no === 2 && 'ayat kursi'.includes(rawQ)) {
                            suggestions.unshift({
                                surahNum: 2,
                                surahName: "Al-Baqarah",
                                ayatNum: 255,
                                arab: "البقرة",
                                badge: "Ayat Kursi",
                                label: `QS. Al-Baqarah [2] : Ayat 255 (Ayat Kursi)`
                            });
                        }
                    }
                });
            }

            if (suggestions.length === 0) {
                dropdown.innerHTML = `
                    <div style="padding: 0.85rem 1rem; color: #94a3b8; font-size: 0.9rem; text-align: center;">
                        Tidak ditemukan surat/ayat untuk "<strong>${escapeHtml(q)}</strong>".<br>
                        <span style="font-size: 0.8rem; color: #64748b;">Contoh format: <em>Al-Baqarah 255</em>, <em>36:82</em>, <em>Kahfi 10</em></span>
                    </div>
                `;
                dropdown.style.display = 'block';
                return;
            }

            let html = '';
            suggestions.slice(0, 8).forEach((item, idx) => {
                html += `
                    <div class="suggestion-item ${idx === 0 ? 'active' : ''}" onclick="selectSmartSuggestion(${item.surahNum}, ${item.ayatNum})">
                        <div class="suggestion-left">
                            <span class="suggestion-badge">${item.badge}</span>
                            <span>${escapeHtml(item.label)}</span>
                        </div>
                        <span class="suggestion-arabic">${item.arab}</span>
                    </div>
                `;
            });

            dropdown.innerHTML = html;
            dropdown.style.display = 'block';
        }

        function onSmartSearchKeydown(e) {
            const dropdown = document.getElementById('smart-search-suggestions');
            if (e.key === 'Enter') {
                e.preventDefault();
                if (dropdown && dropdown.style.display !== 'none') {
                    const firstItem = dropdown.querySelector('.suggestion-item');
                    if (firstItem) {
                        firstItem.click();
                        return;
                    }
                }
                const inp = document.getElementById('smart-surah-ayat-input');
                if (inp && inp.value.trim()) {
                    processSmartSearchQuery(inp.value.trim());
                    const firstItem = dropdown ? dropdown.querySelector('.suggestion-item') : null;
                    if (firstItem) firstItem.click();
                }
            } else if (e.key === 'Escape') {
                if (dropdown) dropdown.style.display = 'none';
            }
        }

        function selectSmartSuggestion(surahNum, ayatNum) {
            const dropdown = document.getElementById('smart-search-suggestions');
            const input = document.getElementById('smart-surah-ayat-input');
            if (dropdown) dropdown.style.display = 'none';

            currentSearchSurah = surahNum;
            currentSearchAyat = ayatNum;

            const selectSurah = document.getElementById('select-search-surah');
            const selectAyat = document.getElementById('select-search-ayat');

            if (selectSurah) selectSurah.value = surahNum;
            populateAyatDropdown(surahNum);
            if (selectAyat) selectAyat.value = ayatNum;
            updateStepperButtons();

            const surahInfo = SURAH_LIST.find(s => s.no == surahNum);
            if (input && surahInfo) {
                input.value = `${surahInfo.name} ${ayatNum}`;
            }

            renderSearchVerseResult(surahNum, ayatNum);
            scrollToSearchCard();
        }

        function selectQuickVerse(surahNum, ayatNum) {
            stopTTS();
            switchMainMode('search');
            selectSmartSuggestion(surahNum, ayatNum);
        }

        function scrollToSearchCard() {
            setTimeout(() => {
                const el = document.getElementById('search-content-area');
                if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }

        /* ==========================================================================
           FITUR 2: Pencarian Kata Kunci (Uraian & Teks Ayat)
           ========================================================================== */
        let keywordFilterMode = 'all'; // 'all', 'uraian', 'ayat'
        let keywordDebounceTimer = null;
        let lastSearchedKeyword = "";

        function onKeywordInput(val) {
            const clearBtn = document.getElementById('btn-clear-keyword-search');
            if (clearBtn) clearBtn.style.display = val.trim() ? 'flex' : 'none';

            clearTimeout(keywordDebounceTimer);
            if (!val.trim()) {
                clearKeywordSearch();
                return;
            }

            keywordDebounceTimer = setTimeout(() => {
                executeKeywordSearch();
            }, 300);
        }

        function clearKeywordSearch() {
            const input = document.getElementById('keyword-search-input');
            const clearBtn = document.getElementById('btn-clear-keyword-search');
            const area = document.getElementById('keyword-content-area');

            if (input) {
                input.value = '';
                input.focus();
            }
            if (clearBtn) clearBtn.style.display = 'none';
            lastSearchedKeyword = "";

            if (area) {
                area.innerHTML = `
                    <div class="empty-state">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem; display: block; color: var(--accent); opacity: 0.8;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        Ketik kata kunci di atas atau pilih salah satu kata populer untuk mencari uraian tematis dan ayat Al-Qur'an.
                    </div>
                `;
            }
        }

        function setKeywordFilter(filter) {
            keywordFilterMode = filter;
            ['all', 'uraian', 'ayat'].forEach(f => {
                const btn = document.getElementById(`filter-pill-${f}`);
                if (btn) {
                    if (f === filter) btn.classList.add('active');
                    else btn.classList.remove('active');
                }
            });

            if (lastSearchedKeyword) {
                executeKeywordSearch();
            }
        }

        function searchKeywordTag(tag) {
            switchMainMode('keyword');
            const input = document.getElementById('keyword-search-input');
            if (input) input.value = tag;
            const clearBtn = document.getElementById('btn-clear-keyword-search');
            if (clearBtn) clearBtn.style.display = 'flex';
            executeKeywordSearch();
        }

        function highlightKeyword(text, keyword) {
            if (!text || !keyword) return text || '';
            const safeKeyword = keyword.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
            const regex = new RegExp(`(${safeKeyword})`, 'gi');
            return text.replace(regex, '<mark class="search-highlight">$1</mark>');
        }

        function escapeHtml(str) {
            if (!str) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        function executeKeywordSearch() {
            stopTTS();
            const input = document.getElementById('keyword-search-input');
            const area = document.getElementById('keyword-content-area');
            if (!input || !area) return;

            const q = input.value.trim();
            if (!q || q.length < 2) {
                area.innerHTML = `<div class="empty-state">Silakan masukkan minimal 2 huruf untuk melakukan pencarian.</div>`;
                return;
            }

            lastSearchedKeyword = q;
            const qLower = q.toLowerCase();

            // 1. Search in all Uraian topics
            let matchedUraian = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'uraian') {
                allThematicUraianList.forEach(item => {
                    const uMatch = item.uraian.toLowerCase().includes(qLower);
                    const sMatch = item.sub.toLowerCase().includes(qLower);
                    const pMatch = item.pokok.toLowerCase().includes(qLower);
                    const tMatch = item.tema.toLowerCase().includes(qLower);

                    if (uMatch || sMatch || pMatch || tMatch) {
                        matchedUraian.push(item);
                    }
                });
            }

            // 2. Search in all Verses (Indonesian translation and Arabic)
            let matchedVerses = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'ayat') {
                allThematicVersesList.forEach(verse => {
                    const indoMatch = verse.indo && verse.indo.toLowerCase().includes(qLower);
                    const nameMatch = verse.surah_name && verse.surah_name.toLowerCase().includes(qLower);
                    const arabMatch = verse.arab && verse.arab.includes(q);

                    if (indoMatch || nameMatch || arabMatch) {
                        matchedVerses.push(verse);
                    }
                });
            }

            renderKeywordSearchResults(q, matchedUraian, matchedVerses);
        }

        function renderKeywordSearchResults(keyword, matchedUraian, matchedVerses) {
            const area = document.getElementById('keyword-content-area');
            if (!area) return;

            const totalUraian = matchedUraian.length;
            const totalVerses = matchedVerses.length;
            const grandTotal = totalUraian + totalVerses;

            if (grandTotal === 0) {
                area.innerHTML = `
                    <div class="empty-state" style="padding: 3rem 1.5rem;">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem; display: block; color: #ef4444; opacity: 0.8;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                        Tidak ditemukan hasil untuk kata kunci "<strong>${escapeHtml(keyword)}</strong>".
                        <div style="font-size: 0.88rem; color: #94a3b8; margin-top: 0.75rem;">
                            Saran: Periksa kembali ejaan kata, gunakan kata dasar (misal <em>sabar</em>, bukan <em>bersabarlah</em>), atau coba kata populer di atas.
                        </div>
                    </div>
                `;
                return;
            }

            let markup = `
                <div class="keyword-stats-banner">
                    <div class="keyword-stats-info">
                        <span>🔍 Hasil pencarian untuk: <strong>"${escapeHtml(keyword)}"</strong></span>
                    </div>
                    <div class="keyword-stats-badges">
                        ${keywordFilterMode !== 'ayat' ? `<span class="thematic-match-badge" style="background: rgba(20, 184, 166, 0.15); border-color: rgba(20, 184, 166, 0.4); color: #5eead4;">📝 ${totalUraian} Uraian Tematis</span>` : ''}
                        ${keywordFilterMode !== 'uraian' ? `<span class="thematic-match-badge" style="background: rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;">📖 ${totalVerses} Ayat Al-Qur'an</span>` : ''}
                    </div>
                </div>
            `;

            // SECTION 1: Uraian Tematis
            if (keywordFilterMode !== 'ayat' && totalUraian > 0) {
                markup += `
                    <div class="keyword-section-title">
                        <span>📝 Topik & Uraian Tematis Terkait</span>
                        <span class="badge">${totalUraian} Topik Ditemukan</span>
                    </div>
                    <div class="keyword-uraian-grid">
                `;

                matchedUraian.slice(0, 40).forEach(u => {
                    const highlightedUraian = highlightKeyword(escapeHtml(u.uraian), keyword);
                    const highlightedSub = highlightKeyword(escapeHtml(u.sub), keyword);
                    const highlightedPokok = highlightKeyword(escapeHtml(u.pokok), keyword);
                    const highlightedTema = highlightKeyword(escapeHtml(u.tema), keyword);

                    markup += `
                        <div class="keyword-uraian-card">
                            <div class="keyword-uraian-header">
                                <div class="keyword-uraian-title">${highlightedUraian}</div>
                                <span class="keyword-verse-count-badge">${u.verseCount} Ayat</span>
                            </div>
                            <div class="keyword-uraian-path">
                                <div>🏷️ <strong>Tema:</strong> ${highlightedTema}</div>
                                <div>📂 <strong>Pokok:</strong> ${highlightedPokok}</div>
                                <div>📑 <strong>Sub Pokok:</strong> ${highlightedSub}</div>
                            </div>
                            <button class="btn-jump-thematic" style="padding: 0.6rem 1.1rem; font-size: 0.88rem;" onclick="navigateToThematicTopic('${u.tema.replace(/'/g, "\\\\'")}', '${u.pokok.replace(/'/g, "\\\\'")}', '${u.sub.replace(/'/g, "\\\\'")}', '${u.uraian.replace(/'/g, "\\\\'")}', ${u.sampleVerses[0] ? u.sampleVerses[0].surah_num : 1}, ${u.sampleVerses[0] ? u.sampleVerses[0].ayat_num : 1})">
                                <span>Buka Topik Tematis Ini</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </button>
                        </div>
                    `;
                });

                if (totalUraian > 40) {
                    markup += `<div style="text-align: center; color: #94a3b8; font-size: 0.88rem; padding: 1rem;">Menampilkan 40 dari ${totalUraian} topik uraian. Spesifikasikan kata kunci Anda untuk hasil yang lebih sempit.</div>`;
                }

                markup += `</div>`;
            }

            // SECTION 2: Verses
            if (keywordFilterMode !== 'uraian' && totalVerses > 0) {
                markup += `
                    <div class="keyword-section-title" style="margin-top: 3.5rem;">
                        <span>📖 Ayat-Ayat Al-Qur'an Terkait</span>
                        <span class="badge">${totalVerses} Ayat Ditemukan</span>
                    </div>
                `;

                matchedVerses.slice(0, 50).forEach(v => {
                    const highlightedTrans = highlightKeyword(escapeHtml(v.indo), keyword);
                    const highlightedArab = highlightKeyword(v.arab, keyword);
                    const topic = (v.topics && v.topics.length > 0) ? v.topics[0] : null;

                    markup += `
                        <div class="keyword-verse-card" data-surah="${v.surah_num}" data-ayat="${v.ayat_num}">
                            <div class="keyword-verse-header">
                                <div class="keyword-verse-title">QS. ${v.surah_name} [${v.surah_num}] : Ayat ${v.ayat_num}</div>
                                <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
                                    ${topic ? `<span class="thematic-match-badge" style="font-size: 0.78rem;">🏷️ ${escapeHtml(topic.uraian)}</span>` : ''}
                                    ${v.audio ? `
                                    <audio controls style="height: 30px; border-radius: 999px;">
                                        <source src="${v.audio}" type="audio/mpeg">
                                    </audio>
                                    ` : ''}
                                </div>
                            </div>

                            <div class="search-arabic-box keyword-arabic-box" style="font-size: 2rem; margin-bottom: 1.25rem;">
                                ${highlightedArab} <span class="verse-end-sign">۝${toArabicDigits(v.ayat_num)}</span>
                            </div>

                            <div class="search-translation-box keyword-trans-box" style="margin-bottom: 1.25rem;">
                                ${highlightedTrans}
                            </div>

                            <div class="search-actions-bar">
                                <div class="search-action-btns-left">
                                    <button class="tts-button play-btn" data-text="${encodeURIComponent(v.indo)}" onclick="playTTS(this, event)" title="Dengarkan Terjemahan Suara">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>
                                        Dengarkan
                                    </button>
                                    <button class="tts-button ai-btn" style="color: #8b5cf6; border-color: #8b5cf6; background-color: rgba(139, 92, 246, 0.1);" onclick="tanyaAI(this, event, 'QS. ${v.surah_name}: ${v.ayat_num}')" title="Tanya AI Bebas Halusinasi">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                        Tanya AI
                                    </button>
                                    <button class="tts-button copy-btn" onclick="copyAyatText(this, event, '${v.surah_name}', ${v.surah_num}, ${v.ayat_num})" title="Salin Ayat">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                        Salin
                                    </button>
                                    <button class="tts-button" style="color: #25d366; border-color: rgba(37, 211, 102, 0.4); background-color: rgba(37, 211, 102, 0.1);" onclick="shareAyatWhatsApp('${v.surah_name}', ${v.surah_num}, ${v.ayat_num})" title="Bagikan ke WhatsApp">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                                        Bagikan
                                    </button>
                                </div>
                                <div class="search-action-btns-right">
                                    <button class="nav-action-btn secondary-btn" style="padding: 0.5rem 1rem; font-size: 0.88rem;" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)">
                                        🔍 Buka di Pencarian Ayat
                                    </button>
                                    ${topic ? `
                                    <button class="nav-action-btn next-btn" style="padding: 0.5rem 1rem; font-size: 0.88rem;" onclick="navigateToThematicTopic('${topic.tema.replace(/'/g, "\\\\'")}', '${topic.pokok.replace(/'/g, "\\\\'")}', '${topic.sub.replace(/'/g, "\\\\'")}', '${topic.uraian.replace(/'/g, "\\\\'")}', ${v.surah_num}, ${v.ayat_num})">
                                        Buka Tematik ➡️
                                    </button>
                                    ` : ''}
                                </div>
                            </div>
                        </div>
                    `;
                });

                if (totalVerses > 50) {
                    markup += `<div style="text-align: center; color: #94a3b8; font-size: 0.88rem; padding: 1rem;">Menampilkan 50 dari ${totalVerses} ayat yang memuat kata "${escapeHtml(keyword)}".</div>`;
                }
            }

            area.innerHTML = markup;
        }"""

    if old_tanya_ai in content:
        content = content.replace(old_tanya_ai, new_features_js, 1)
        print("Updated tanyaAI and injected Smart Search, Keyword Search, and Zero-Hallucination AI logic successfully.")
    else:
        print("ERROR: old_tanya_ai not found!")
        return

    # Write output
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: index.html updated successfully!")

if __name__ == '__main__':
    main()
