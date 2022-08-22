import torch.nn as nn
import torch.optim as optim
import torch
from ..config.model_structure import Transfer_classifier

from transformers import AutoTokenizer
from transformers import AutoModel
import os

file_path="/app/model/transfer_model40.pth"
# print(os.getcwd()+file_path)

checkpoint=torch.load(os.getcwd()+file_path,map_location=torch.device('cpu'))

classifier = Transfer_classifier(768)
classifier.load_state_dict(checkpoint['model_state_dict'])
classifier.eval()

pretrain_checkpoint ="airesearch/wangchanberta-base-att-spm-uncased"
pretrain_tokenizer = AutoTokenizer.from_pretrained(pretrain_checkpoint)

pretrain_bert_model = AutoModel.from_pretrained(pretrain_checkpoint)

def predict(title,article):
	article_tokens = pretrain_tokenizer(article, return_tensors="pt",truncation=True,padding=True, max_length=128)
	title_tokens = pretrain_tokenizer(title, return_tensors="pt",truncation=True,padding=True, max_length=109)

	article_result = pretrain_bert_model(**article_tokens)
	title_result = pretrain_bert_model(**title_tokens)

	article_pool=article_result[1]
	title_pool=title_result[1]

	return classifier(article_pool,title_pool)