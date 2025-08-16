
PRIOR_LIST = [
    "cp1250",  # Windows encoding for Central and Eastern European languages
    "Latin1",
    "utf-16",  # Used for multilingual text, especially in Windows
    "ascii",  # Standard ASCII, used for basic Latin characters
    "cp1252",  # Windows encoding for Western European languages
    "isc_devanagari",  # ISCII encoding for Devanagari script (Hindi, Marathi, Sanskrit)
    "utf-16-le",       # UTF-16 Little Endian
    "utf-16-be",       # UTF-16 Big Endian
    "utf-8-sig",       # UTF-8 with BOM, often used in Windows
    "latin-1",         # Western European languages (ISO-8859-1), used in legacy systems
    "cp1251",          # Windows encoding for Cyrillic (Russian, Ukrainian, etc.)
    "cp1253",          # Windows encoding for Greek
    "cp1254",          # Windows encoding for Turkish
    "cp1255",          # Windows encoding for Hebrew
    "cp1256",          # Windows encoding for Arabic
    "cp1257",          # Windows encoding for Baltic languages
    "cp1258",          # Windows encoding for Vietnamese
    "shift_jis",       # Japanese encoding (used on Windows and legacy systems)
    "euc_jp",          # Japanese encoding, commonly used on Unix-based systems
    "iso2022_jp",      # Japanese encoding used in emails and text interchange
    "gb2312",          # Simplified Chinese encoding (legacy)
    "gbk",             # Extended Chinese encoding (simplified)
    "gb18030",         # Comprehensive Chinese encoding that covers all Unicode characters
    "big5",            # Traditional Chinese encoding (used in Taiwan and Hong Kong)
    "euc_kr",          # Korean encoding
    "iso2022_kr",      # Korean encoding, used in legacy systems and emails
    "mac_roman",       # Legacy encoding for Western European languages on macOS
    "iso8859_2",       # Central and Eastern European languages (ISO-8859-2)
    "iso8859_5",       # Cyrillic encoding (ISO-8859-5)
    "iso8859_6",       # Arabic encoding (ISO-8859-6)
    "iso8859_7",       # Greek encoding (ISO-8859-7)
    "iso8859_8",       # Hebrew encoding (ISO-8859-8)
    "isc_tamil",       # ISCII encoding for Tamil script
    "isc_bengali",     # ISCII encoding for Bengali script
    "isc_gujarati",    # ISCII encoding for Gujarati script
    "isc_kannada",     # ISCII encoding for Kannada script
    "isc_telugu",      # ISCII encoding for Telugu script
    "isc_urdu",        # ISCII encoding for Urdu script
    "isc_malayalam",   # ISCII encoding for Malayalam script
    "isc_oriy",        # ISCII encoding for Odia script
    "punycode",        # Encoding for Internationalized Domain Names (IDN)
    "rot_13",          # Encoding used for obfuscation (ROT13)
    "raw_unicode_escape",  # For decoding Unicode escape sequences directly
    "zlib",            # Not text encoding, but can be used for compressed data
]
MOST_COMMON = [    "utf-8",  # Most commonly used, universal encoding for all languages
]
