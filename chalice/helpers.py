import re
import translitcodec
import markdown

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))

def generate_taglist(text):
    taglist = list(set(text.split(','))) # Converting to set and back removes duplicates
    result = [slugify(tag) for tag in taglist]
    return result

def markup(text):
    return markdown.markdown(text, extensions = ['codehilite', 'html_tidy'], output_format = 'html5')
