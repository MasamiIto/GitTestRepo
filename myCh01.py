
# coding: shift_jis

import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot 	as plt
import numpy 				as np
import pandas 				as pd
import seaborn 				as sns
import chainer
import chainer.functions 	as F
import chainer.links 		as L
import pydot

from chainer 				import optimizers, training
from chainer.training 		import extensions
from chainer 				import Chain
from IPython.display 		import Image, display
from chainer 				import Variable

#####################################################################
LABEL_NAMES = [
    'T-shirt/top', 
    'Trouser',
    'Pullover',
    'Dress',
    'Coat', 
    'Sandal', 
    'Shirt',
    'Sneaker',
    'Bag', 
    'Ankle boot'
]

#####################################################################
def get_label_name(label):
    return LABEL_NAMES[label]

	
#####################################################################
class MLP2(Chain):

    # Initialization of layers
    def __init__(self):
        super(MLP2, self).__init__()
        with self.init_scope():
            self.l1 = L.Linear(784, 200)  # From 784-dimensional input to hidden unit with 200 nodes
            self.l2 = L.Linear(200, 10)  # From hidden unit with 200 nodes to output unit with 10 nodes  (10 classes)

    # Forward computation
    def forward(self, x):
        h1 = F.tanh(self.l1(x))  # Forward from x to h1 through activation with tanh function
        y = self.l2(h1)  # Forward from h1to y
        return y
## 3-layer multi-Layer Perceptron (MLP)
#####################################################################
class MLP3(Chain):

    def __init__(self):
        super(MLP3, self).__init__()
        with self.init_scope():
            self.l1=L.Linear(784, 200)
            self.l2=L.Linear(200, 200)   # Additional  layer
            self.l3=L.Linear(200, 10)

    def forward(self, x):
        h1 = F.tanh(self.l1(x))   # Hidden unit 1
        h2 = F.tanh(self.l2(h1)) # Hidden unit 2
        y = self.l3(h2)
        return y
## Let's create new Multi-Layer Perceptron (MLP)
#####################################################################
class MLPNew(Chain):

    def __init__(self):
        # Add more layers?
        super(MLPNew, self).__init__()
        with self.init_scope():
            self.l1=L.Linear(784, 200)  # Increase output node as (784, 300)?
            self.l2=L.Linear(200, 200)  # Increase nodes as (300, 300)?
            self.l3=L.Linear(200, 10)      # Increase nodes as (300, 10)?

    def forward(self, x):
        h1 = F.tanh(self.l1(x))        # Replace F.tanh with F.sigmoid  or F.relu ?
        h2 = F.tanh(self.l2(h1))        # Replace F.tanh with F.sigmoid  or F.relu ?
        y = self.l3(h2)
        return y
#####################################################################
class LeNet5(Chain):
    def __init__(self):
        super(LeNet5, self).__init__()
        with self.init_scope():
            self.conv1 = L.Convolution2D( in_channels=1 , out_channels=  6, ksize=5, stride=1, pad=0)
            self.conv2 = L.Convolution2D( in_channels=6 , out_channels= 16, ksize=5, stride=1, pad=0)
            self.conv3 = L.Convolution2D( in_channels=16, out_channels=120, ksize=4, stride=1, pad=0)
            self.fc4 = L.Linear(None, 84)
            self.fc5 = L.Linear(84, 10)s

    def forward(self, x):
        h = F.sigmoid       ( self.conv1( x.reshape((-1, 1, 28, 28))))
        h = F.max_pooling_2d( h             , ksize=2, stride=2)
        h = F.sigmoid       ( self.conv2(h) )
        h = F.max_pooling_2d( h             , ksize=2, stride=2)
        h = F.sigmoid       ( self.conv3(h) )
        h = F.sigmoid       ( self.fc4  (h) )
        return self.fc5(h)
