#!/usr/bin/env python
import sys

args = sys.argv

Line_Count = 0
piRNA_Count = 0
siRNA_Count = 0
Pair_Count = 0
#Pair_Flag = 0
Pair_Count_2_8 = 0
Pair_Count_2_9 = 0
Pair_Count_2_10 = 0
match_score = 0
GU_Count = 0

siRNA_ID_list =[]
piRNA_ID_list =[]
siRNA_seq_list =[]
piRNA_seq_list =[]

# 置き換え表の作成
# 置換する文字をつなげて記述します
table_RC = str.maketrans('GATCU', 'CTAGA') #文字置き換え用のテーブル, G->C, A->T, T->A, C->G, U->A
table_UT = str.maketrans('U', 'T') #文字置き換え用のテーブル,  U->T

input_siRNA = args[1] #library_1
input_piRNA = args[2] #library_2

output_file1 = "complementary_analysis_result1.txt"
output_file2 = "complementary_analysis_result2.txt"
#print(output_file)

file_out = open(output_file1, "w") #.txtファイルを書き込みモードで作成
file_out.writelines("library_1_ID" + "\t")
#file_out.writelines("Pair_Count_2_8" + "\t")
#file_out.writelines("Pair_Count_2_9" + "\t")
file_out.writelines("Pair_Count_2_10" + "\n")

file_out2 = open(output_file2, "w") #.txtファイルを書き込みモードで作成
file_out2.writelines("library_1_ID" + "\t" + "library_1_seq_10nt" + "\t")
file_out2.writelines("library_2_ID" + "\t" + "library_2_seq_10nt" + "\t")
file_out2.writelines("match_score" + "\t" + "GU_count" + "\n")

### store piRNA library in memory ####
for piRNA_line in open(input_piRNA, "r"): # library_2を読み込んで１０塩基分をストア
	piRNA_data = piRNA_line[:-1].split('\t')

	Line_Count += 1     # 行数をカウントアップ

	if (">" in piRNA_data[0]):
		piRNA_ID_list.append(piRNA_data[0])
		#print(piRNA_ID_list[piRNA_Count])
	else:
		piRNA_seq_data = piRNA_data[0][0:10] #Store piRNA 1-10nt sequence
		#print(piRNA_seq_data)
		piRNA_seq_data_UT = piRNA_seq_data.translate(table_UT) #U->T
		piRNA_seq_list.append(piRNA_seq_data_UT) #Store piRNA 1-10nt sequence
		#print(piRNA_seq_list[piRNA_Count])
		#file_out.writelines(piRNA_seq_list[piRNA_Count])
		piRNA_Count += 1


for siRNA_line in open(input_siRNA, "r"): # library_1を読み込む
	siRNA_data = siRNA_line[:-1].split('\t')

	Line_Count += 1     # 行数をカウントアップ

	if (">" in siRNA_data[0]):
		siRNA_ID_list.append(siRNA_data[0])
		#print(siRNA_ID_list[siRNA_Count])
	else:
		siRNA_seq_list.append(siRNA_data[0][0:10])
		#print(siRNA_seq_list[siRNA_Count])

		reverse = siRNA_seq_list[siRNA_Count][::-1]
		#print(reverse)

		reverse_complment = reverse.translate(table_RC)
		#print(reverse_complment)
		for i in range(piRNA_Count):
			for j in range(1,10): #skip first base
				#print (str(j), reverse_complment[j], piRNA_seq_list[i][j])
				if (reverse_complment[j] == piRNA_seq_list[i][j]):
					match_score += 1
					if j == 9:
						Pair_Count_2_10 += 1
				#if (j == 7 & match_score == 7):
				#	Pair_Flag += 1
				#	Pair_Count_2_8 += 1
					#print("Pair_Count_2_8 =　" + str(Pair_Count_2_8))
				#if (j == 8 & match_score == 8):
				#	Pair_Count_2_9 += 1
					#print("Pair_Count_2_9 =　" + str(Pair_Count_2_9))
				#if (j == 9 & match_score == 9):
				#	Pair_Count_2_10 += 1
					#print("Pair_Count_2_10 =　" + str(Pair_Count_2_10))
				elif ((reverse_complment[j] == "C") & (piRNA_seq_list[i][j] == "T")): #GT in the original sequence
					match_score += 1
					GU_Count += 1
				elif ((reverse_complment[j] == "A") & (piRNA_seq_list[i][j] == "G")): #TG in the original sequence
					match_score += 1
					GU_Count += 1
				else:
					if j == 8:
						Pair_Count_2_8 += 1
					if j == 9:
						Pair_Count_2_9 += 1
					break
#				if (reverse_complment[j] != piRNA_seq_list[i][j]):
#					break
			#--- End of the nucleotide matching ---

			#--- Show the nucleotide matching result for each piRNA---
			if match_score >= 9:
				file_out2.writelines(siRNA_ID_list[siRNA_Count].split('>')[1] + "\t")
				file_out2.writelines(siRNA_seq_list[siRNA_Count] + "\t")
				#file_out2.writelines(reverse + "\t")
				#file_out2.writelines(reverse_complment + "\t")
				file_out2.writelines(piRNA_ID_list[i].split('>')[1] + "\t")
				file_out2.writelines(piRNA_seq_list[i] + "\t")
#				file_out2.writelines("match_score: " + str(match_score) + "\t")
#				file_out2.writelines("GU_Count: " + str(GU_Count) + "\n")
				file_out2.writelines(str(match_score) + "\t")
				file_out2.writelines(str(GU_Count) + "\n")
				Pair_Count += 1 #count up the matching piRNAs for each siRNA
				#Pair_Flag = 0 #reset the Flag

			#print("match_score = " + str(match_score))
			match_score = 0
			GU_Count = 0
		#print(siRNA_ID_list[siRNA_Count], Pair_Count)

		if Pair_Count > 0:
			#print(siRNA_ID_list[siRNA_Count], Pair_Count)
			file_out.writelines(siRNA_ID_list[siRNA_Count].split('>')[1] + "\t")
#			file_out.writelines(siRNA_seq_list[siRNA_Count] + "\t")
#			file_out.writelines("Pair_Count (Score >=7):　" + str(Pair_Count) + "\t")
#			file_out.writelines("Pair_Count_2_8:　" + str(Pair_Count_2_8) + "\t")
#			file_out.writelines("Pair_Count_2_9:　" + str(Pair_Count_2_9) + "\t")
#			file_out.writelines("Pair_Count_2_10:　" + str(Pair_Count_2_10) + "\n")
			#file_out.writelines(str(Pair_Count_2_8) + "\t")
			#file_out.writelines(str(Pair_Count_2_9) + "\t")
			file_out.writelines(str(Pair_Count_2_10) + "\n")

			file_out2.writelines("\n")
		siRNA_Count += 1
		if siRNA_Count % 10000 == 0:
			print("file1_RNA_analyzed = " + str(siRNA_Count))
		Pair_Count = 0
		Pair_Count_2_8 = 0
		Pair_Count_2_9 = 0
		Pair_Count_2_10 = 0

file_out.close() # 書き込み用のファイルを閉じる

print("total_line = " + str(Line_Count))
print("piRNA_count = " + str(piRNA_Count))
print("siRNA_count = " + str(siRNA_Count))
print("Finish!")


