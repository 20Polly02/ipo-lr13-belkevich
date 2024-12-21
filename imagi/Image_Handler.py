from PIL import Image

class ImageHandler:
    def __init__(self, image):
        self.image = None
     
    def load_image(self):
        self.image = Image.open('image_4.png')
        return self.image
    def save_changed_image(self, new_name):
        if self.image:
            self.image.save(new_name) # сохраняем изображение по указанному пути
            print(f"Изображение сохранено в {new_name}.")
        else:
            print("Отсутствует изображение!")

    def jpg(self, new_name):#в формат jpg
        if self.image:
            self.image = self.image.convert("RGB")
            new_name = new_name.replace(".png", ".jpg") 
            self.image.save(new_name) 
        else:
            print("Отсутствует изображение")

    def rotate_image(self, angle=45):#поворот изображения на указанный угол
        if self.image:
            self.image = self.image.rotate(angle, expand=True)
        else:
            print("Отсутствует изображение")

    def get_image(self):#текущее изображение
        if self.image:
            return self.image
        else:
            print("Отсутствует изображение")
            return None