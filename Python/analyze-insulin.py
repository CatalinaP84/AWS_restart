# Read file content
with open("preproinsulin-seq.txt", "r") as input_file:
    content = input_file.readlines()
    
print(content)

# Delete the first and last lines
remaining_lines = content[1:-1]
print(remaining_lines)

# Remove the spaces and numbers placed at the begining of the line
processed_lines = []
for line in remaining_lines:
    line = line.replace(' ', '');
    line = line.replace('\n', '');
    processed_lines.append(line.strip('0123456789'))
    
print(processed_lines)

# Write the result in a new file
with open("preproinsulin-processed.txt", 'w') as output_file:
    output_file.writelines(processed_lines)
    
# Print the number of lowercase characters saved in the processed file
lowercase_count = 0
with open("preproinsulin-processed.txt", 'r') as file:
    content = file.read()
for char in content:
    if(char.islower()):
        lowercase_count += 1
        
print(lowercase_count)

# Function that reads the amino acids and write the amino acids corresponding to a given range in a specific file
def extract_and_save_amino_acids(input_file, start, end, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
# Extract the sequence of amino acids with corresponds to the given range
    amino_acids_sequence = content[start-1:end]
    
    with open(output_file, 'w') as file:
        file.write(amino_acids_sequence)
    
    print(f'The file named {output_file} contains {len(amino_acids_sequence)} characters')

extract_and_save_amino_acids("preproinsulin-processed.txt", 1, 24, "lsinsulin-seq-clean.txt")
extract_and_save_amino_acids("preproinsulin-processed.txt", 25, 54, "binsulin-seq-clean.txt")
extract_and_save_amino_acids("preproinsulin-processed.txt", 55, 89, "cinsulin-seq-clean.txt")
extract_and_save_amino_acids("preproinsulin-processed.txt", 90, 110, "ainsulin-seq-clean.txt")