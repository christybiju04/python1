def get_file_extension(filename):
    parts = filename.split('.')
    if len(parts) > 1:
        return parts[-1]
    else:
        return "No extension found"

try:
    filename = input("Input the Filename: ")
    extension = get_file_extension(filename)
    print(f"The extension of the file is: '{extension}'")
except Exception as e:
    print("An error occurred:", e)
