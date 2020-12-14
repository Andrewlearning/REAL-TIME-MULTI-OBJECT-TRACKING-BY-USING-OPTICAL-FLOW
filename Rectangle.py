import cv2
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


class Rectangle:
    border = 5

    def __init__(self, left, top, width=None, height=None):
        self.left = int(left)
        self.top = int(top)
        self.right = None
        self.bottom = None
        self.height = int(height)
        self.width = int(width)
        self.ready = False
        self.features = None


    def update_right_bottom(self):
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def set_lower_right(self, x, y):
        self.right = x
        self.bottom = y

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width


    def find_features(self, current):
        self.features = cv2.goodFeaturesToTrack(current[self.top:self.bottom, self.left:self.right],
                                                100, 0.15, 1)
        if self.features is not None:
            for feature in self.features:
                feature[0] += [self.left, self.top]

    def update_features(self, prev, current):
        # Have last frame, current frame and have feature points
        # Then we can get the new location of these feature points in this frame
        new_location, status, err = cv2.calcOpticalFlowPyrLK(prev, current, self.features, None, **lk_params)
        # status = 1 means last frames feature points was found in current frame
        good_new = new_location[status == 1]
        self.left, self.top = (good_new.min(axis=0) - Rectangle.border).astype(int)
        self.right, self.bottom = (good_new.max(axis=0) + Rectangle.border).astype(int)

        self.find_features(current)


    def is_ready(self):
        return self.ready


    def get_xywh(self):
        return [self.left, self.top, self.width, self.height]



