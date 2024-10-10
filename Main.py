import os
import shutil

# Dictionary to categorize extensions into folders
EXTENSIONS = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.raw', '.ico'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.mpg', '.3gp', '.vob'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.opus', '.mid', '.xmf', '.ra'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.csv', '.json', '.ppt', '.pptx', '.odt', '.rtf', '.tex'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.xz', '.bz2', '.lz', '.z', '.ace'],
    'Spreadsheets': ['.xls', '.xlsx', '.ods', '.csv', '.tsv'],
    'Scripts': ['.py', '.js', '.html', '.css', '.php', '.java', '.rb', '.pl', '.sh', '.sql', '.bat'],
    'Executables': ['.exe', '.msi', '.bat', '.sh', '.apk'],
}


# Function to categorize the file based on its extension
def categorize_file(file_name):
    _, extension = os.path.splitext(file_name)  # Get the file extension
    for category, ext_list in EXTENSIONS.items():
        if extension.lower() in ext_list:
            return category
    return 'Others'  # Files that don't match the above categories


# Function to organize the files
def organize_files(folder_path):
    # Get the list of all files in the directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file_name in files:
        category = categorize_file(file_name)  # Determine the category

        # Create the destination folder based on the category
        dest_folder = os.path.join(folder_path, category)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Move the file to the appropriate folder
        shutil.move(os.path.join(folder_path, file_name), os.path.join(dest_folder, file_name))
        print(f"Moved {file_name} to {category} folder.")


if __name__ == '__main__':
    folder_path = input("Enter the folder path to organize: ")   #Here you have to write the  Folder path of the folder in which you want to organize the Data
    organize_files(folder_path)
