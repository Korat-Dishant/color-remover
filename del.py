import tkinter as tk
from PIL import Image, ImageTk


def change_image():
    # Replace this path with the path to your new image file
    x = Image.open('PP.png')
    print("called update")
    # Resize the image to fit the canvas
    new_image = x.resize(
        (canvas_width, canvas_height), Image.ANTIALIAS)
    # Update the canvas image
    canvas.image = ImageTk.PhotoImage(new_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image)


def main():
    # Set up the main window
    root = tk.Tk()
    root.title("Change Image on Button Click")

    # Set up the canvas
    global canvas_width, canvas_height, canvas
    canvas_width = 400
    canvas_height = 300
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Load the initial image on the canvas
    initial_image_path = "photo.png"
    initial_image = Image.open(initial_image_path)
    initial_image = initial_image.resize(
        (canvas_width, canvas_height), Image.ANTIALIAS)
    canvas.image = ImageTk.PhotoImage(initial_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image)

    # Set up the button to change the image
    change_button = tk.Button(root, text="Change Image", command=change_image)
    change_button.pack()

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
