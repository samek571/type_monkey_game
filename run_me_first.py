import os
import subprocess
import sys

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}. Please try to install it manually.")

def main():
    for package in ['nltk', 'bcrypt', 'pygame', 'pyfiglet']:
        install(package)

    import nltk
    current_directory = os.path.dirname(os.path.abspath(__file__))
    nltk_data_directory = os.path.join(current_directory, 'nltk_data')
    nltk.data.path.append(nltk_data_directory)
    if not nltk.download('brown', download_dir=nltk_data_directory):
        print("Failed to download 'brown' dataset for nltk. Please try to download it manually.")

if __name__ == "__main__":
    main()
