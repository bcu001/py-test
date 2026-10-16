import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate",125);
engine.setProperty("volume", 1.0);
voices = engine.getProperty('voices');
engine.setProperty("voices", voices[0].id)

print("voices :", voices);

shakespear = '''Shall I compare thee to a summer’s day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date;
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimm'd;
And every fair from fair sometime declines,
By chance or nature’s changing course untrimm'd;
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow’st;
Nor shall death brag thou wander’st in his shade,
When in eternal lines to time thou grow’st:
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee.'''

engine.say(shakespear)
engine.runAndWait()
engine.stop();
engine.save_to_file(shakespear, 'shakespear.mp3');