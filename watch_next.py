import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')
f = open("movies.txt", "r")
lines = f.readlines()
f.close()
d = dict(line.strip().split(":") for  line in lines)

# get first key
s = list(d)[0]

for k, v in d.items():
    d[k] = nlp(v)

def should_watch_next(watched_desc):
    watched = nlp(watched_desc)
    b = watched.similarity(d[s])
    for k, v in  d.items():
        if watched.similarity(v) > b:
            b = watched.similarity(v)
            title = k
    return title

hulk = " Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

x = nlp(hulk)
title = should_watch_next(x)

print(title)



