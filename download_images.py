import os

# main_dir = ["FolderA", "FolderB"]
# common_dir = ["SubFolder1", "SubFolder2", "SubFolder3"]

main_dir = 'sport_ball_images'
sub_dirs = ['basketball', 'soccer']

for sub_dir in sub_dirs:
    try:
        os.makedirs(os.path.join(main_dir, sub_dir))
    except OSError:
        pass