#####################################################################
def  train_and_validate(  model, optimizer, train, validation, n_epoch, batchsize, device):
    
								# 2. Optimizerを設定する
    optimizer.setup(model)
 								# 3. DatasetからIteratorを作成する
    train_iter 		= chainer.iterators.SerialIterator( train     , batchsize)
    validation_iter = chainer.iterators.SerialIterator( validation, batchsize, repeat=False, shuffle=False)
 								# 4. Updater・Trainerを作成する
    updater 		= training.StandardUpdater( train_iter, optimizer, device=device)
    trainer 		= chainer.training.Trainer( updater , (n_epoch, 'epoch'), out='out')
								# 5. Trainerの機能を拡張する
    trainer.extend( extensions.LogReport  ())
    trainer.extend( extensions.Evaluator  ( validation_iter, model, device=device), name='val')
    trainer.extend( extensions.PrintReport( ['epoch'        , 'main/loss', 'main/accuracy', 'val/main/loss', 'val/main/accuracy', 'elapsed_time']))
    trainer.extend( extensions.PlotReport ( ['main/loss'    , 'val/main/loss'    ], x_key='epoch', file_name='loss.png'))
    trainer.extend( extensions.PlotReport ( ['main/accuracy', 'val/main/accuracy'], x_key='epoch', file_name='accuracy.png'))
    trainer.extend( extensions.dump_graph ( 'main/loss'))
								# 6. 訓練を開始する
    trainer.run()
	

#####################################################################
def show_graph():
    graph = pydot.graph_from_dot_file('out/cg.dot') # load from .dot file
    graph[0].write_png('graph.png')
    display(Image('graph.png', width=600, height=600))	

def show_loss_and_accuracy():
    display(Image(filename='out/loss.png'))
    display(Image(filename='out/accuracy.png'))

def show_examples(model, test, device):
    plt.figure(figsize=(12,50))
    if device >= 0:
        model.to_cpu()
    for i in range(45, 105):
        data, label = test[i]  # test data, label
        x = Variable(np.asarray([data]))  
        t = Variable(np.asarray([label]))  # labels
        y = model(x)
        prediction = y.data.argmax(axis=1)
        example = (data * 255).astype(np.int32).reshape(28, 28)
        plt.subplot(20, 5, i - 44)
        plt.imshow(example, cmap='gray')
        plt.title("No.{0}\nAnswer:{1}\nPredict:{2}".format(
            i,
            get_label_name(label),
            get_label_name(prediction[0])
        ))
        plt.axis("off")
    plt.tight_layout()
	
def show_test_performance(model, test, device, batchsize=256):
    if device >=0:
        model.to_gpu()
    test_iter = chainer.iterators.SerialIterator(
        test, batchsize, repeat=False, shuffle=False
    )
    test_evaluator = extensions.Evaluator(test_iter, model, device=device)
    results = test_evaluator()
    print('Test accuracy:', results['main/accuracy'])
	
#####################################################################
#  MAIN 
#####################################################################
for i in range(len(LABEL_NAMES)):
    print(i, ' is ', get_label_name(i))
from chainer.datasets.fashion_mnist import get_fashion_mnist

# データセットがダウンロード済みでなければ、ダウンロードも行う
train, test = get_fashion_mnist(withlabel=True, ndim=1)	

print('Size of train', len(train))
print('Size of test ', len(test ))

#print('------------------------- データ読み込み確認----------------' )
#x, t = test[0]
#print('Shape of x:' , x.shape			)
#print('label:'      , t					)
#print('label name:' , get_label_name(t)	)

#plt.plot(x)
#plt.show()

#plt.imshow(x.reshape(28, 28), cmap='gray')
#plt.show()

#for label_name in LABEL_NAMES:
#    this_data = ((x,t) for x, t in test if get_label_name(t) == label_name)  # generator
#    x, t = next(this_data)
#    print(t, label_name)
#    plt.imshow(x.reshape(28, 28), cmap='gray')
#    plt.show()

train, validation = chainer.datasets.split_dataset_random(train, 50000, seed=0)

device    =  -1  # specify gpu id. if device == -1, use cpu
n_epoch   =   5  # Only 5 epochs
batchsize = 256
model            = MLP2() 				# MLP2 model
#model 			 = MLP3()  # Use MLP3 instead of MLP2
classifier_model = L.Classifier(model)
optimizer 		 = optimizers.SGD()
train_and_validate( classifier_model, optimizer, train, validation, n_epoch, batchsize, device)

n_epoch = 10
batchsize = 256
model 			 = LeNet5()
classifier_model = L.Classifier(model)
optimizer 		 = optimizers.Adam()
train_and_validate( classifier_model, optimizer, train, validation, n_epoch, batchsize, device)


#show_graph()

show_loss_and_accuracy()

show_examples(	model, test, device)

show_test_performance(	classifier_model , test, device)



