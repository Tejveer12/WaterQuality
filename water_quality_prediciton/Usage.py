{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9ccbaf16",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from joblib import load"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d497b128",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=load(\"water_quality.joblib\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1e905497",
   "metadata": {},
   "outputs": [],
   "source": [
    "input=np.array([[6.000e-02, 1.011e+01, 4.000e-02, 5.000e-01, 0.000e+00, 0.000e+00,\n",
    "       5.000e-02, 1.550e+00, 1.090e+00, 0.000e+00, 7.200e-01, 1.370e-01,\n",
    "       1.466e+01, 6.400e-01, 1.000e-03, 2.000e-02, 1.520e+00, 9.000e-02,\n",
    "       6.000e-02, 3.000e-02]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "aa087ecb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0], dtype=int64)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(input)"
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
