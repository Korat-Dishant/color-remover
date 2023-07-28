import tkinter as tk
# from tkinter import *
from PIL import Image ,  ImageTk

def main():
    img = Image.open('photo.png')
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    # rgba.save("transparent_image.png", "PNG")
    remove = removal_range({ 'color':[110, 232, 27] , 'range':[30,90,30] })
    print(remove)
    rgba.putdata(remove_color(datas,remove))
    # rgba.show()


    root = tk.Tk()

    root.title("Center Image with Sliders")
    # Load the image
    # image = Image.open('photo.png')
    image = rgba
    photo = ImageTk.PhotoImage(image)
    # Create a label to display the image
    label = tk.Label(root, image=photo)
    label.grid(row=0, column=0, padx=5, pady=5)
    # Create sliders below the image
    label2 = tk.Label(root, text="color removal range")
    label2.grid(row=1, column=0, padx=5, pady=2)

    slider1_value = tk.IntVar()
    slider2_value = tk.IntVar()
    slider3_value = tk.IntVar()
    slider1 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="red"  ,  variable=slider1_value)
    slider1.grid(row=2, column=0, padx=5, pady=5)
    slider2 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="green" ,  variable=slider2_value)
    slider2.grid(row=3, column=0, padx=5, pady=5)    
    slider3 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="green" ,  variable=slider3_value)
    slider3.grid(row=4, column=0, padx=5, pady=5)


    def get_slider_values():
        value1 = slider1_value.get()
        value2 = slider2_value.get()
        value3 = slider3_value.get()
        print("Slider 1 value:", value1)
        print("Slider 2 value:", value2)
        print("Slider 3 value:", value3)

    # Create a button to get slider values
    button = tk.Button(root, text="Get Slider Values", command=get_slider_values)
    button.grid(row=2, column=1, padx=5, pady=5)
    root.mainloop()

def removal_range(obj):
    rng = []
    for i in range(3):
        upper = obj['color'][i]+obj['range'][i]
        lower = obj['color'][i] - obj['range'][i]
        if lower < 0 :
            lower = 0
        if upper > 255 :
            upper = 255
        rng.append([ lower , upper ])
    return rng
    

def remove_color(datas,remove):  
    newData = []
    for item in datas:
        if item[0] in range(remove[0][0] , remove[0][1])  and item[1] in range(remove[1][0] , remove[1][1]) and item[2] in range(remove[2][0] , remove[2][1]):  
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # other colours remain unchanged
    
    return newData










if __name__ == "__main__" :
    main()