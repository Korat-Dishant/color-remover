import tkinter as tk
# from tkinter import *
from PIL import Image ,  ImageTk
import copy 

def main():

    img = Image.open('photo.png')
    global rgba
    rgba = img.convert("RGBA")
    # datas = rgba.getdata()
    # # rgba.save("transparent_image.png", "PNG")
    # range_value1 = slider1_value.get()
    # range_value2 = slider2_value.get()
    # range_value3 = slider3_value.get()
    # remove = removal_range({ 'color':[110, 232, 27] , 'range':[range_value1,range_value2,range_value3] })
    # print(remove)
    # rgba.putdata(remove_color(datas,remove))
    # rgba.show()


    root = tk.Tk()

    root.title("Center Image with Sliders")
    # Load the image
    # image = Image.open('photo.png')
    image = rgba
    photo = ImageTk.PhotoImage(image)
    # Create a label to display the image
    global image_label  
    image_label = tk.Label(root, image=photo)
    image_label.grid(row=0, column=0, padx=5, pady=5)

    # Create sliders below the image
    label2 = tk.Label(root, text="color removal range")
    label2.grid(row=1, column=0, padx=5, pady=2)

    slider1_value = tk.IntVar()
    slider2_value = tk.IntVar()
    slider3_value = tk.IntVar()
    slider1 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="red"  ,  variable=slider1_value ,  command=lambda value: update_image(slider1_value.get(), slider2_value.get() , slider3_value.get()) )
    slider1.grid(row=2, column=0, padx=5, pady=5)
    slider2 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="green" ,  variable=slider2_value ,  command=lambda value: update_image(slider1_value.get(), slider2_value.get() , slider3_value.get()))
    slider2.grid(row=3, column=0, padx=5, pady=5)    
    slider3 = tk.Scale(root, from_=0, to=255, orient="horizontal", label="blue" ,  variable=slider3_value ,  command=lambda value: update_image(slider1_value.get(), slider2_value.get() , slider3_value.get()))
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


def update_image(slider1_value, slider2_value , slider3_value ):
    new_img = copy.deepcopy(rgba)
    datas = new_img.getdata()
    # new_img.save("transparent_image.png", "PNG")
    remove = removal_range({ 'color':[110, 232, 27] , 'range':[slider1_value,slider2_value,slider3_value] })
    print(remove)
    new_img.putdata(remove_color(datas,remove))
    photo = ImageTk.PhotoImage(new_img)
    # Update the image displayed in the label
    image_label.configure(image=photo)
    image_label.image = photo 



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