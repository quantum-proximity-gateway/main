import os
import re

TEMPLATE_PATH = 'README_TEMPLATE.md'
OUTPUT_PATH = 'README.md'

SUBMODULES = {
    'server': 'SERVER_README',
    'registration-site': 'REGISTRATION_README',
    'esp32-code': 'ESP32_README',
    'rpi-code': 'RPI_README',
    'desktop-app': 'DESKTOP_README'
}

def get_submodule_readme(submodule_path):
    readme_file = os.path.join(submodule_path, 'README.md')
    if os.path.isfile(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    else:
        return f"(No README found in {submodule_path}.)"

def transform_headings(markdown_text):
    lines = markdown_text.split('\n')
    heading_pattern = re.compile(r'^(#{1,6})(\s+)(.*)$')
    new_lines = []

    for line in lines:
        match = heading_pattern.match(line)
        if match:
            hashes, spacing, text = match.groups()
            if len(hashes) == 1:
                continue
            else:
                new_line = f"{hashes}##{spacing}{text}"
                new_lines.append(new_line)
        else:
            new_lines.append(line)

    return "\n".join(new_lines)

def main():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    for path, placeholder in SUBMODULES.items():
        readme_content = get_submodule_readme(path)

        readme_transformed = transform_headings(readme_content)

        pattern = r"{{" + re.escape(placeholder) + r"}}"
        content = re.sub(pattern, readme_transformed, content)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    main()
