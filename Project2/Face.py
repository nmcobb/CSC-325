class Face:
    def __init__(self, label, xmin, ymin, xmax, ymax, mat):
        self.label = label
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.mat = mat
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def bounding_box(self):
        return (self.xmin, self.ymin, self.xmax, self.ymax)
