#!/usr/bin/env python
#import math #libraryをインポート
import sys

args = sys.argv
#print(args[0])
#print(args[1])

#pythonでは、行頭のタブが重要　タブを深くすることがperlの{}の役割
#読み込んだデータは文字列なので、実数型に変換してから計算する
#変数はstr型に変換してから出力
#読み込むデータの要素数が全て揃ってないとエラーになる

Line_Count = 0
piRNA_Count = 0
siRNA_Count = 0
Pair_Count = 0

siRNA_RC = [0] * 10

siRNA_ID_list =[]
piRNA_ID_list =[]
siRNA_seq_list =[]
piRNA_seq_list =[]

# 置き換え表の作成
# 置換する文字をつなげて記述します
table = str.maketrans('GATC', 'CTAG') #文字置き換え用のテーブル, G->C, A->T, T->A, C->G

input_siRNA = args[1] #test_siRNA
input_piRNA = args[2] #test_piRNA
#input_file = "Dam-Stil-2-vs-Dam.gatc-FDR0.01.peaks.gff"
#output_file = input_file.split('.')[0]+input_file.split('.')[1]+input_file.split('.')[2]+"_converted.tsv"
output_file = "complementary_analysis_result.txt"
#print(output_file)

file_out = open(output_file, "w") #.txtファイルを書き込みモードで作成
file_out.writelines("siRNA_ID" + "\t" + "Pair_Count" + "\n")

### store piRNA library in memory ####
for piRNA_line in open(input_piRNA, "r"): # .txtファイルを１行ごとに読み込む
	piRNA_data = piRNA_line[:-1].split('\t') #１行読み込む #返り値はリスト型になっている。

	Line_Count += 1     # 行数をカウントアップ
	#if(Line_Count > 10):	#最初の２つぐらいでテストしたい時
	#	break

#	if (Line_Count ==1):
#		continue

	if (">" in piRNA_data[0]):
		piRNA_ID_list.append(piRNA_data[0])
		print(piRNA_ID_list[piRNA_Count])
	else:
		piRNA_seq_list.append(piRNA_data[0][0:10]) #Store piRNA 1-10nt sequence
		print(piRNA_seq_list[piRNA_Count])
		#file_out.writelines(piRNA_seq_list[piRNA_Count])
		piRNA_Count += 1


for siRNA_line in open(input_siRNA, "r"): # .txtファイルを１行ごとに読み込む
	siRNA_data = siRNA_line[:-1].split('\t') #１行読み込む #返り値はリスト型になっている。

	Line_Count += 1     # 行数をカウントアップ
	#if(Line_Count > 10):	#最初の２つぐらいでテストしたい時
	#	break

#	if (Line_Count ==1):
#		continue

	if (">" in siRNA_data[0]):
		siRNA_ID_list.append(siRNA_data[0])
		print(siRNA_ID_list[siRNA_Count])
	else:
		siRNA_seq_list.append(siRNA_data[0][0:10])
		print(siRNA_seq_list[siRNA_Count])

		# 文字列[::-1]とすれば反転できる
		reverse = siRNA_seq_list[siRNA_Count][::-1]
		#print(reverse)

		reverse_complment = reverse.translate(table)
		print(reverse_complment)
		for i in range(piRNA_Count):
			if (reverse_complment == piRNA_seq_list[i]):
				Pair_Count += 1
		print(siRNA_ID_list[siRNA_Count], Pair_Count)
		file_out.writelines(siRNA_ID_list[siRNA_Count] + "\t" + str(Pair_Count) + "\n")
		siRNA_Count += 1

	Pair_Count = 0

file_out.close() # 書き込み用のファイルを閉じる


print("total_line = " + str(Line_Count))
print("piRNA_count = " + str(piRNA_Count))
print("siRNA_count = " + str(siRNA_Count))
print("Finish!")


