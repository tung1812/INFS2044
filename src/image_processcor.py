from abc import ABC, abstractmethod

class ImageProcessor(ABC):
    @abstractmethod
    def analyzeImage(self, image):
        pass

    @abstractmethod
    def identifyObjects(self):
        pass
