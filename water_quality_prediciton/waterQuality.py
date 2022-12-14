{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "492c714e",
   "metadata": {},
   "source": [
    "## Importing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4e877e44",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from pandas.plotting import scatter_matrix\n",
    "from sklearn.model_selection import StratifiedShuffleSplit\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score,confusion_matrix\n",
    "from joblib import dump"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00c013f4",
   "metadata": {},
   "source": [
    "## Data preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ddf24c4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "water=pd.read_csv(\"waterQuality.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5370fc3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>aluminium</th>\n",
       "      <th>ammonia</th>\n",
       "      <th>arsenic</th>\n",
       "      <th>barium</th>\n",
       "      <th>cadmium</th>\n",
       "      <th>chloramine</th>\n",
       "      <th>chromium</th>\n",
       "      <th>copper</th>\n",
       "      <th>flouride</th>\n",
       "      <th>bacteria</th>\n",
       "      <th>...</th>\n",
       "      <th>lead</th>\n",
       "      <th>nitrates</th>\n",
       "      <th>nitrites</th>\n",
       "      <th>mercury</th>\n",
       "      <th>perchlorate</th>\n",
       "      <th>radium</th>\n",
       "      <th>selenium</th>\n",
       "      <th>silver</th>\n",
       "      <th>uranium</th>\n",
       "      <th>is_safe</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.65</td>\n",
       "      <td>9.08</td>\n",
       "      <td>0.04</td>\n",
       "      <td>2.85</td>\n",
       "      <td>0.007</td>\n",
       "      <td>0.35</td>\n",
       "      <td>0.83</td>\n",
       "      <td>0.17</td>\n",
       "      <td>0.05</td>\n",
       "      <td>0.20</td>\n",
       "      <td>...</td>\n",
       "      <td>0.054</td>\n",
       "      <td>16.08</td>\n",
       "      <td>1.13</td>\n",
       "      <td>0.007</td>\n",
       "      <td>37.75</td>\n",
       "      <td>6.78</td>\n",
       "      <td>0.08</td>\n",
       "      <td>0.34</td>\n",
       "      <td>0.02</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.32</td>\n",
       "      <td>21.16</td>\n",
       "      <td>0.01</td>\n",
       "      <td>3.31</td>\n",
       "      <td>0.002</td>\n",
       "      <td>5.28</td>\n",
       "      <td>0.68</td>\n",
       "      <td>0.66</td>\n",
       "      <td>0.90</td>\n",
       "      <td>0.65</td>\n",
       "      <td>...</td>\n",
       "      <td>0.100</td>\n",
       "      <td>2.01</td>\n",
       "      <td>1.93</td>\n",
       "      <td>0.003</td>\n",
       "      <td>32.26</td>\n",
       "      <td>3.21</td>\n",
       "      <td>0.08</td>\n",
       "      <td>0.27</td>\n",
       "      <td>0.05</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.01</td>\n",
       "      <td>14.02</td>\n",
       "      <td>0.04</td>\n",
       "      <td>0.58</td>\n",
       "      <td>0.008</td>\n",
       "      <td>4.24</td>\n",
       "      <td>0.53</td>\n",
       "      <td>0.02</td>\n",
       "      <td>0.99</td>\n",
       "      <td>0.05</td>\n",
       "      <td>...</td>\n",
       "      <td>0.078</td>\n",
       "      <td>14.16</td>\n",
       "      <td>1.11</td>\n",
       "      <td>0.006</td>\n",
       "      <td>50.28</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0.07</td>\n",
       "      <td>0.44</td>\n",
       "      <td>0.01</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.36</td>\n",
       "      <td>11.33</td>\n",
       "      <td>0.04</td>\n",
       "      <td>2.96</td>\n",
       "      <td>0.001</td>\n",
       "      <td>7.23</td>\n",
       "      <td>0.03</td>\n",
       "      <td>1.66</td>\n",
       "      <td>1.08</td>\n",
       "      <td>0.71</td>\n",
       "      <td>...</td>\n",
       "      <td>0.016</td>\n",
       "      <td>1.41</td>\n",
       "      <td>1.29</td>\n",
       "      <td>0.004</td>\n",
       "      <td>9.12</td>\n",
       "      <td>1.72</td>\n",
       "      <td>0.02</td>\n",
       "      <td>0.45</td>\n",
       "      <td>0.05</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.92</td>\n",
       "      <td>24.33</td>\n",
       "      <td>0.03</td>\n",
       "      <td>0.20</td>\n",
       "      <td>0.006</td>\n",
       "      <td>2.67</td>\n",
       "      <td>0.69</td>\n",
       "      <td>0.57</td>\n",
       "      <td>0.61</td>\n",
       "      <td>0.13</td>\n",
       "      <td>...</td>\n",
       "      <td>0.117</td>\n",
       "      <td>6.74</td>\n",
       "      <td>1.11</td>\n",
       "      <td>0.003</td>\n",
       "      <td>16.90</td>\n",
       "      <td>2.41</td>\n",
       "      <td>0.02</td>\n",
       "      <td>0.06</td>\n",
       "      <td>0.02</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows ?? 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   aluminium  ammonia  arsenic  barium  cadmium  chloramine  chromium  copper  \\\n",
       "0       1.65     9.08     0.04    2.85    0.007        0.35      0.83    0.17   \n",
       "1       2.32    21.16     0.01    3.31    0.002        5.28      0.68    0.66   \n",
       "2       1.01    14.02     0.04    0.58    0.008        4.24      0.53    0.02   \n",
       "3       1.36    11.33     0.04    2.96    0.001        7.23      0.03    1.66   \n",
       "4       0.92    24.33     0.03    0.20    0.006        2.67      0.69    0.57   \n",
       "\n",
       "   flouride  bacteria  ...   lead  nitrates  nitrites  mercury  perchlorate  \\\n",
       "0      0.05      0.20  ...  0.054     16.08      1.13    0.007        37.75   \n",
       "1      0.90      0.65  ...  0.100      2.01      1.93    0.003        32.26   \n",
       "2      0.99      0.05  ...  0.078     14.16      1.11    0.006        50.28   \n",
       "3      1.08      0.71  ...  0.016      1.41      1.29    0.004         9.12   \n",
       "4      0.61      0.13  ...  0.117      6.74      1.11    0.003        16.90   \n",
       "\n",
       "   radium  selenium  silver  uranium  is_safe  \n",
       "0    6.78      0.08    0.34     0.02        1  \n",
       "1    3.21      0.08    0.27     0.05        1  \n",
       "2    7.07      0.07    0.44     0.01        0  \n",
       "3    1.72      0.02    0.45     0.05        1  \n",
       "4    2.41      0.02    0.06     0.02        1  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "water.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7bec2fe4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 7996 entries, 0 to 7995\n",
      "Data columns (total 21 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   aluminium    7996 non-null   float64\n",
      " 1   ammonia      7996 non-null   float64\n",
      " 2   arsenic      7996 non-null   float64\n",
      " 3   barium       7996 non-null   float64\n",
      " 4   cadmium      7996 non-null   float64\n",
      " 5   chloramine   7996 non-null   float64\n",
      " 6   chromium     7996 non-null   float64\n",
      " 7   copper       7996 non-null   float64\n",
      " 8   flouride     7996 non-null   float64\n",
      " 9   bacteria     7996 non-null   float64\n",
      " 10  viruses      7996 non-null   float64\n",
      " 11  lead         7996 non-null   float64\n",
      " 12  nitrates     7996 non-null   float64\n",
      " 13  nitrites     7996 non-null   float64\n",
      " 14  mercury      7996 non-null   float64\n",
      " 15  perchlorate  7996 non-null   float64\n",
      " 16  radium       7996 non-null   float64\n",
      " 17  selenium     7996 non-null   float64\n",
      " 18  silver       7996 non-null   float64\n",
      " 19  uranium      7996 non-null   float64\n",
      " 20  is_safe      7996 non-null   int64  \n",
      "dtypes: float64(20), int64(1)\n",
      "memory usage: 1.3 MB\n"
     ]
    }
   ],
   "source": [
    "water.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "130e0143",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>aluminium</th>\n",
       "      <th>ammonia</th>\n",
       "      <th>arsenic</th>\n",
       "      <th>barium</th>\n",
       "      <th>cadmium</th>\n",
       "      <th>chloramine</th>\n",
       "      <th>chromium</th>\n",
       "      <th>copper</th>\n",
       "      <th>flouride</th>\n",
       "      <th>bacteria</th>\n",
       "      <th>...</th>\n",
       "      <th>lead</th>\n",
       "      <th>nitrates</th>\n",
       "      <th>nitrites</th>\n",
       "      <th>mercury</th>\n",
       "      <th>perchlorate</th>\n",
       "      <th>radium</th>\n",
       "      <th>selenium</th>\n",
       "      <th>silver</th>\n",
       "      <th>uranium</th>\n",
       "      <th>is_safe</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "      <td>7996.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.666396</td>\n",
       "      <td>14.278212</td>\n",
       "      <td>0.161477</td>\n",
       "      <td>1.567928</td>\n",
       "      <td>0.042803</td>\n",
       "      <td>2.177589</td>\n",
       "      <td>0.247300</td>\n",
       "      <td>0.805940</td>\n",
       "      <td>0.771646</td>\n",
       "      <td>0.319714</td>\n",
       "      <td>...</td>\n",
       "      <td>0.099431</td>\n",
       "      <td>9.819250</td>\n",
       "      <td>1.329846</td>\n",
       "      <td>0.005193</td>\n",
       "      <td>16.465266</td>\n",
       "      <td>2.920106</td>\n",
       "      <td>0.049684</td>\n",
       "      <td>0.147811</td>\n",
       "      <td>0.044672</td>\n",
       "      <td>0.114057</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.265323</td>\n",
       "      <td>8.878930</td>\n",
       "      <td>0.252632</td>\n",
       "      <td>1.216227</td>\n",
       "      <td>0.036049</td>\n",
       "      <td>2.567210</td>\n",
       "      <td>0.270663</td>\n",
       "      <td>0.653595</td>\n",
       "      <td>0.435423</td>\n",
       "      <td>0.329497</td>\n",
       "      <td>...</td>\n",
       "      <td>0.058169</td>\n",
       "      <td>5.541977</td>\n",
       "      <td>0.573271</td>\n",
       "      <td>0.002967</td>\n",
       "      <td>17.688827</td>\n",
       "      <td>2.322805</td>\n",
       "      <td>0.028773</td>\n",
       "      <td>0.143569</td>\n",
       "      <td>0.026906</td>\n",
       "      <td>0.317900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>-0.080000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.040000</td>\n",
       "      <td>6.577500</td>\n",
       "      <td>0.030000</td>\n",
       "      <td>0.560000</td>\n",
       "      <td>0.008000</td>\n",
       "      <td>0.100000</td>\n",
       "      <td>0.050000</td>\n",
       "      <td>0.090000</td>\n",
       "      <td>0.407500</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.048000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.003000</td>\n",
       "      <td>2.170000</td>\n",
       "      <td>0.820000</td>\n",
       "      <td>0.020000</td>\n",
       "      <td>0.040000</td>\n",
       "      <td>0.020000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.070000</td>\n",
       "      <td>14.130000</td>\n",
       "      <td>0.050000</td>\n",
       "      <td>1.190000</td>\n",
       "      <td>0.040000</td>\n",
       "      <td>0.530000</td>\n",
       "      <td>0.090000</td>\n",
       "      <td>0.750000</td>\n",
       "      <td>0.770000</td>\n",
       "      <td>0.220000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.102000</td>\n",
       "      <td>9.930000</td>\n",
       "      <td>1.420000</td>\n",
       "      <td>0.005000</td>\n",
       "      <td>7.745000</td>\n",
       "      <td>2.410000</td>\n",
       "      <td>0.050000</td>\n",
       "      <td>0.080000</td>\n",
       "      <td>0.050000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.280000</td>\n",
       "      <td>22.132500</td>\n",
       "      <td>0.100000</td>\n",
       "      <td>2.482500</td>\n",
       "      <td>0.070000</td>\n",
       "      <td>4.240000</td>\n",
       "      <td>0.440000</td>\n",
       "      <td>1.390000</td>\n",
       "      <td>1.160000</td>\n",
       "      <td>0.610000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.151000</td>\n",
       "      <td>14.610000</td>\n",
       "      <td>1.760000</td>\n",
       "      <td>0.008000</td>\n",
       "      <td>29.487500</td>\n",
       "      <td>4.670000</td>\n",
       "      <td>0.070000</td>\n",
       "      <td>0.240000</td>\n",
       "      <td>0.070000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.050000</td>\n",
       "      <td>29.840000</td>\n",
       "      <td>1.050000</td>\n",
       "      <td>4.940000</td>\n",
       "      <td>0.130000</td>\n",
       "      <td>8.680000</td>\n",
       "      <td>0.900000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.200000</td>\n",
       "      <td>19.830000</td>\n",
       "      <td>2.930000</td>\n",
       "      <td>0.010000</td>\n",
       "      <td>60.010000</td>\n",
       "      <td>7.990000</td>\n",
       "      <td>0.100000</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>0.090000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8 rows ?? 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         aluminium      ammonia      arsenic       barium      cadmium  \\\n",
       "count  7996.000000  7996.000000  7996.000000  7996.000000  7996.000000   \n",
       "mean      0.666396    14.278212     0.161477     1.567928     0.042803   \n",
       "std       1.265323     8.878930     0.252632     1.216227     0.036049   \n",
       "min       0.000000    -0.080000     0.000000     0.000000     0.000000   \n",
       "25%       0.040000     6.577500     0.030000     0.560000     0.008000   \n",
       "50%       0.070000    14.130000     0.050000     1.190000     0.040000   \n",
       "75%       0.280000    22.132500     0.100000     2.482500     0.070000   \n",
       "max       5.050000    29.840000     1.050000     4.940000     0.130000   \n",
       "\n",
       "        chloramine     chromium       copper     flouride     bacteria  ...  \\\n",
       "count  7996.000000  7996.000000  7996.000000  7996.000000  7996.000000  ...   \n",
       "mean      2.177589     0.247300     0.805940     0.771646     0.319714  ...   \n",
       "std       2.567210     0.270663     0.653595     0.435423     0.329497  ...   \n",
       "min       0.000000     0.000000     0.000000     0.000000     0.000000  ...   \n",
       "25%       0.100000     0.050000     0.090000     0.407500     0.000000  ...   \n",
       "50%       0.530000     0.090000     0.750000     0.770000     0.220000  ...   \n",
       "75%       4.240000     0.440000     1.390000     1.160000     0.610000  ...   \n",
       "max       8.680000     0.900000     2.000000     1.500000     1.000000  ...   \n",
       "\n",
       "              lead     nitrates     nitrites      mercury  perchlorate  \\\n",
       "count  7996.000000  7996.000000  7996.000000  7996.000000  7996.000000   \n",
       "mean      0.099431     9.819250     1.329846     0.005193    16.465266   \n",
       "std       0.058169     5.541977     0.573271     0.002967    17.688827   \n",
       "min       0.000000     0.000000     0.000000     0.000000     0.000000   \n",
       "25%       0.048000     5.000000     1.000000     0.003000     2.170000   \n",
       "50%       0.102000     9.930000     1.420000     0.005000     7.745000   \n",
       "75%       0.151000    14.610000     1.760000     0.008000    29.487500   \n",
       "max       0.200000    19.830000     2.930000     0.010000    60.010000   \n",
       "\n",
       "            radium     selenium       silver      uranium      is_safe  \n",
       "count  7996.000000  7996.000000  7996.000000  7996.000000  7996.000000  \n",
       "mean      2.920106     0.049684     0.147811     0.044672     0.114057  \n",
       "std       2.322805     0.028773     0.143569     0.026906     0.317900  \n",
       "min       0.000000     0.000000     0.000000     0.000000     0.000000  \n",
       "25%       0.820000     0.020000     0.040000     0.020000     0.000000  \n",
       "50%       2.410000     0.050000     0.080000     0.050000     0.000000  \n",
       "75%       4.670000     0.070000     0.240000     0.070000     0.000000  \n",
       "max       7.990000     0.100000     0.500000     0.090000     1.000000  \n",
       "\n",
       "[8 rows x 21 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "water.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "98ae4a37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7996, 21)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "water.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "698b3e0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'aluminium'}>,\n",
       "        <AxesSubplot:title={'center':'ammonia'}>,\n",
       "        <AxesSubplot:title={'center':'arsenic'}>,\n",
       "        <AxesSubplot:title={'center':'barium'}>,\n",
       "        <AxesSubplot:title={'center':'cadmium'}>],\n",
       "       [<AxesSubplot:title={'center':'chloramine'}>,\n",
       "        <AxesSubplot:title={'center':'chromium'}>,\n",
       "        <AxesSubplot:title={'center':'copper'}>,\n",
       "        <AxesSubplot:title={'center':'flouride'}>,\n",
       "        <AxesSubplot:title={'center':'bacteria'}>],\n",
       "       [<AxesSubplot:title={'center':'viruses'}>,\n",
       "        <AxesSubplot:title={'center':'lead'}>,\n",
       "        <AxesSubplot:title={'center':'nitrates'}>,\n",
       "        <AxesSubplot:title={'center':'nitrites'}>,\n",
       "        <AxesSubplot:title={'center':'mercury'}>],\n",
       "       [<AxesSubplot:title={'center':'perchlorate'}>,\n",
       "        <AxesSubplot:title={'center':'radium'}>,\n",
       "        <AxesSubplot:title={'center':'selenium'}>,\n",
       "        <AxesSubplot:title={'center':'silver'}>,\n",
       "        <AxesSubplot:title={'center':'uranium'}>],\n",
       "       [<AxesSubplot:title={'center':'is_safe'}>, <AxesSubplot:>,\n",
       "        <AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>]], dtype=object)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x1440 with 25 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "water.hist(bins=50,figsize=(20,20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1a04c763",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    7084\n",
       "1     912\n",
       "Name: is_safe, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "water[\"is_safe\"].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7de7637",
   "metadata": {},
   "source": [
    "## Train-Test split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dd83d985",
   "metadata": {},
   "outputs": [],
   "source": [
    "split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)\n",
    "for train_index,test_index in split.split(water,water[\"is_safe\"]):\n",
    "    train_set=water.loc[train_index]\n",
    "    test_set=water.loc[test_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1bdfbb3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1600, 21)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_set.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "04d567ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6396, 21)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_set.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bab2d94d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1418\n",
       "1     182\n",
       "Name: is_safe, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_set[\"is_safe\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "00f5f8d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    5666\n",
       "1     730\n",
       "Name: is_safe, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_set[\"is_safe\"].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc902909",
   "metadata": {},
   "source": [
    "## Train features and label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3f8b923b",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_features=train_set.drop(\"is_safe\",axis=1).copy()\n",
    "train_labels=train_set[\"is_safe\"].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6dbbbb57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6396, 20)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_features.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cc009dff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6396,)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_labels.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6f641c92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'aluminium'}>,\n",
       "        <AxesSubplot:title={'center':'ammonia'}>,\n",
       "        <AxesSubplot:title={'center':'arsenic'}>,\n",
       "        <AxesSubplot:title={'center':'barium'}>],\n",
       "       [<AxesSubplot:title={'center':'cadmium'}>,\n",
       "        <AxesSubplot:title={'center':'chloramine'}>,\n",
       "        <AxesSubplot:title={'center':'chromium'}>,\n",
       "        <AxesSubplot:title={'center':'copper'}>],\n",
       "       [<AxesSubplot:title={'center':'flouride'}>,\n",
       "        <AxesSubplot:title={'center':'bacteria'}>,\n",
       "        <AxesSubplot:title={'center':'viruses'}>,\n",
       "        <AxesSubplot:title={'center':'lead'}>],\n",
       "       [<AxesSubplot:title={'center':'nitrates'}>,\n",
       "        <AxesSubplot:title={'center':'nitrites'}>,\n",
       "        <AxesSubplot:title={'center':'mercury'}>,\n",
       "        <AxesSubplot:title={'center':'perchlorate'}>],\n",
       "       [<AxesSubplot:title={'center':'radium'}>,\n",
       "        <AxesSubplot:title={'center':'selenium'}>,\n",
       "        <AxesSubplot:title={'center':'silver'}>,\n",
       "        <AxesSubplot:title={'center':'uranium'}>]], dtype=object)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x1440 with 20 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "train_features.hist(bins=50,figsize=(15,20))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8719d99d",
   "metadata": {},
   "source": [
    "## Creating a pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7db33121",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_pipeline=Pipeline(\n",
    "[\n",
    "    (\"imputer\",SimpleImputer(strategy=\"mean\"))\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e1513804",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_features=my_pipeline.fit_transform(train_features)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07fb4073",
   "metadata": {},
   "source": [
    "## Selecting a desired model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "3735b4e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "model1=KNeighborsClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ca38b9b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "model2=LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "ec48f339",
   "metadata": {},
   "outputs": [],
   "source": [
    "model3=DecisionTreeClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "de1f3177",
   "metadata": {},
   "outputs": [],
   "source": [
    "model4=RandomForestClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6b4967a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier()"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model1.fit(train_features,train_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "78d0f5eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Tejveer\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model2.fit(train_features,train_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d923f933",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier()"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model3.fit(train_features,train_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2e3dd159",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model4.fit(train_features,train_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "edc28a4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_data=train_features[:10]\n",
    "prepared_data=my_pipeline.fit_transform(some_data)\n",
    "some_label=train_labels[:10]\n",
    "model4.predict(prepared_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "abbf570c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5068    0\n",
       "5776    0\n",
       "5493    0\n",
       "4590    0\n",
       "7241    0\n",
       "3283    0\n",
       "6649    0\n",
       "4333    1\n",
       "7440    0\n",
       "396     0\n",
       "Name: is_safe, dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f37ae8f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9055659787367104"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model1_predicted=model1.predict(train_features)\n",
    "accuracy_score(train_labels,model1_predicted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a03519e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9008755472170107"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model2_predicted=model2.predict(train_features)\n",
    "accuracy_score(train_labels,model2_predicted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "cbf9054b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model3_predicted=model3.predict(train_features)\n",
    "accuracy_score(train_labels,model3_predicted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "060d83b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model4_predicted=model4.predict(train_features)\n",
    "accuracy_score(train_labels,model4_predicted)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f1057d1",
   "metadata": {},
   "source": [
    "## Dumping and storing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "2b933178",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['water_quality.joblib']"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dump(model4,\"water_quality.joblib\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2ef52cd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'test_set' (DataFrame)\n"
     ]
    }
   ],
   "source": [
    "%store test_set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3f7ed4e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'my_pipeline' (Pipeline)\n"
     ]
    }
   ],
   "source": [
    "%store my_pipeline"
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
