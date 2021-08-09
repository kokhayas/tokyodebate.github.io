import csv

#input.tsv の中身は以下 タブの個数で分類する 大会名は<h2>,その他は<p>
#
# 【Tokyo mini 2020】
# 	【Ajudicatior Prize】
# 	[Breaking Adjudicator]
# 	Todai Taro
#
# <h2 style="text-align: center;">LSE Open 2021</h2>
# <p style="text-align: center;">【Ajudicatior Prize】
# [Breaking Adjudicator]
# Todai Taro</p>

with open('output2020.txt', 'w') as fw:
	with open('input2020.tsv', encoding='utf-8', newline='') as fr:
		counter = 0
		memory = ''
		for cols in csv.reader(fr, delimiter='\t'):

			if len(cols) == 0:  # empty line
				if counter != 0:
					memory = memory + '</p>'
					fw.write(memory + '\n')
					counter = 0


			elif len(cols) == 1:  # 大会名
				if counter != 0:
					memory = memory + '</p>'
					fw.write(memory + '\n')
					counter = 0


				output = '<h2 style="text-align: center;">' + cols[0] + '</h2>'
				fw.write(output + '\n')


			elif len(cols) == 2: #
				if counter == 0:
					memory = '<p style="text-align: center;">' + cols[1] + '\n'
					counter += 1
				else:
					memory = memory + cols[1] + '\n'


			print(cols)
			print(len(cols))

