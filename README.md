
<p align="center">
  <img src="https://i.ibb.co/5vrHn2B/i-Seefood-Readme.jpg">
</p>

<p align="center">
   <a href="https://travis-ci.com/IbrahimNM/iSeefood" alt="Contributors">
        <img src="https://travis-ci.com/IbrahimNM/iSeefood.svg?token=Z7DztJ4D33ytYAbsRtvx&branch=master" /></a>
  <a href="https://www.codefactor.io/repository/github/ibrahimnm/iseefood" alt="Contributors">
        <img src="https://www.codefactor.io/repository/github/ibrahimnm/iseefood/badge" /></a>
  <a href="https://codecov.io/gh/IbrahimNM/iSeefood" alt="Contributors">
        <img src="https://codecov.io/gh/IbrahimNM/iSeefood/branch/master/graph/badge.svg?token=M1xWBWCg2X" /></a>
  <a href="https://requires.io/github/IbrahimNM/iSeefood/requirements/?branch=master"><img        src="https://requires.io/github/IbrahimNM/iSeefood/requirements.svg?branch=master" alt="Requirements Status" /></a>
  <a href="https://opensource.org/licenses/mit-license.php" alt="Contributors">
        <img src="https://badges.frapsoft.com/os/mit/mit.svg?v=103" /></a>
  <a href="https://www.tensorflow.org/" alt="Contributors">
        <img src="https://github.com/aleen42/badges/blob/master/src/tensorflow.svg" /></a>
  <a href="https://github.com/" alt="Contributors">
        <img src="https://aleen42.github.io/badges/src/github.svg" /></a>
</p>

## What Is This?
  A python module to recognize the existence of food in images by using a trained AI - [SFCA](https://github.com/wsu-wacs/seefood). 
## Dependencies
In order to run the iSeefood module, you need to install the following packages: 
  * Numpy
  * Tensorflow
  * Pillow 
  * Nose
  * Tornado
  
  - You can just run the following command to install all required packages:
  ```console
  $ pip install -r requirements.txt
  ```
  
## How To Use This
1. **Download**/ **Clone** the source code. 
   
   **NOTE**: Make sure that you download all the saved_model data file (≈217MB). 
  
    You can download the saved_model files:
      1. Manualy through the repository.
      2. By running the following command:

          ```console
          $ git lfs pull
          ```
2. **Copy** the *iSeefood* file to your project directory. 
    
    Recommended file structure:
    ```bash
    yourProject/
    ├── iSeefood/
    │   ├── README.md
    │   ├── SeefoodAI.py
    │   ├── __init__.py
    │   ├── samples/
    │   └── saved_model/
    │       ├── checkpoint
    │       ├── model_epoch5.ckpt.data-00000-of-00001
    │       ├── model_epoch5.ckpt.index
    │       └── model_epoch5.ckpt.meta
    ├── __init__.py
    └── main.py
    ```
    
3. **Import** the package to your *main.py* file.
    
    ```python
      from iSeefood import SeefoodAI
    ```
4. **Instantiate** a new object.
    ```python
      example = SeefoodAI()
    ```
5. **Pass** an image to be processed (**.png and .jpg only**).
    ```python
      example.process('../image.png')
    ```
6. **Get** the processing statistics.
    ```python
      statistics = example.getScore()
    ```
7. **Evaluate** the statistics.
    ```python
      result = example.getResult(statistics)
    ```
### Example
  ```python
  from iSeefood.SeefoodAI import SeefoodAI

  example = SeefoodAI()
  example.process("/iSeefood/samples/cookies.png")
  statistics = example.getScores()
  result = example.getResult(statistics)
  print  'Does the image contains food: ', result
  ```
  #### Output
  ```bash
  Does the image contains food:  True
  ```
## :warning: Notes
  * SeefoodAI class **assumes** that the saved_models are stored in the following path:
      ```bash
      yourWorkingDirectory/iSeefood/saved_model/
      ```
  * If you try to run your project from any location other than the project-base-path, the SeefoodAI class **will not** be able to find the *saved_model* directory!
  * If you would like to manipulate the directory location, you will have to update saved_models/ direcotry path inside the SeefoodAI.py class. The saved_models directory is specified inside the __setup() function. 
    
    ```python
    def __setup(self):
      ......
      saver = tf.train.import_meta_graph(
                'yourCustomizedPath/iSeefood/saved_model/model_epoch5.ckpt.meta')
      saver.restore(self.sess, tf.train.latest_checkpoint('yourCustomizedPath/iSeefood/saved_model/'))
      ......
    ```
## :page_with_curl: Documentation
|   Function    |   Parameter   | Return value | Description|
| ------------- | ------------- | ------------ | -----------
|   process()     | image_path:String  | True/False:bool     | **If** the image has been processed, then True. **Else**, then False. |
|  getScores()    | ---           |   numpy.ndarray     | Returns the data of the last processed image. 
|  getResult()  | scores:numpy.ndarray  | True/False:bool    | **If** there is food in the image, then True. **Else**, then False.

## Built With

* [Tensorflow](https://www.tensorflow.org/) - An E2E open source machine learning platform.
* [Pytest](https://docs.pytest.org/) - Testing framework.
* [Travis CI](https://travis-ci.com/) - CI service.
* [CodeFactor](https://www.codefactor.io) - Automated code review tool.
* [Codecov](https://codecov.io/) - A code coverage measurement tool   

## Versioning

We use [Github](https://github.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/IbrahimNM/BudgetOrganizer/tags).

## Authors

* **Ibrahim Almohaimeed** - [Github account](https://github.com/IbrahimNM)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments
* **Machine Learning and Complex Systems Lab at Wright State University** - [GitHub repo](https://github.com/wsu-wacs/seefood)
# 
