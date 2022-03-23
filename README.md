Working repository for Whodidit

added data from https://github.com/EdinburghNLP/csi-corpus

added metadata from wikpedia and IMDB

cleaned IMDB to just episode name, rank order, and rank

cleaned SRT files 
* removed music
* removed some special chars
* combined sub that span a sentence
* removed speaker and emphasis designators
* removed double quotes
* changed to tab-separated files

next steps 
1. redo some of the sub cleaning, remove double quotes, strip ()
2. joining labels for perp identification
3. fine-tune BERT on the subtitle dataset
4. train BERT on labeled set

Resources
1. https://www.tensorflow.org/text/tutorials/fine_tune_bert
2. testting body commit


