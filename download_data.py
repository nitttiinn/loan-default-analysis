import kagglehub # Kaggle's official Python Library
import shutil # Used for file and folder opertaion - Copying, Moving, Deleting
import os # Used for operating system operations - Creating folders, checking paths,listing files

#1. Download Dataset:
path = kagglehub.dataset_download("yasserh/loan-default-dataset")
print(f"Dataset downloaded to:{path}")

#2. Create data folder if not exists
os.makedirs("data",exist_ok=True)

#3. Copy to our project data Folder
shutil.copytree(path,"data",dirs_exist_ok=True)
print("Dataset ready in data folder!✅")