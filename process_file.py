def process_text_file(input_file, output_file):
    try:
        # Read the file and split words
        with open(input_file, 'r') as file:
            words = file.read().split()

        # Filter words longer than or equal to 8 characters and remove duplicates
        unique_words = set(word for word in words if len(word) >= 8)

        # Sort the words for better readability
        sorted_words = sorted(unique_words)

        # Write the processed words to the output file
        with open(output_file, 'w') as file:
            file.write('\n'.join(sorted_words))

        print(f"Processed file saved as: {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file = 'process_file_input.txt'  # Replace with your input file path
output_file = 'process_file_output.txt'  # Replace with your desired output file path
process_text_file(input_file, output_file)
