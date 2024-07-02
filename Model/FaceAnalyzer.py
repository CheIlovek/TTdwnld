import face_recognition as fc
from PIL import Image
from Controller.LimitsChecker import LimitsChecker

class FaceAnalyzer:


    def analyze(self,image_paths):
        percents = []
        passed = True
        for path in image_paths:
            image = fc.load_image_file(path)
            face_per = self.calc_percent(image)
            percents.append(face_per)
            if face_per < LimitsChecker.FACE_PERCENT_REQ:
                passed = False
                break
    
        return passed


    def calc_percent(self,fc_img):
        # возвращает процент площади, которую занимает лицо на заданном изображении
        fc_loc = fc.face_locations(fc_img)
        pil_img = Image.fromarray(fc_img)
        width, height = pil_img.size
        if len(fc_loc) != 1:
            percent = 0
        else:
            percent = (((fc_loc[0][2] - fc_loc[0][0]) * (fc_loc[0][1] - fc_loc[0][3])) / (width * height)) * 100
        return percent