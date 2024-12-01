import os

folder_path = 'images/'  # Folder containing the images
output_file = 'README.md'  # Path to the README file

with open(output_file, 'w') as readme:
    readme.write("""# Viz Vault \n Repository of charting public datasets \n\n""")
    readme.write("## Image Gallery\n\n")
    for image_name in sorted(os.listdir(folder_path)):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(folder_path, image_name)
            readme.write(f"![{image_name}]({image_path})\n\n")
