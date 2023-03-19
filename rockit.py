import os
import collections
import codecs

# Define the input and output file names
input_folder = "data"
output_lv_tld = "lv-tld.txt"
output_rockyou_lv = "rockyou-lv.txt"

# Initialize the counter for passwords
passwords = collections.Counter()

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    # Open the file and ignore any encoding and unicode errors
    with codecs.open(os.path.join(input_folder, filename), 'r', encoding='utf-8', errors='ignore') as f:
        # Initialize the line counter for the file
        line_count = 0

        # Iterate over each line in the file
        for line in f:
            # Strip any whitespace from the line
            line = line.strip()

            # If the line contains the ":" character
            if ":" in line:
                # Split the line into email and password
                email, password = line.split(":", 1)

                # If the email ends with ".lv" TLD
                if email.endswith(".lv"):
                    # Add the line to the output file
                    with open(output_lv_tld, "a") as f_lv_tld:
                        f_lv_tld.write(line + "\n")

                    # Add the password to the counter
                    passwords.update([password])

            # Increment the line count for the file
            line_count += 1

        # Output the number of lines processed for the file
        print(f"{filename}: {line_count} lines processed")

# Open the output file for writing and write the sorted passwords
with open(output_rockyou_lv, "w") as f_rockyou_lv:
    for password, count in passwords.most_common():
        if count > 1:
            f_rockyou_lv.write(f"{password}\n") # can add {count} to retrieve times used
