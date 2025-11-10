import unittest
from EmotionDetection.emotion_detection import emotion_detector

tests = [
    {'statement': 'I am glad this happened', 'want': 'joy'},
    {'statement': 'I am really mad about this', 'want': 'anger'},
    {'statement': 'I feel disgusted just hearing about this', 'want': 'disgust'},
    {'statement': 'I am so sad about this', 'want': 'sadness'},
    {'statement': 'I am really afraid that this will happen', 'want': 'fear'},
]

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        for t in tests:
            output = emotion_detector(t['statement'])
            self.assertEqual(output['dominant_emotion'], t['want'])


unittest.main()
