{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "from classLib_yash_Copy1 import *\n",
    "import random\n",
    "\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "length of random points: 1000\n",
      "no of waypoints: 18\n",
      "[[0.9638 0.7005]\n",
      " [0.7234 0.0248]\n",
      " [0.085  0.039 ]\n",
      " [0.3994 0.2679]\n",
      " [0.5229 0.074 ]\n",
      " [0.4136 0.7284]\n",
      " [0.1553 0.4205]\n",
      " [0.8899 0.5693]\n",
      " [0.6347 0.6904]\n",
      " [0.5297 0.8988]\n",
      " [0.115  0.6662]\n",
      " [0.7481 0.3167]\n",
      " [0.08   0.2747]\n",
      " [0.9884 0.1893]\n",
      " [0.5719 0.4321]]\n",
      "15\n",
      "^^^\n",
      "\n"
     ]
    }
   ],
   "source": [
    "\n",
    "randompoints= [] # generating random point between 0 and 1\n",
    "for i in range(1000): \n",
    "    a=[np.round(random.random(),4), np.round(random.random(),4)]\n",
    "    randompoints.append(a)\n",
    "print('length of random points:',len(randompoints))\n",
    "allWaypoint = [] #here selecting the points which have a distance of more than 0.2 from every other (no justification as to why 0.2)\n",
    "for j in range(len(randompoints)):\n",
    "    a=[]\n",
    "    for k in range(j+1,len(randompoints)):\n",
    "        s=np.linalg.norm(np.array(randompoints[j])-np.array(randompoints[k])) # not efficient way to claculate distance of one point from all others\n",
    "        a.append(s)\n",
    "    if all(i>0.15 for i in a):\n",
    "        allWaypoint.append(randompoints[j])\n",
    "print('no of waypoints:', len(allWaypoint))\n",
    "waypointList = allWaypoint[:15] #need 15 waypoints\n",
    "\n",
    "waypointList=np.round(waypointList,4)\n",
    "print(waypointList)\n",
    "print(len(waypointList))\n",
    "print(\"^^^\")\n",
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "wpN = ['wpA','wpB','wpC','wpD','wpE','wpF','wpG','wpH','wpI', 'wpJ','wpK','wpL','wpM', 'wpN','wpO','wpP']\n",
    "wpNameList=wpN[:len(waypointList)]\n",
    "#print(wpNames)\n",
    "wps =[]\n",
    "for i in range(len(waypointList)):\n",
    "    wps.append(WayPoint(wpNameList[i],waypointList[i])) #list containing waypoint class elements\n",
    "# print(\"****\")\n",
    "# print(wps[0].name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "waypoint class:wpB  x co-ord: 0.7234  y co-ord: 0.0248\n"
     ]
    }
   ],
   "source": [
    "print(wps[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['wpA', array([0.9638, 0.7005])], ['wpB', array([0.7234, 0.0248])], ['wpC', array([0.085, 0.039])], ['wpD', array([0.3994, 0.2679])], ['wpE', array([0.5229, 0.074 ])], ['wpF', array([0.4136, 0.7284])], ['wpG', array([0.1553, 0.4205])], ['wpH', array([0.8899, 0.5693])], ['wpI', array([0.6347, 0.6904])], ['wpJ', array([0.5297, 0.8988])], ['wpK', array([0.115 , 0.6662])], ['wpL', array([0.7481, 0.3167])], ['wpM', array([0.08  , 0.2747])], ['wpN', array([0.9884, 0.1893])], ['wpO', array([0.5719, 0.4321])]]\n"
     ]
    }
   ],
   "source": [
    "##################################    AIRWAYS  #####################################################\n",
    "# Here, airway is a subclass of wayPoint class and every \n",
    "wayPointInfo=[]\n",
    "for i in range(len(wpNameList)):\n",
    "    wayPointInfo.append([wpNameList[i],waypointList[i]])\n",
    "print(wayPointInfo)\n",
    "airwayNames=np.arange(len(wpNameList))\n",
    "airwayList=[]\n",
    "sampled_airways=[]\n",
    "for i in range(8): #no of airways chosen 8 at random\n",
    "    points = random.sample(wayPointInfo,2)\n",
    "    airwayList.append(Airways(airwayNames[i],points))\n",
    "    sampled_airways.append(points)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('wpI', 0.6347)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "airwayList[0].start_wp, airwayList[0].start_wp_x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "waypoint class:wpA  x co-ord: 0.9638  y co-ord: 0.7005\n",
      "waypoint class:wpB  x co-ord: 0.7234  y co-ord: 0.0248\n",
      "waypoint class:wpC  x co-ord: 0.085  y co-ord: 0.039\n",
      "waypoint class:wpD  x co-ord: 0.3994  y co-ord: 0.2679\n",
      "waypoint class:wpE  x co-ord: 0.5229  y co-ord: 0.074\n",
      "waypoint class:wpF  x co-ord: 0.4136  y co-ord: 0.7284\n",
      "waypoint class:wpG  x co-ord: 0.1553  y co-ord: 0.4205\n",
      "waypoint class:wpH  x co-ord: 0.8899  y co-ord: 0.5693\n",
      "waypoint class:wpI  x co-ord: 0.6347  y co-ord: 0.6904\n",
      "waypoint class:wpJ  x co-ord: 0.5297  y co-ord: 0.8988\n",
      "waypoint class:wpK  x co-ord: 0.115  y co-ord: 0.6662\n",
      "waypoint class:wpL  x co-ord: 0.7481  y co-ord: 0.3167\n",
      "waypoint class:wpM  x co-ord: 0.08  y co-ord: 0.2747\n",
      "waypoint class:wpN  x co-ord: 0.9884  y co-ord: 0.1893\n",
      "waypoint class:wpO  x co-ord: 0.5719  y co-ord: 0.4321\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(wps)):\n",
    "    print(wps[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wpIstart coords0.63470.6904wpH\n",
      "wpFstart coords0.41360.7284wpA\n",
      "wpJstart coords0.52970.8988wpA\n",
      "wpAstart coords0.96380.7005wpO\n",
      "wpBstart coords0.72340.0248wpO\n",
      "wpHstart coords0.88990.5693wpM\n",
      "wpDstart coords0.39940.2679wpO\n",
      "wpGstart coords0.15530.4205wpC\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(airwayList)):\n",
    "    print(airwayList[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.6347, 0.6904]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = [airwayList[0].start_wp_x,airwayList[0].start_wp_y]\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([0.8899, 0.5693], 'wpH')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b=[airwayList[0].end_wp_x, airwayList[0].end_wp_y]\n",
    "b,airwayList[0].end_wp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "ac_per_scenario =8  # just a random number to have no of aircraft in one scenario\n",
    "aircraftList=[]\n",
    "aircraft_name=np.arange(ac_per_scenario)\n",
    "for i in range(ac_per_scenario):\n",
    "    aircraft= Aircraft(aircraft_name[i],random.choice(sampled_airways))\n",
    "    aircraftList.append(aircraft)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "names=[]\n",
    "x =[]\n",
    "y=[]\n",
    "\n",
    "for i in range(len(wps)):\n",
    "    names.append(wps[i].name)\n",
    "    x.append(wps[i].x)\n",
    "    y.append(wps[i].y)\n",
    "air_x=[]\n",
    "air_y=[]\n",
    "for i in range(len(airwayList)):\n",
    "    a=[airwayList[i].start_wp_x,airwayList[i].start_wp_y]\n",
    "    b=[airwayList[i].end_wp_x,airwayList[i].end_wp_y]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9638 0.7005\n",
      "0.7234 0.0248\n",
      "0.085 0.039\n",
      "0.3994 0.2679\n",
      "0.5229 0.074\n",
      "0.4136 0.7284\n",
      "0.1553 0.4205\n",
      "0.8899 0.5693\n",
      "0.6347 0.6904\n",
      "0.5297 0.8988\n",
      "0.115 0.6662\n",
      "0.7481 0.3167\n",
      "0.08 0.2747\n",
      "0.9884 0.1893\n",
      "0.5719 0.4321\n",
      "[0.6347, 0.6904] [0.8899, 0.5693]\n",
      "[0.4136, 0.7284] [0.9638, 0.7005]\n",
      "[0.5297, 0.8988] [0.9638, 0.7005]\n",
      "[0.9638, 0.7005] [0.5719, 0.4321]\n",
      "[0.7234, 0.0248] [0.5719, 0.4321]\n",
      "[0.8899, 0.5693] [0.08, 0.2747]\n",
      "[0.3994, 0.2679] [0.5719, 0.4321]\n",
      "[0.1553, 0.4205] [0.085, 0.039]\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA2oAAANOCAYAAABgFv8rAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzdd3QUheLF8e9selk6JBQRULIgoDQLSEACSAsRSSCUIKHaUcQCiij6FAUrSpHeJJQEMaFLUYpYQpMioffeE1oSsr8/VvyhorQks9m9n3PeObK72bkc3vFx38zcMex2OyIiIiIiIuI8LGYHEBERERERkb9SURMREREREXEyKmoiIiIiIiJORkVNRERERETEyaioiYiIiIiIOBlPsw5cpEgRe5kyZcw6vIiIiIiIiKlWr1593G63F73We6YVtTJlypCcnGzW4UVERERERExlGMaef3tPlz6KiIiIiIg4GRU1ERERERERJ6OiJiIiIiIi4mRU1ERERERERJzMdYuaYRhjDcM4ahjGxn953zAMY4hhGNsNw/jNMIzq2R9TRERERETEfdzIGbXxQJP/eL8pUP6P//QAht9+LBEREREREfd13aJmt9uXASf/4yOPARPtDj8BBQzDKJ5dAUVERERERNxNdtyjVhLYd9Wv9//x2j8YhtHDMIxkwzCSjx07lg2HFhERERERcT3ZUdSMa7xmv9YH7Xb7SLvdXtNut9csWvSaD+AWERERERFxe9lR1PYDd1z161LAwWz4XhEREREREbeUHUUtEXjij/XHh4Azdrv9UDZ8r4iIiIiIiFvyvN4HDMOIAx4BihiGsR94C/ACsNvtI4C5QDNgO3Ae6JxTYUVERERERNzBdYua3W5vd5337cCz2ZZIRERERETEzWXHpY8iIiIiIiKSjVTUREREREREnIyKmoiIiIiIiJNRURMREREREXEyKmoiIiIiIiJORkVNRERERETEyaioiYiIiIiIOBkVNRERERERESejoiYiIiIiIuJkVNREREREREScjIqaiIiIiIiIk1FRExERERERcTIqaiIiIiIiIk5GRU1ERERERMTJqKiJiIiIiIg4GRU1ERERERERJ6OiJiIiIiIi4mRU1ERERERERJyMipqIiIiIiIiTUVETERERERFxMipqIiIiIiIiTkZFTUTElRxY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\n",
      "text/plain": [
       "<Figure size 1080x1080 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig,ax=plt.subplots(1,1,figsize=(15,15))\n",
    "plt.scatter(x,y)\n",
    "for i,n in enumerate(names):\n",
    "    plt.annotate(n, (x[i],y[i]))\n",
    "    print(x[i],y[i])\n",
    "for i in range(len(airwayList)):\n",
    "    a=[airwayList[i].start_wp_x,airwayList[i].start_wp_y]\n",
    "    b=[airwayList[i].end_wp_x,airwayList[i].end_wp_y]\n",
    "    print(a,b)\n",
    "    plt.plot(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x22dd5646748>]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "c=[0.6347, 0.6904]\n",
    "d=[0.8899, 0.5693]\n",
    "plt.plot(c,d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "[airway_list[0].start_wp_x,airway_list[0].start_wp_y],airway_list[0].start_wp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "airway_list[0].end_wp_x,airway_list[0].end_wp_y,airway_list[0].end_wp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
