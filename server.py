"""
This is the main emotion detection application written with
the Flask framework.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

def fmt_emotions(output: dict):
    """
    formats the emotion_detector output to an human readable format.
    """

    return (
        f"For the given statement, the system response is 'anger': {output['anger']}, "
        f"'disgust': {output['disgust']}, 'fear': {output['fear']}, "
        f"'joy': {output['joy']} and 'sadness': {output['sadness']}. "
        f"The dominant emotion is {output['dominant_emotion']}."
    )

@app.route("/emotionDetector")
def emot_detector():
    """
    Uses the query parameter `textToAnalyze`, then
    issues an emotion detection request and returns the
    output to the client.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return fmt_emotions(response)

@app.route("/")
def render_index_page():
    """
    renders the index page
    """

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
