import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")

        self.process_button = tk.Button(self.root, text="Select an image", command=self.process_image)
        self.process_button.pack(pady=10)

        self.download_button = tk.Button(self.root, text="Download Image", command=self.download_image)
        self.download_button.pack(pady=5)

        self.display_label = tk.Label(self.root)
        self.display_label.pack(pady=5)

        self.threshold_img = None
        self.processed_image = None

    def process_image(self):
        filename = filedialog.askopenfilename(title="Select Image")
        if filename:
            img = cv2.imread(filename)

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, self.threshold_img = cv2.threshold(gray_img, 170, 255, cv2.THRESH_BINARY)

            # Convert processed image to PIL Image for display
            self.processed_image = Image.fromarray(self.threshold_img)

            # Display the processed image
            self.display_processed_image()

    def download_image(self):
        if self.processed_image:
            # Ask the user to select a directory to save the image
            directory = filedialog.askdirectory(title="Select Directory to Save Image")
            if directory:
                # Get the filename from the user
                filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialdir=directory)
                if filename:
                    self.processed_image.save(filename)

    def display_processed_image(self):
        # Convert PIL Image to Tkinter PhotoImage
        photo = ImageTk.PhotoImage(self.processed_image)

        # Display the image on a label
        self.display_label.configure(image=photo)
        self.display_label.image = photo  # Keep a reference to the image to prevent garbage collection

def main():
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
