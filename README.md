# Slant

## Slant Frontend

We made our frontend with the Chrome Extensions API.

## Slant Backend

### Installing Dependencies

We've enumerated our Python dependencies in `requirements.txt`. To install them all, type `pip install -r requirements.txt`.

### Downloading Stuff

We used checkpoints for our Skip-Thoughts model that were pretrained on the [BookCorpus](http://yknzhu.wixsite.com/mbweb) dataset to understand English. You can download those by running `cd model; ./download_pretrained_models.sh`. Be warned: they are quite large (10 Gb or so).

Our sentiment analysis also requires a pre-trained English tokenizer. To download this, run `python` and type:
```
import nltk
nltk.download('punkt')
```

### Our Corpus
We classified political bias using the [Ideological Books Corpus](https://people.cs.umass.edu/~miyyer/ibc/). This dataset contains labeled data related to American politics. A political science expert labeled sentences from books and magazines written by authors with known ideologies. Specifically, it has 2025 liberal sentences, 1701 conservative sentences, and 600 neutral sentences. Each sentence was labeled by a political science expert.

### Running the App
To run dev Flask Server: `python -m flask run`

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

flask run --host=0.0.0.0


### Inspiration

We're thankful for a whole host of work that existed on this topic before we began the Slant project. Truly, we stand on the shoulders of giants. Specifically, we've based our work off of these two papers:

- Measuring Ideological Proportions in Political Speeches (https://www.cs.cmu.edu/~nasmith/papers/sim+acree+gross+smith.emnlp13.pdf)
- Skip-Thought Vectors (https://papers.nips.cc/paper/5950-skip-thought-vectors.pdf)

and these two Github repositories:

- this demo from Tensorflow https://github.com/tensorflow/models/tree/master/research/skip_thoughts
- this guy's project that used the skip-vector model for classification https://github.com/jz359/modemo