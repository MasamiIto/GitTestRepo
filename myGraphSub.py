# coding: shift_jis
#################################################################################
#
# 
#
#################################################################################

import  os
import  sys
import 	json
import 	csv
import  datetime
import 	locale
import  numpy 				as 	np
import 	matplotlib.pyplot 	as 	plt
import  pandas				as 	pd
from 	mpl_toolkits.mplot3d 	import Axes3D           # (A)
#%matplotlib inline




#import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec


#################################################################################
# 一番簡単なグラフ
#################################################################################
def g0():
	x = np.arange(-3, 3, 0.1)
	y = np.sin(x)
	plt.plot(x, y)
	plt.show()
#################################################################################
# 一番簡単なグラフ（データは引数で指定）
#################################################################################
def g0a( x , y ):
	plt.plot(x, y)
	plt.show()
	###------------------------------------------ 3次元グラフ
#################################################################################
# 
#################################################################################
def g3Da( xn, x0,x1 ):
	print('------------------------------------------------- sample:03B( 3D-graph )' );
#	xn       = 9
#	x0       = np.linspace( -2, 2, xn )            # (A)
#	x1       = np.linspace( -2, 2, xn )            # (B)
	xx0, xx1 = np.meshgrid( x0 , x1 )              # (B)
	y        = np.zeros   ( (len(x0), len(x1)) )   # (C)
	for i0 in range( xn ):
		for i1 in range( xn ):
			y[i1, i0] = f3( x0[i0], x1[i1] ) 	   # (D)

	plt.figure (figsize=(5, 3.5))
	ax = plt.subplot( 1, 1, 1, projection='3d')    # (C)
	ax.plot_surface( xx0 , xx1,  y , 
	            rstride  = 1    , 
				cstride  = 1    , 
				alpha    = 0.3  ,
                color    ='blue', 
				edgecolor='black')  			   # (D)
	ax.set_zticks( (0, 0.2) )                      # (E)
	ax.view_init( 75 ,  -95 ) 					   # (F)
	plt.show()	

#################################################################################
# 3Dグラフ表示
#################################################################################
def g3D( ):
	X = np.arange(-5, 5, 0.25)
	Y = np.arange(-5, 5, 0.25)
	X, Y = np.meshgrid(X, Y)
	R = np.sqrt(X**2 + Y**2)
	Z = np.sin(R)

	fig = plt.figure()
	ax = Axes3D(fig)
	ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

	plt.show()
#################################################################################
# 3Dグラフ表示
#################################################################################
def g3D2( ):
# This import registers the 3D projection, but is otherwise unused.
#from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

#from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
#import matplotlib.pyplot as plt
#import numpy as np

	fig = plt.figure()

	ax = fig.add_subplot(1, 2, 1, projection='3d')
	X = np.arange(-5, 5, 0.25)
	Y = np.arange(-5, 5, 0.25)
	X, Y = np.meshgrid(X, Y)
	R = np.sqrt(X**2 + Y**2)
	Z = np.sin(R)
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
	ax.set_zlim3d(-1.01, 1.01)

#ax.w_zaxis.set_major_locator(LinearLocator(10))
#ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))

	fig.colorbar(surf, shrink=0.5, aspect=5)

	from mpl_toolkits.mplot3d.axes3d import get_test_data
	ax = fig.add_subplot(1, 2, 2, projection='3d')
	X, Y, Z = get_test_data(0.05)
	ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

	plt.show()
# Fixing random state for reproducibility
#################################################################################
# グラフ表示
#################################################################################
def gBase( ):
	np.random.seed(19680801)

	dt = 0.01
	t = np.arange(0, 30, dt)
	nse1 = np.random.randn(len(t))                 # white noise 1
	nse2 = np.random.randn(len(t))                 # white noise 2

	# Two signals with a coherent part at 10Hz and a random part
	s1 = np.sin(2 * np.pi * 10 * t) + nse1
	s2 = np.sin(2 * np.pi * 10 * t) + nse2

	fig, axs = plt.subplots(2, 1)
	axs[0].plot(t, s1, t, s2)
	axs[0].set_xlim(0, 2)
	axs[0].set_xlabel('time')
	axs[0].set_ylabel('s1 and s2')
	axs[0].grid(True)

	cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
	axs[1].set_ylabel('coherence')

	fig.tight_layout()
	plt.show()
#################################################################################
# グラフ表示
#################################################################################
def gBase3( ):

	x = np.linspace(0, 2 * np.pi, 20)
	y = np.sin(x)
	yp = None
	xi = np.linspace(x[0], x[-1], 100)
	yi = np.interp(xi, x, y, yp)

	fig, ax = plt.subplots()
	ax.plot(x, y, 'o', xi, yi, '.')
	plt.show()
	
#################################################################################
# グラフ表示
#################################################################################
def gBase4( ):
	
	# Data for plotting
	t = np.arange(0.0, 2.0, 0.01)
	s = 1 + np.sin(2 * np.pi * t)

	fig, ax = plt.subplots()
	ax.plot(t, s)

	ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
	ax.grid()

	fig.savefig("test.png")
	plt.show()


	
