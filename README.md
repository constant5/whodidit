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
2. https://medium.com/@armandj.olivares/using-bert-for-classifying-documents-with-long-texts-5c3e7b04573d
    https://github.com/ArmandDS/bert_for_long_text/blob/master/final_bert_long_docs.ipynb
3. https://arxiv.org/abs/1910.10781
4. https://medium.com/@vishwajeetkumar_85368/news-classification-using-bidirectional-lstm-and-attention-a67aa803ca74
5. https://github.com/vishwajeetkr/Deep_News_Classifier
6. https://huggingface.co/flax-sentence-embeddings/all_datasets_v3_mpnet-base



