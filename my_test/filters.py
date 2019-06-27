from PIL import Image

def load_img(file_name):
    im = Image.open(file_name)
    return im

def show_img(img_object):
    img_object.show()

def save_img(img_object, save_name):
    img_object.save(save_name)

#should return a new Image object with filter applied
def obamicon(img_object):
    #create new empty list which you will put all new pixel values into (HINT: USE APPEND)
    new_list = []
    img = load_img(img_object)
    org_img_list = img.getdata()

    for tup in org_img_list:
        if sum(tup) > 182:
            new_list.append((0, 51, 76))
        elif sum(tup) > 182 and sum(tup) < 364:
            new_list.append((217, 26, 33))
        elif sum(tup) > 364 and sum(tup) < 546:
            new_list.append((217, 26, 33))
        
        else:
            new_list.append(tup)
    img.putdata(new_list)
    return img



        
        


    #use for loop to iterate through every single pixel
        #at every pixel, sum up the RGB values
        #use conditionals and boolean checks to determine which new color to change to
