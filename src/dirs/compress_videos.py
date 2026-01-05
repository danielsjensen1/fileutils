import subprocess
from os import fspath, getcwd, listdir, makedirs
from os.path import join, splitext


def convert_files_in_folder(input_folder=None, output_folder=None, suffix='.mkv'):
    input_folder = fspath(input_folder) if input_folder is not None else getcwd()
    output_folder = fspath(output_folder) if output_folder is not None else join(getcwd(), 'compressed')
    if input_folder == output_folder:
        raise ValueError(f"The input folder ({input_folder}) can't be the same as the output folder ({output_folder}).")
    makedirs(output_folder, exist_ok=True)
    # TODO: make the output folder if it doesn't exist
    files = listdir(input_folder)
    for file in files:
        if splitext(file)[1] == suffix:
            print(f"Processing {file}")
            input_file = join(input_folder, file)
            output_file = join(output_folder, file)
            cmd = ["HandBrakeCLI", "-i", input_file, '-o', output_file, "--preset-import-file", 'HQ 1080p30 Surround Normal.json', "--subtitle-lang-list", "eng" "--first-subtitle"]
            print(cmd)
            subprocess.run(cmd)

if __name__ == '__main__':
    convert_files_in_folder()