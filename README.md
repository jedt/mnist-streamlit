# mnist-streamlit
Pytorch training of MNIST dataset using a CNN model. Also included is a prediction web app using an html5 canvas in streamlit.
Check out the [training notebook](https://github.com/jedt/mnist-streamlit/blob/main/train_mnist.ipynb)

<img src="https://lh3.googleusercontent.com/u/0/drive-viewer/AEYmBYSLJIQkSjR0SqTfOHK8k2GlnboTtxsurrFlNanm6VPqgljQlHDDr3mm3jFPnSL_HGM9ufLXgzzixQxNm-OpiZrm9CTynQ=w2992-h1624" class="ndfHFb-c4YZDc-HiaYvf-RJLb9c" alt="Displaying screenshot-mnist.gif" aria-hidden="true" width="400">
Update: after changing the learning rate to lr=3e-4 it looks like it doesn't overfit anymore

# Installation
pip install -r requirements.txt

# Train the model
jupyter notebook train_mnist.ipynb

# Run the prediction app
streamlit run app.py


## Training accuracy results

```
Train Epoch: 50 	Average Loss: 0.007770	Accuracy: 99.76%
Train Epoch: 51 	Average Loss: 0.008432	Accuracy: 99.70%
Train Epoch: 52 	Average Loss: 0.008943	Accuracy: 99.69%
Train Epoch: 53 	Average Loss: 0.008401	Accuracy: 99.71%
Train Epoch: 54 	Average Loss: 0.007571	Accuracy: 99.75%
Train Epoch: 55 	Average Loss: 0.008158	Accuracy: 99.74%
Train Epoch: 56 	Average Loss: 0.006548	Accuracy: 99.80%
Train Epoch: 57 	Average Loss: 0.008153	Accuracy: 99.72%
Train Epoch: 58 	Average Loss: 0.007016	Accuracy: 99.75%
Train Epoch: 59 	Average Loss: 0.007247	Accuracy: 99.75%
Train Epoch: 60 	Average Loss: 0.007248	Accuracy: 99.75%
Train Epoch: 61 	Average Loss: 0.007317	Accuracy: 99.75%
Train Epoch: 62 	Average Loss: 0.007578	Accuracy: 99.75%
Train Epoch: 63 	Average Loss: 0.007143	Accuracy: 99.75%
Train Epoch: 64 	Average Loss: 0.006568	Accuracy: 99.77%
Train Epoch: 65 	Average Loss: 0.007010	Accuracy: 99.76%
Train Epoch: 66 	Average Loss: 0.006297	Accuracy: 99.79%
Train Epoch: 67 	Average Loss: 0.007704	Accuracy: 99.74%
Train Epoch: 68 	Average Loss: 0.006199	Accuracy: 99.78%
Train Epoch: 69 	Average Loss: 0.005578	Accuracy: 99.80%
Train Epoch: 70 	Average Loss: 0.006639	Accuracy: 99.76%
Train Epoch: 71 	Average Loss: 0.007192	Accuracy: 99.78%
Train Epoch: 72 	Average Loss: 0.005899	Accuracy: 99.81%
Train Epoch: 73 	Average Loss: 0.005731	Accuracy: 99.80%
Train Epoch: 74 	Average Loss: 0.005509	Accuracy: 99.80%
Train Epoch: 75 	Average Loss: 0.005899	Accuracy: 99.78%
Train Epoch: 76 	Average Loss: 0.005147	Accuracy: 99.82%
Train Epoch: 77 	Average Loss: 0.006637	Accuracy: 99.77%
Train Epoch: 78 	Average Loss: 0.005603	Accuracy: 99.81%
Train Epoch: 79 	Average Loss: 0.005901	Accuracy: 99.80%
Train Epoch: 80 	Average Loss: 0.005696	Accuracy: 99.80%
```
