from PIL import Image
import os


###多个图片合成一个pdf

class picToPDF():


    def jpg2pdf(self,jpgFile):
        global imglist
        path, fileName = jpgFile.rsplit('\\', 1)
        preName, postName = fileName.rsplit('.', 1)

        img = Image.open(jpgFile)
        imglist.append(img)
        # return img.save(path + "\\" + preName + '.pdf', "PDF", resolution=100.0, save_all=True)

    def jpg2pdfByPath(self,pathName,fileName,savePath):
        global imglist

        imglist = []
        imgfile = ''
        files = os.listdir(pathName)
        for f in files:
            if f.lower().find(".jpg") > 0:
                self.jpg2pdf(pathName + '\\' + f)
                imgfile = f

        imgMerge = imglist.pop(0)  # 取出第一个图片示例

        # imgMerge.save(pathName + r'\merge'+'.pdf', "PDF", resolution=100.0, save_all=True, append_images=imglist)
        imgMerge.save(os.path.join(savePath,fileName+'.pdf'), "PDF", resolution=100.0, save_all=True, append_images=imglist)
        # print("all images processed!")

    def pic_to_Pdf(self,pathDir,saveDir):
        try:
            listdir = os.listdir(pathDir)
            print(listdir)
            for x in listdir:
                test = os.path.isdir(r'C:\Users\92410\Desktop\test' + os.path.sep + x)
                if not test:
                    listdir.remove(x)
            print(listdir)
            for x in listdir:
                dir = os.path.join(pathDir, x)
                self.jpg2pdfByPath(pathName=dir, savePath=saveDir, fileName=os.path.basename(x))
            return "success"
        except Exception as e:
            return e

# if __name__ == '__main__':
#     a=pic_toPDF()
#     a.pic_to_Pdf(r'C:\Users\92410\Desktop\test',r'C:\Users\92410\Desktop\test')