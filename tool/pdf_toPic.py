from multiprocessing import Pool
# 安装fitz需要安装PyMuPDF才能使用
import fitz
import os


class pdf_toPic():

    tmp =os.getcwd()
    export_file =os.getcwd()
    os.makedirs(export_file, exist_ok=True)
    pdf_dir =[]
    def pdf_to_jpg(self,name):
        # 拼接pdf的文件路径
        pwd_name = os.path.join(self.tmp, name)
        doc = fitz.open(pwd_name)
        # 将文件名同我们的保存路径拼接起来（保存图片的文件夹）
        dir_name = os.path.splitext(name)[0]
        pdf_name = os.path.join(self.export_file, dir_name)
        temp = 0
        # （保存图片的文件夹）不存咋则生成
        os.makedirs(pdf_name, exist_ok=True)
        for pg in range(doc.pageCount):
            page = doc[pg]
            temp += 1
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)

            pic_name = '{}.jpg'.format(temp)
            # 拼接生成pdf的文件路径
            pic_pwd = os.path.join(pdf_name, pic_name)
            pm.writePNG(pic_pwd)

    def main(self):
        try:
            pool = Pool(10)
            for i in self.pdf_dir:
                res = pool.apply_async(self.pdf_to_jpg, (i,))
            pool.close()
            pool.join()
            return 'success'
        except Exception as e:
            return e.args

