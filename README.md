# Yelp Star Predictor 

## Installation
Install manually

1.  Download supervised_training.py and runme.py from the GitHub repository
2.  Copy everything in the GitHub repository to a folder.

## Dependencies
These programs utilize json, sklearn, pandas and pickle
`pip install json pandas scikit-learn pickle-mixin` 
## Usage

1. To begin first train the supervised model on the yelp dataset that includes stars to create the serialized.pickle file.
 `python3 supervised_training.py`
 (skip to step 3 if you already have the serialized.pickle file and do not wish to re-train the model, you can also download the serialized.pickle file directly here https://drive.google.com/file/d/16Xqb9MNvqCR2oXVwZnys8r91FQJgYwfl/view?usp=sharing)
2. Wait for the random forest to finish running. 
3. Now, after you have created the pickle file in step 1 run the run.py model to predict the stars for your dataset without stars.
`python3 runme.py`
4. The program will output the star response in the terminal.

 ## License
Copyright 2020 Lee Leavitt

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


> Written with [StackEdit](https://stackedit.io/).
