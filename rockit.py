import os
import glob
from collections import Counter, defaultdict
import time
from datetime import datetime
import re

# Start measuring processing time
start_time = time.time()

data_folder = "data/"
output_file_lv_tld = "lv-tld.txt"
output_file_rockyou_lv = "rockyou-lv.txt"
readme_file = "README.md"
md5_pattern = re.compile(r'^[a-f0-9]{32}$')

# Helpers
def normalize_email(email):
    parts = email.split('@')
    if len(parts) == 2:
        local_part, domain = parts
        normalized_local_part = local_part.split('+')[0]
        return normalized_local_part + '@' + domain
    else:
        return email

def file_size_mb(filepath):
    return os.path.getsize(filepath) / (1024 * 1024)

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        return 0

# Initialize variables for statistics
txt_files = glob.glob(os.path.join(data_folder, "*.txt"))
unique_email_passwords = set()
email_providers_counter = Counter()
total_file_size_mb = 0
file_line_count = {}
prev_lv_tld_count = count_lines_in_file(output_file_lv_tld)
prev_rockyou_lv_count = count_lines_in_file(output_file_rockyou_lv)

# Process each text file for email:password pairs and statistics
for txt_file in txt_files:
    total_file_size_mb += file_size_mb(txt_file)
    with open(txt_file, 'r', errors='ignore') as file:
        lines = file.readlines()
        file_line_count[txt_file] = len(lines)
        for line in lines:
            if ':' in line:
                email, password = line.strip().split(':', 1)
                if not md5_pattern.match(password) and email.endswith('.lv') and '@' in email and password.strip():
                    unique_email_passwords.add((email, password.strip()))
                    email_providers_counter[email.split('@')[1]] += 1

# Update the .lv TLD and rockyou-lv.txt files
password_occurrences = Counter(password for _, password in unique_email_passwords if password)
sorted_passwords_by_occurrence = sorted(password_occurrences.items(), key=lambda x: x[1], reverse=True)

with open(output_file_lv_tld, 'w') as lv_tld_file:
    for email, password in unique_email_passwords:
        lv_tld_file.write(f"{email}:{password}\n")

with open(output_file_rockyou_lv, 'w') as rockyou_lv_file:
    for password, count in sorted_passwords_by_occurrence:
        if count > 1 and password:
            rockyou_lv_file.write(f"{password}\n")

new_lv_tld_count = len(unique_email_passwords)
new_rockyou_lv_count = sum(count > 1 for count in password_occurrences.values())

# Processing time
end_time = time.time()
processing_time_seconds = end_time - start_time
processing_date = datetime.now().strftime('%Y-%m-%d')

# Prepare statistics in README.md
with open(readme_file, 'r') as file:
    readme_content = file.read()

contributing_start_index = readme_content.find('## Contributing')

statistics_markdown = f"""
## Statistics for {processing_date}

| Statistic | Value |
| --- | --- |
| Total lines processed | {sum(file_line_count.values())} |
| Total data processed (MB) | {total_file_size_mb:.2f} |
| Previous .lv TLD count | {prev_lv_tld_count} |
| New .lv TLD count | {new_lv_tld_count} |
| Difference in .lv TLD count | {new_lv_tld_count - prev_lv_tld_count} |
| Previous rockyou-lv count | {prev_rockyou_lv_count} |
| New rockyou-lv count | {new_rockyou_lv_count} |
| Difference in rockyou-lv count | {new_rockyou_lv_count - prev_rockyou_lv_count} |
| Processing time (seconds) | {processing_time_seconds:.2f} |

### Top 10 .lv TLD Email Providers

| Rank | Provider | Occurrences |
| --- | --- | --- |
"""

for rank, (provider, occurrences) in enumerate(email_providers_counter.most_common(10), 1):
    statistics_markdown += f"| {rank} | {provider} | {occurrences} |\n"

if contributing_start_index != -1:
    last_newline_before_contributing = readme_content.rfind('\n', 0, contributing_start_index)
    updated_readme_content = readme_content[:last_newline_before_contributing] + statistics_markdown + readme_content[last_newline_before_contributing:]
else:
    updated_readme_content = readme_content.strip() + statistics_markdown

with open(readme_file, 'w') as file:
    file.write(updated_readme_content)

# Output processed files and line counts
for txt_file, line_count in file_line_count.items():
    print(f"Processed file: {txt_file}, lines: {line_count}")