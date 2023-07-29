import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import copy


def on_canvas_click(event):
    global eyedropper
    if event == 'initialize':
        eyedropper = (255, 255, 255, 255)
    else:
        x, y = event.x, event.y
        eyedropper = image.getpixel((x, y))
    if event == 'initialize':
        eyedropper = (255, 255, 255, 255)
    else:
        x, y = event.x, event.y
        eyedropper = image.getpixel((x, y))
    print('eye dropper - ', eyedropper)
    update_image(slider1.get(), slider2.get(), slider3.get())


def open_image(*args):
    global file_path
    if len(args) != 0:
        print('welcome')
        file_path = args[0]
    else:
        file_path = filedialog.askopenfilename()
    # file_path = 'photo.png'
    if file_path:
        global image, photo
        image = Image.open(file_path)
        image = image.resize(new_dimensions(image))
        image = image.resize(new_dimensions(image))
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo


def new_dimensions(img):
    width = img.size[0]
    height = img.size[1]
    max_width, max_height = 600, 600
    ratio = min(max_width / width, max_height / height)
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    return new_width, new_height


def save_img():
    rgba = Image.open(file_path)
    # global new_img
    new_img = rgba.convert("RGBA")
    datas = new_img.getdata()
    remove = removal_range({'color': eyedropper, 'range': [
                           slider1.get(), slider2.get(), slider3.get()]})
    new_img.putdata(remove_color(datas, remove))
    file = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
    new_img.save(file)


def main():


    root = tk.Tk()
    root.title("Color remover")

    global image_label
    image_label = tk.Label(root)
    image_label.grid(row=0, column=0, padx=5, pady=5)
    open_image('welcome.png')
    global image_label
    image_label = tk.Label(root)
    image_label.grid(row=0, column=0, padx=5, pady=5)
    open_image('welcome.png')

    open_button = tk.Button(root, text="Open Image", command=open_image)
    open_button.grid(row=1, column=0, padx=5, pady=5)

    open_button = tk.Button(root, text="Save Image", command=save_img)
    open_button.grid(row=1, column=1, padx=5, pady=5)

    label2 = tk.Label(root, text="color removal range")
    label2.grid(row=2, column=0, padx=5, pady=2)

    slider1_value = tk.IntVar()
    slider2_value = tk.IntVar()
    slider3_value = tk.IntVar()
    global slider1
    slider1 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="red",  variable=slider1_value,
                       command=lambda value: update_image(slider1_value.get(), slider2_value.get(), slider3_value.get()))
    slider1.grid(row=3, column=0, padx=5, pady=5)
    global slider2
    slider2 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="green",  variable=slider2_value,
                       command=lambda value: update_image(slider1_value.get(), slider2_value.get(), slider3_value.get()))
    slider2.grid(row=4, column=0, padx=5, pady=5)
    global slider3
    slider3 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="blue",  variable=slider3_value,
                       command=lambda value: update_image(slider1_value.get(), slider2_value.get(), slider3_value.get()))
    slider3.grid(row=5, column=0, padx=5, pady=5)

    # Bind the mouse click event to the canvas
    on_canvas_click('initialize')
    on_canvas_click('initialize')
    image_label.bind("<Button-1>", on_canvas_click)

    root.mainloop()


def update_image(slider1_value, slider2_value, slider3_value):
    rgba = copy.deepcopy(image)
    # global new_img
    new_img = rgba.convert("RGBA")
    datas = new_img.getdata()
    remove = removal_range({'color': eyedropper, 'range': [
                           slider1_value, slider2_value, slider3_value]})
    print('remove range', remove)
    new_img.putdata(remove_color(datas, remove))

    new_photo = ImageTk.PhotoImage(new_img)

    # new_img.show()
    image_label.configure(image=new_photo)
    image_label.image = new_photo


def removal_range(obj):
    rng = []
    for i in range(3):
        upper = obj['color'][i]+obj['range'][i]
        lower = obj['color'][i] - obj['range'][i]
        if lower < 0:
            lower = 0
        if upper > 255:
            upper = 255
        rng.append([lower, upper])
    return rng


def remove_color(datas, remove):
    newData = []
    for item in datas:
        if item[0] in range(remove[0][0], remove[0][1]) and item[1] in range(remove[1][0], remove[1][1]) and item[2] in range(remove[2][0], remove[2][1]):
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # other colours remain unchanged

    return newData


if __name__ == "__main__":
    main()
