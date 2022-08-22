import torch.nn as nn
import torch.optim as optim
import torch


class Transfer_classifier(nn.Module):
    def __init__(self,num_dim,num_class=3):
          #num_emb = total number of words/ emb_dim = number of dimension in each word/ num_word = total number of keyword in each article
        super(Transfer_classifier,self).__init__() 
        self.num_dim=num_dim
        self.num_class= num_class
        self.lin1 = nn.Linear(self.num_dim,64) #layer for title
        self.lin2 = nn.Linear(self.num_dim,64) #layer for article
        self.lin3 = nn.Linear(64*2,3) # combination layer
        self.flatten=nn.Flatten()
        self.dp =  nn.Dropout(0.3) #help with overfit (can apply in every layer, but let's try this first)
        self.sf = nn.Softmax(dim=1) # nn.Softmax(dim=1) # close layer , we need prob of each class to know which class the data are likely in.  (give probability)
        
    def forward(self,title_input,article_input):
        title_input = self.flatten(title_input)
        article_input = self.flatten(article_input)
        title_input = self.dp(title_input)
        article_input = self.dp(article_input)
        title_input = self.lin1(title_input)
        article_input = self.lin2(article_input)
        x = torch.cat([title_input,article_input],dim=1)
        x = torch.flatten(x,start_dim=1)
        x = self.lin3(x)
        x = self.sf(x)
        return x  # get the prob out