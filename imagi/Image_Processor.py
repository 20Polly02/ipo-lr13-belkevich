from PIL import ImageFilter, Image

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def sharpen_filter(self):#Применить фильтр повышения резкости (SHARPEN)
        if self.image:
            self.image = self.image.filter(ImageFilter.SHARPEN) # применяем фильтр повышения резкости
            print("Фильтр повышения резкости применён.") # печатаем сообщение о применении фильтра
        else:
            print("Отсутствует изображение")

    def add_border(self, border_width=15, color="white"):#Добавление рамки вокруг изображения с шириной 15 пикселей
        if self.image:
            new_width = self.image.width + 2 * border_width
            new_height = self.image.height + 2 * border_width
            new_image = Image.new("RGB", (new_width, new_height), color)
            new_image.paste(self.image, (border_width, border_width))
            self.image = new_image
        else:
            print("Отсутствует изображение")

    def save_image(self, save_path):#сохранение изображения
        if self.image:
            self.image.save(save_path)
        else:
            print("Отсутствует изображение")