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
	plt.title ( '$f_2(x)$' )        # (G) タイトル
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