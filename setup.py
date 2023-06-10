from cx_Freeze import setup, Executable
import sys

# Specify the main script
mainScript = 'runner.py'

# Determine the base parameter based on the platform
if sys.platform == 'win32' or sys.platform == 'darwin':
    base = 'Win32GUI'
else:
    base = None

# Create an instance of the Executable class
executable = Executable(script=mainScript, base=base)

# Set additional options for the setup
options = {
    'build_exe': {
        'includes': ['pytube', 'pathlib', 'tkinter', 'PIL', 'os'],  # Include additional modules
        'include_files': ['Rv1.png']
    }
}

# Call the setup function
setup(
    name='YoutubeToMP4',
    version='1.0',
    description='Converts a Youtube URL to a downloaded MP4 file. This is downloaded to the users downloads folder.',
    executables=[executable],
    options=options,
)
