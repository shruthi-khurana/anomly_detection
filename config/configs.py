from pathlib import Path
root_dir = Path(Path.cwd().parent)
augmented_image_dir = root_dir / 'images'/ 'augmented_images'
cropped_image_dir = root_dir / 'images' / 'cropped_images'
saved_model_dir = root_dir / 'saved_models' 
reports_dir = root_dir / 'reports'