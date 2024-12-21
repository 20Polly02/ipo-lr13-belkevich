from imagi.Image_Handler import ImageHandler 
from imagi.Image_Processor import ImageProcessor 
def main():
    
    image_path = input("Введите путь к изображению: ")
    
    ih = ImageHandler(image_path)
   
    ih.load_image()
    # преобразуем изображение в формат JPG и сохраняем его в файл output.jpg
    ih.jpg("file.jpg") 
    # поворачиваем изображение на 45 градусов
    ih.rotate_image(45)
    # создаем объект класса ImageProcessor, передав ему изображение из ImageHandler для дальнейшей обработки
    ip = ImageProcessor(ih.get_image())
    # применяем фильтр повышения резкости к изображению
    ip.sharpen_filter()
    # добавляем рамку шириной 15 пикселей вокруг изображения
    ip.add_border(15)
    # сохранение обработанного изображения
    ip.save_image("change_file.jpg")

if __name__ == "__main__":
    main() 