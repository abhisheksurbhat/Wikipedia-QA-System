import torch
from torch.autograd import Variable
import torchtext.vocab as vocab
import json

q = open("question.json","r")
dataq = json.load(q)
q.close()
datalq = dataq['data']

c = open("context.json","r")
datac = json.load(c)
c.close()
datalc = datac['data']

torch.manual_seed(1)
class LstmPreprocessLayer(torch.nn.Module):
	def __init__(self,input_size,hidden_size,number_layer):
		super(LstmPreprocessLayer,self).__init__()

		self.input_size = input_size
		self.hidden_size = hidden_size
		self.number_layer = number_layer

		self.glove = vocab.GloVe(name='6B', dim=input_size)
		self.lstm = torch.nn.LSTM(self.input_size,self.hidden_size,self.number_layer)	#,bidirectional=True
		
	def forward(self,x,hidden):
		inputs = Variable(torch.zeros(len(x),self.input_size))
		for word in range(len(x)):
			try:
				inputs[word] = self.glove.vectors[self.glove.stoi[x[word]]]
			except:
				pass
		# print(inputs.unsqueeze(1).shape)
		# exit()
		
		output,hidden = self.lstm(inputs.unsqueeze(1),hidden)
		
		return output,hidden

	def initHidden(self):
		return Variable(torch.zeros(1,1,self.hidden_size)),Variable(torch.zeros(1,1,self.hidden_size))


class LstmAttentionLayer(torch.nn.Module):
	def __init__(self,input_size,hidden_size,number_layer,number_Q_tok):
		super(LstmAttentionLayer,self).__init__()

		self.input_size = input_size
		self.hidden_size = hidden_size
		self.number_layer = number_layer
		self.number_Q_tok = number_Q_tok

		self.tanh = torch.nn.Tanh()
		self.Wq = torch.nn.Linear(self.hidden_size,self.hidden_size)
		self.w = torch.nn.Linear(self.hidden_size,1)
		self.lstm = torch.nn.LSTM(self.hidden_size,self.hidden_size,self.number_layer)
		self.softmax = torch.nn.Softmax(dim =1)
	def forward(self,x,hidden,Hq):

		# temp = self.tanh(self.Wq(Hq) + ( self.lstm(x.view(1,-1).unsqueeze(1),hidden)[0].squeeze(1) ).repeat(self.number_Q_tok,1))
		temp = self.tanh(self.Wq(Hq))
		output,hidden = self.lstm(x.view(1,-1).unsqueeze(1),hidden)
		output = output.squeeze(1)
		output = output.repeat(self.number_Q_tok,1)
		output = output+temp
		# print(temp.shape)
		# alpha = self.softmax(self.w(temp))
		# exit()
		return output,hidden

	def initHidden(self):
		return Variable(torch.zeros(1,1,self.hidden_size)),Variable(torch.zeros(1,1,self.hidden_size))

class MatchLstmLayer(torch.nn.Module):
	def __init__(self,input_size,hidden_size,number_layer):
		super(MatchLstmLayer,self).__init__()

		self.input_size = input_size
		self.hidden_size = hidden_size
		self.number_layer = number_layer

		self.lstm = torch.nn.LSTM(self.input_size,self.hidden_size,self.number_layer)
		
	def forward(self,x,hidden):
		output,hidden = self.lstm(x.view(1,-1).unsqueeze(1),hidden)
		return output,hidden

	def initHidden(self):
		return Variable(torch.zeros(1,1,self.hidden_size)),Variable(torch.zeros(1,1,self.hidden_size))

p = LstmPreprocessLayer(100,150,1)

Hp,hidden = p(datalc[0]['0'],p.initHidden())
Hq,hidden = p(datalq[0]['Q'],p.initHidden())
# print(Hp[0].squeeze(1).shape,Hq.squeeze(1).shape)
# print(Hp,Hq)
Hp = Hp.squeeze(1)
Hq = Hq.squeeze(1)

a = LstmAttentionLayer(150,150,1,len(Hq))
hidden = a.initHidden()
h = Variable()
for i in Hp:
	output,hidden = a(i,hidden,Hq)
	try:
		h = torch.cat(h,output)
	except:
		h =  output
# print(h.shape)
alpha = a.softmax(a.w(h))
x = torch.mm(torch.t(Hq),alpha)
x = torch.t(x.repeat(1,len(Hp)))


Z = torch.cat((Hp,x),1)
print(Z.shape)	#141 X 300

m = MatchLstmLayer(300,150,1)
hidden = m.initHidden()
for i in Z:
	output,hidden = m(i,hidden)
	try:
		hr = torch.cat(h,output)
	except:
		hr =  output
print("output Tensor",hr.shape)

