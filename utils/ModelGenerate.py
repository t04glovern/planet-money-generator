from textgenrnn import textgenrnn
from json import loads
from sys import argv

file_path = argv[1]
num_sentence = argv[2]


def convertTranscript(file_path):
    #if we have an AWS transcript then convert it to just the transcript text
    f = open(file_path)
    filetext = f.read()
    filetext = loads(filetext)
    results = filetext['results']['transcripts']
    results = results[0]['transcript']
    newfilename = file_path[len(file_path):len(file_path.split[-1])]+'.txt'
    newfile = open(newfilename,'w')
    for line in results:
        newfile.write(line + '\n')
    newfile.close()
    return newfilename


if file_path.split(".")[-1]=='json':
    file_path = convertTranscript(file_path)

textgen = textgenrnn()
textgen.reset()

textgen.train_from_file(file_path, new_model=True, num_epochs=25, gen_epochs=100, context=False,
                        rnn_bidirectional=True, word_level=False, rnn_layers=4, dim_embeddings=900,
                        max_length=10)

f = open("FinalScript.txt", "w")
for _ in range(0, num_sentence):
    k = textgen.generate(n=1, prefix="KESTENBAUM", temperature=0.5, return_as_list=True)
    s = textgen.generate(n=1, prefix="SMITH", temperature=0.5, return_as_list=True)
    f.write(str(k[0]) + '\n')
    f.write(str(s[0]) + '\n')
    print(k)
    print(s)
f.close()


