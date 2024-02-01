
import cv2 as cv
import numpy as np


class Image:
    def __init__(self, path=r'point2image/input/One-piece.png'):
        '''
        Initialize the Image object

        Parameters:
            path (str): the path to the input image file
        '''
        # Initialize padding parameters and load the image
        self.pad_h = None
        self.pad_w = None
        self.img = cv.imread(path, cv.IMREAD_GRAYSCALE)
        assert self.img is not None, "Couldn't read the image!"
        # Get image dimensions and perform initial resizing and Canny edge detection
        self.height, self.width = self.img.shape
        self.resize()
        # Canny algorithm
        self.img = cv.Canny(self.img, 100, 150)
        # Initialize monitor demensions
        self.monitor_w = 0
        self.monitor_h = 0

    def resize(self, max_edge: int = 500):
        '''
        Resize the image while maintaining its aspect ratio

        Parameters:
            max_edges (int): the maximun edge length after resizing 
        '''
        if self.width > self.height:
            new_width = max_edge
            new_height = int(new_width * self.height / self.width)
        else:
            new_height = max_edge
            new_width = int(new_height * self.width / self.height)
        # resize the image using cubic interpolation
        self.img = cv.resize(self.img, (new_width, new_height),
                             interpolation=cv.INTER_CUBIC)
        self.width = new_width
        self.height = new_height

    def padding(self, monitor_w: int, monitor_h: int):
        '''
        Apply adding to the image to fit within the specified monitor dimensions

        Parameters:
            monitor_w (int): width of the monitor or display area
            monitor_h (int): height of the monitor or display area
        '''
        self.pad_w = int(monitor_w - self.width) // 2
        self.pad_h = int(monitor_h - self.height) // 2
        # create a black image with the specified monitor dimensions
        tmp = np.zeros((monitor_h, monitor_w), dtype=np.uint8)
        # insert the resized image into the center of the black image
        tmp[self.pad_h: self.pad_h+self.height,
            self.pad_w:self.pad_w+self.width] = self.img
        # update the image attribute and set the monitor dimensions
        self.img = tmp
        self.monitor_h = monitor_h
        self.monitor_w = monitor_w
