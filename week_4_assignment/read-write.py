#!/usr/bin/env python3
"""
python script to read contents of input.txt
count the number of words in the file
convert all text to uppercase
write the processed text and the word count to a new file called output.txt
"""

def process_file(input_file, output_file):
    """
    Process the input file and write the results to the output file.
    
    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
            word_count = len(content.split())
            upper_content = content.upper()
        
        with open(output_file, 'w') as outfile:
            outfile.write(upper_content)
            outfile.write(f"\nWord Count: {word_count}\n")
        
        print(f"Processed {input_file} and wrote to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


process_file('input.txt', 'output.txt')