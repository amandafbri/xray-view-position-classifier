# X-ray view position simple classifier

Despite the healthcare area having several discussions about interoperability and adoption of standards, there are still many databases not updated in this regard. In addition to this, there are the data and metadata integrity issues.

One of the topics related to this is about the metadata of very common exams, like X-rays. It is often observed, for example, that the position in which the X-ray was taken is recorded in an erroneous manner (examination with lateral view, but indicated as anteroposterior, etc.). One of the cases in which this can have a major impact is in the creation of machine learning models for predicting medical findings, since the patterns observed from different views can be quite distinct for the same finding.

With this in mind, the objective of this project was to create a classifier of radiographic view positions, using a reduced public dataset as a starting point and also using the simplest ML pipeline possible.

## Repository details

- Python 3.7.4 and 3.7.10
- In the `pipeline_before_deploy` folder there are the scripts and notebook for preparing the data, training and testing the model. In the GCP_Automl folder there is a simple script to prepare data to be used in AutoML Vision tool from Google Cloud Platform, but it was not used here.
- It was created a notebook with some explanations about the pipeline because this project was presented as a hands on. Check it out [here](https://www.youtube.com/c/Roadsec/videos).
- In the `xray_classifier_api` folder there are the Flask API created for serving the model.
- The public dataset "COVID-19 image data collection" used for this project is available in GitHub:

```
COVID-19 Image Data Collection: Prospective Predictions Are the Future
Joseph Paul Cohen and Paul Morrison and Lan Dao and Karsten Roth and Tim Q Duong and Marzyeh Ghassemi
arXiv:2006.11988, https://github.com/ieee8023/covid-chestxray-dataset, 2020
```
