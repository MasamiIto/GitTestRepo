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

import  mysub1				as 	sb1

#################################################################################
#
#################################################################################
def sample01():
	print('------------------------------------------------- sample:01(list)' );
	x=123
	y=1/3
	s='Hello!'
	print( 'Text [{0:5}]'.format(s) )
	print( 'Int  [{0:5}]'.format(x) )
	print( 'Real [{0:.4f}]'.format(y) )

#------------------------ ARRAY
	ary =[1,2,3,4]
	print('ARRRY{0}'.format(ary))
	print('LEN={0}'.format( len( ary ) ))

	ary2 =[[1,2,3,4] , [5,6,7,8]]
	print('ARRRY{0}'.format(ary2))
	print('LEN={0}'.format( len( ary2 ) ))
#             range renzoku suu sakusei
	for i in range( len(ary) ) :
		print('	ary[{0}]={0}'.format( i,ary[i] ))


#################################################################################
#
#################################################################################
def sample02():
	print('------------------------------------------------- sample:02(np)' );
	A = np.array( [[1,2,3],[5,6,7],[8,9,10]] )
	B = np.array( [[1,2,3],[5,6,7],[8,9,10]] )
	w,h = A.shape	
	print('matrix A=s{0}'.format(A))
	print('matrix B=s{0}'.format(B))
	print('LEN={0} {1},{2}'.format( len( A ) , w ,h ) )
	C = A+B
	print( 'A+B=',C );
	D = A*B
	print( 'A*B=',D );
	print('END' )	
#################################################################################
# ファイルREAD/WRITE
#################################################################################
def sample04():
	print('------------------------------------------------- sample:04' );
	print("FILE Rewad/Write" )
	filename = 'table0.txt'
	
#----------------------------- READ
	f=open( filename ,'r' )
	for row in f:
		print (row.strip() )
	f.close()
#----------------------------- READ
	f=open( filename ,'r' )
	a=f.readlines()
	f.close()
	print( a)
#----------------------------- READ by WITH ( NO NEED CLOSE)
	with open(filename , mode='r') as f:
#		l_strip = [s.strip() for s in f.readlines()]
		for s in f.readlines():
			print(s.strip()) 
#----------------------------- WRITE
	f = open('test.txt','w')
	f.write('TEST\n')
	f.close()	
#----------------------------- APPEND
	f = open('test.txt','a')
	f.write('APPENDED TEXT\n')
	f.close()

#################################################################################
# CSVファイルREAD/WRITE
#################################################################################
def sample05():
	print('------------------------------------------------- sample:05( csv )' );
	filename = 'table1.csv'
	
	f = open( filename, 'r')
	reader = csv.reader( f )
	header = next( reader )
	for row in reader:
		print (row )
	f.close()
	
	with open(filename, 'r') as f:
		reader = csv.reader( f )
		header = next( reader )  # ヘッダーを読み飛ばしたい時
#		print( header , type( header) )
		for row in reader:
			print ( row )         # 1行づつ取得できる
			for s in row:
				print(s)
			
#################################################################################
def sample05A():  #pandas
	print('------------------------------------------------- sample:05( pandas )' );
	filename = 'table1.csv'
	
	df = pd.read_csv( filename )
	print('--- 全体表示---' )
	print (df)       # show all column
	print('---- name colum ----' )
	print (df['name'])  # show 'A' column
	print('--- name 取り出し---' )
	for s in df['name'] :
		print(s)
	print('--- name 取り出し2---' )
	for (i,row) in df.iterrows():
#		print('  --- ',i )
#		print(row)
		print('   {0}:{1}'.format(i, row['name']) )
	
	
#################################################################################
# JSONファイル
#################################################################################
def sample06():
	print('------------------------------------------------- sample:06( JSON )' );
	print("data_json_large Data" )
	f2=open('data/data_json_large.json','r' )
	jsonData = json.load(f2)
	f2.close()
	print (json.dumps(jsonData, sort_keys = True, indent = 4))
	for x in jsonData :
		print( str(x['index']) +":" + x['name'] )
		lst= x['friends'] 
		for z in  lst :
			print("		"+ z['name'])
def sample06x():
	print('------------------------------------------------- sample:04' );
	print("TokyoMetro Data" )
	f2=open('data/data_json_Metro.json','r' )
	jsonData = json.load(f2)
	f2.close()
	print (json.dumps(jsonData, sort_keys = True, indent = 4))
	for x in jsonData :
		print( x['dc:date'] )
def sample06y():   #NG by SHIFT-JIS JSON
	print('------------------------------------------------- sample:04' );
	print("data_json_Weather Data" )
	f2=open('data/data_json_Weather.json','r' )
	jsonData = json.load(f2)
	f2.close()
	print (json.dumps(jsonData, sort_keys = True, indent = 4))
	for x in jsonData :
		print( x['dc:date'] )
#################################################################################
# 時刻
#################################################################################
def sample07():
	print('------------------------------------------------- sample:07' );
	time="151230"
	day = time[0:2]
	h   = time[2:4]
	m   = time[4:6]
	s   = time[6:8]
	print( day +","+ h +","+ m +","+ s)	
#---------------------------------------------------	
	d = datetime.datetime.today()
	print( "  RAW      : " + str(d )) 
	print( '  DATE     : %s/%s/%s' % (d.year, d.month, d.day))
	print( '  TIME     : %s:%s:%s.%s' % (d.hour, d.minute, d.second, d.microsecond))
	print( d.strftime("  DATE TIME: %Y/%m/%d %H:%M:%S"))
# 地域の設定
	locale.setlocale(locale.LC_ALL, 'ja') 
	print ('  LOCALE:'+ str(locale.getlocale()))
#---------------------------------------------------	
	y   = int(d.year)
	mon = int(d.month)
	d2  = datetime.datetime( y,mon , int(day) , int(h) , int(m) , 14 )
	print( d2.strftime("  DATE TIME: %Y/%m/%d %H:%M:%S"))
#################################################################################
# クラス
#################################################################################
class myStruct:
	def __init__(self):
		self.name = ''				
		self.data1 = 11
		self.data2 = 222
		self.data3 = 3333
		
	def __call__(self,nm,da1,da2,da3):
		self.name = nm
		self.data1 =da1
		self.data2 =da2
		self.data3 =da3
	def dump(self):
		print('  name={0},D1={1},D2={2}'.format( self.name,self.data1,self.data2 ))

#################################################################################
def sample08A():
	print('------------------------------------------------- sample:08A( struct )' );
	myst1 = myStruct()
	myst2 = myStruct()
	myst2('masami',123,456,789)

	myst1.name ='ito'
	myst1.data1=9999
	print( 'name={0},D1={1}'.format(myst1.name , myst1.data1));
	print( 'name={0},D1={1}'.format(myst2.name , myst2.data1));
	myst2.dump()
#	print( myst2 );
	

#################################################################################
#
# MAIN PROGRAM
#
#################################################################################
	
print('------------------------------------------------- MAIN-----' );
args = sys.argv	
argc = len( args )
print('ARGC=' , argc )
#
#-------------------- LIST,MATRIX
#sample01()
#sample02()
#-------------------- GRAPH
#sb1.sample03A()
#sample03B()
#sample03C()
#sample03D()

#sample04()
#sample05()
#sample05A()
#sample06()
#sample07()
sample08A()
