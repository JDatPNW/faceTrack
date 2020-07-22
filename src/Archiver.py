import cv2
import re
import os


class Archiver:

    def saveImg(self, dir, num, scores, crop_img_re, d):
        if(d[0][0] >= 0 and d[0][1] >= 0 and d[1][0] >= 0 and d[1][1] >= 0):
            self.loc = os.path.dirname(os.path.abspath(
                __file__)) + "/../" + dir + "/" + str(num) + " - " + str(round(scores, 4)) + ".jpg"
            cv2.imwrite(self.loc, crop_img_re)

    def cropAndResize(self, frame, i, d):
        if(d[0][0] >= 0 and d[0][1] >= 0 and d[1][0] >= 0 and d[1][1] >= 0):
            self.crop_img = frame[d[0][1]:d[1][1],  d[0][0]: d[1][0]]
            self.crop_img_re = cv2.resize(self.crop_img, (48, 48))
            return self.crop_img_re

    def getCurrentDir(self, line, experiment, loader):
        url = line
        if(int(loader) == 0):
            folder = re.findall("[^\=]*$", url)
            folder = folder[0]
            dir = "results/" + experiment + folder
        else:
            dir = "results/" + experiment + "imageStream"
        return dir, url
