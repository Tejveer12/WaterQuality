{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0419823d",
   "metadata": {},
   "outputs": [],
   "source": [
    "%store -r my_pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9843aa03",
   "metadata": {},
   "outputs": [],
   "source": [
    "%store -r test_set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bf6fc86c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from joblib import load\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a6716e76",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=load(\"water_quality.joblib\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7ddc5d4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_features=test_set.drop(\"is_safe\",axis=1).copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f7d3d540",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_labels=test_set[\"is_safe\"].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ca1b453d",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_features=my_pipeline.fit_transform(test_features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4c42e210",
   "metadata": {},
   "outputs": [],
   "source": [
    "model_predicted=model.predict(test_features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "868afd53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.95625"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(model_predicted,test_labels)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