#################################################################################
# グラフ表示
#################################################################################
def gBase5( ):
	
	fig = plt.figure(tight_layout=True)
	gs = gridspec.GridSpec(2, 2)

	ax = fig.add_subplot(gs[0, :])
	ax.plot(np.arange(0, 1e6, 1000))
	ax.set_ylabel('YLabel0')
	ax.set_xlabel('XLabel0')

	for i in range(2):
		ax = fig.add_subplot(gs[1, i])
		ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
		ax.set_ylabel('YLabel1 %d' % i)
		ax.set_xlabel('XLabel1 %d' % i)
		if i == 0:
			for tick in ax.get_xticklabels():
				tick.set_rotation(55)
#	fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()
#	fig.align_xlabels()
#	fig.align_ylabels()

	plt.show()
	
#################################################################################
# グラフ表示
#################################################################################
def gBase2( ):
	
	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
	sizes = [15, 30, 45, 10]
	explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.show()
#################################################################################
# グラフ表示
#################################################################################
def f2(x, w):
    return (x - w) * x * (x + 2) #(A) 関数定義
def f3(x0, x1):
    r = 2 * x0**2 + x1**2
    ans = r * np.exp(-r)
    return ans
###------------------------------------------ 2次元グラフ
def sample03A():
	print('------------------------------------------------- sample:03A( 2D-graph )' );
	x = np.linspace(-3, 3, 100) 	# (B) x を100 分割にする
	plt.plot( x, f2(x, 2) , color='black'         , label='$w=2$') #(C)
	plt.plot( x, f2(x, 1) , color='cornflowerblue', label='$w=1$') #(D)
	plt.legend(loc="upper left")    # (E) 凡例表示
	plt.ylim  ( -15 , 15   )        # (F) y 軸の範囲
	plt.title ( '$Function(x)$' )        # (G) タイトル
	plt.xlabel( '$x$'      )        # (H) x ラベル
	plt.ylabel( '$y$'      )        # (I) y ラベル
	plt.grid  ( True)               # (J) グリッド
	plt.show()
#
###------------------------------------------ 3次元グラフ
def sample03B():
	print('------------------------------------------------- sample:03B( 3D-graph )' );
	xn       = 9
	x0       = np.linspace( -2, 2, xn )            # (A)
	x1       = np.linspace( -2, 2, xn )            # (B)
	xx0, xx1 = np.meshgrid( x0 , x1 )              # (B)
	y        = np.zeros   ( (len(x0), len(x1)) )   # (C)
	for i0 in range( xn ):
		for i1 in range( xn ):
			y[i1, i0] = f3( x0[i0], x1[i1] ) 	   # (D)

	plt.figure (figsize=(5, 3.5))
	ax = plt.subplot( 1, 1, 1, projection='3d')    # (C)
	ax.plot_surface( xx0 , xx1,  y , 
	            rstride  = 1    , 
				cstride  = 1    , 
				alpha    = 0.3  ,
                color    ='blue', 
				edgecolor='black')  			   # (D)
	ax.set_zticks( (0, 0.2) )                      # (E)
	ax.view_init( 75 ,  -95 ) 					   # (F)
	plt.show()	
###------------------------------------------ COLOR MAP
def sample03C():
	print('------------------------------------------------- sample:03C( COLOR )' );
	xn = 9
	x0 = np.linspace(-2, 2, xn)            # (A)
	x1 = np.linspace(-2, 2, xn)            # (B)
	y = np.zeros((len(x0), len(x1)))       # (C)
	for i0 in range(xn):
		for i1 in range(xn):
			y[i1, i0] = f3(x0[i0], x1[i1]) # (D)
		
	plt.figure(figsize=(3.5, 3))
	plt.gray()                     # (A)
	plt.pcolor(y)                  # (B)
	plt.colorbar()                 # (C)
	plt.show()
	

###------------------------------------------ 等高線グラフ
def sample03D():
	print('------------------------------------------------- sample:03D( CONTOUR )' );
	xn = 50
	x0 = np.linspace(-2, 2, xn)
	x1 = np.linspace(-2, 2, xn)

	y = np.zeros((len(x0), len(x1)))
	for i0 in range(xn):
		for i1 in range(xn):
			y[i1, i0] = f3(x0[i0], x1[i1])

	xx0, xx1 = np.meshgrid(x0, x1)                     # (A)

	plt.figure(1, figsize=(4, 4))
	cont = plt.contour(xx0, xx1, y, 5, colors='black') # (B)
	cont.clabel(fmt='%3.2f', fontsize=8)               # (C)
	plt.xlabel('$x_0$', fontsize=14)
	plt.ylabel('$x_1$', fontsize=14)
	plt.show()	
	
#################################################################################
#
# MAIN PROGRAM
#
#################################################################################
if __name__ == '__main__': # 追加
	print('------------------------------------------------- SUB-----' );
	sample03A()