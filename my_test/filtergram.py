import filters

def main():
    img = filters.load_img("obama.jpg")
    filters.obamicon(img)
    saved_img = img.save('newobama.jpg')
    print(saved_img.title)



#DONT TOUCH
if __name__ == "__main__":
    main()