import pytesseract
from PIL import Image
from pdf2image import convert_from_path


def get_img_string(img):
    # img = Image.open(img_path)
    result = pytesseract.image_to_string(img, lang='por')
    return result


def pdf_to_img(pdf_path):
    pages = convert_from_path(pdf_path)
    return pages


def get_text_from_pages(pages):
    text = ''
    for i in pages:
        page_separator = (
            '\n\n========================================\n' +
            '*** PÁGINA ' +
            str(pages.index(i) + 1) +
            '\n========================================\n\n'
        )
        page_text = get_img_string(i)
        text += page_separator + page_text
    return text


def tesseract_test_image():
    img_path = input('Caminho da imagem de entrada: ')
    imagem = Image.open(img_path)
    print('\n*** Lendo imagem: ' + img_path + '\n')
    print(get_img_string(imagem))


def tesseract_test_pdf():
    pdf_path = input('Caminho do pdf de entrada: ')
    print('\n*** Lendo documento: ' + pdf_path + '\n')
    print(get_text_from_pages(pdf_to_img(pdf_path)))

# "main"
tesseract_test_pdf()
