import os
import glob
from collections import Counter

data_folder = "data/"
output_file_lv_tld = "lv-tld.txt"
output_file_rockyou_lv = "rockyou-lv.txt"

# Read all .txt files in the data folder
txt_files = glob.glob(os.path.join(data_folder, "*.txt"))

unique_email_passwords = set()
file_line_count = {}

for txt_file in txt_files:
    with open(txt_file, 'r', errors='ignore') as f:
        line_count = 0
        for line in f:
            line_count += 1
            if ':' not in line:
                continue

            email, password = line.strip().split(':', 1)

            if email.endswith('.lv'):
                unique_email_passwords.add((email, password))

        file_line_count[txt_file] = line_count

# Save the .lv TLD email-password combinations to a file
with open(output_file_lv_tld, 'w') as f:
    for email, password in unique_email_passwords:
        f.write(f"{email}:{password}\n")

# Count password occurrences and sort by descending order
password_occurrences = Counter(password for email, password in unique_email_passwords)
sorted_password_occurrences = sorted(password_occurrences.items(), key=lambda x: x[1], reverse=True)

# Save the most common passwords to a file
with open(output_file_rockyou_lv, 'w') as f:
 for password, count in sorted_password_occurrences:
        if count > 1:
            f.write(f"{password}\n")

# Output processed files and line counts
for file, line_count in file_line_count.items():
    print(f"Processed file: {file}, lines: {line_count}")