import qrcode,os,time
from PIL import Image


contents = r'http://qrcode.unionpay.com/12344/55555/999999'

def readIcon():
    icon = Image.open('qiuckpass-logo.png')
    icon_w, icon_h = icon.size
    return icon, icon_w, icon_h

class QR:

    def __init__(self,path = 'qiuckpass-logo.png'):
        self.icon = Image.open(path)
        self.icon_w,self.icon_h = self.icon.size

    def genarateQR(self,content):
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image().convert("RGBA")
        img_w, img_h = img.size
        w = int((img_w - self.icon_w) / 2)
        h = int((img_h - self.icon_h) / 2)

        img.paste(self.icon, (w, h), self.icon)
        return img

    def savePic(self,content,filename,dir=None):
        if None == dir:
            dir = os.path.join(os.path.dirname(__file__),time.strftime("%Y-%m-%d", time.localtime()))
        os.makedirs(dir,exist_ok=True)
        image = self.genarateQR(contents)
        ff = os.path.join(dir,filename+'.png')
        print (ff)
        image.save(ff)


if __name__=='__main__':
    q= QR()
    q.savePic('asfljaksdfjlasdkflasdfjlkasldfkadfjl','test')
