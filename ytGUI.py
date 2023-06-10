import tkinter as tk
import os
from pytube import exceptions
from ytToMp4 import downloadVideo
from tkinter import messagebox
from PIL import Image, ImageTk


class ytGUI():
    def __init__(self):
        self.window = tk.Tk()
        self.urlEntryLabel = None
        self.titleLabel = None
        self.downloadButton = None
        self.logoImage = None

    def main(self):
        # Create the main window
        self.window.title("YouTube to MP4 Downloader")

        # Set the background color
        self.window.configure(bg="light blue")

        # Calculating the PCs currently resolution.
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()

        # Calculating the size of the window.
        windowWidth = int(screenWidth*0.3)
        windowHeight = int(screenHeight*0.3)

        # Calculating the position of screen where the window is to be placed.
        screenPositionX = int(screenWidth*0.35)
        screenPositionY = int(screenPositionX*0.3)

        # Defining the window size
        self.window.geometry(f"{windowWidth}x{windowHeight}+{screenPositionX}+{screenPositionY}")
        
        # Make the window non-resizable
        self.window.resizable(False, False)

        # Create a label and an entry for the URL
        self.titleLabel = tk.Label(self.window, text="YouTube to MP4 Downloader")
        self.titleLabel.configure(font=("Arial", 28, "bold"), bg="light blue")
        self.titleLabel.pack()

        # Creating a subtitle label
        self.descLabel = tk.Label(self.window, text="YouTube URL:")
        self.descLabel.configure(font=("Arial", 14), bg="light blue")
        self.descLabel.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Creating a text box for the URL to be entered into
        self.urlEntryLabel = tk.Entry(self.window, width=60)
        self.urlEntryLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a button to run the script
        self.downloadButton = tk.Button(self.window, text="Download", command=self._runYtDownloadScript)
        self.downloadButton.configure(bg="#bbf4ae")
        self.downloadButton.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Resizing the images to a smaller aspect ratio
        logo = Image.open("Rv1.png")

        # Size of logo and Youtube Icon
        logoSize = int(windowWidth*(3/34))

        # Resize the images
        logo = logo.resize((logoSize, logoSize), Image.ANTIALIAS)

        # Create a Tkinter-compatible image object
        tkLogo = ImageTk.PhotoImage(logo)

        # Create a label to display the logo
        logoLabel = tk.Label(self.window, image=tkLogo)
        logoLabel.place(relx=0, rely=1, anchor=tk.SW)

        # Start the GUI main loop
        self.window.mainloop()

    def _runYtDownloadScript(self):
        try:
            # Obtain the entered Youtube URL
            url = self.urlEntryLabel.get()
            
            if url is None or url == "":
                raise ValueError

            # Run the Youtube to MP4 script.
            downloadVideo(url)

            # Display a popup message on successful completion
            messagebox.showinfo("Download Complete", "Download completed successfully!")
            self._closeWindow()

        # Show an error message if the script fails to grab data.
        except ValueError:
            messagebox.showerror("Error!", "Enter a URL.")
            self._closeWindow()
        
        except exceptions.RegexMatchError:
            messagebox.showerror("Error!", "Could not find that URL on YouTube. Please enter a valid URL.")
            self._closeWindow()
        
        except Exception:
            messagebox.showerror("Error!", "Unknown Error!")
            self._closeWindow()

    def _closeWindow(self):
        self.window.destroy()