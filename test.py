#!/home/andy/.my_projects/ImageToText/imgtxtvenv/bin/python3
# /usr/bin/tesseract
# from PySide2.QtUiTools import QUiLoader

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys

# zvImg = sys.argv[1]

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

#print(ocr_core(zvImg))

# =========================================== Qt UI ==========================================================
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "imgtxt.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    # -----------------------------------------
    def btn_clk():
        #print(window.lineEdit.text())

        window.plainTextEdit.setPlainText('')
        window.plainTextEdit.setPlainText('extracting text from '+window.lineEdit.text()+' . . . \n\n')
        zvTxt = ocr_core(window.lineEdit.text())
        window.plainTextEdit.setPlainText(zvTxt)

    window.pushButton.clicked.connect(btn_clk)
    # -----------------------------------------

    sys.exit(app.exec_())
