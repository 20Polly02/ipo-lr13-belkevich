from imagi.Image_Handler import ImageHandler 
from imagi.Image_Processor import ImageProcessor 
def main():
    
    image_path = input("Введите путь к изображению: ")
    ih = ImageHandler(image_path)
    ih.load_image()
    ih.jpg("file.jpg")  # преобразуем изображение в формат jpg
    ih.rotate_image(45)# поворачиваем изображение на 45 градусов
    ip = ImageProcessor(ih.get_image())
    ip.sharpen_filter()# применяем фильтр повышения резкости к изображению
    ip.add_border(15)   # добавляем рамку шириной 15 пикселей вокруг изображения
    ip.save_image("change_file.jpg") # сохранение обработанного изображения

if __name__ == "__main__": ip.save_image("change_file.jpg")
    main() 
