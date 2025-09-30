import os
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud

def toWordCloud(data, imageName):
    wordcloud = WordCloud().generate(data) #check
    wordcloud.to_file(imageName)

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
#d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()

# Generate a word cloud image
#wordcloud = WordCloud(width = 300, height = 500).generate(text)

# Display the generated image:
# the matplotlib way:

#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")

# lower max_font_size
#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()
#plt.savefig('foo.png', bbox_inches='tight')
# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
