# 練習-BMI計算程式
height = input('請輸入身高(m): ')
weight = input('請輸入體重(kg): ')
height = float(height)
weight = float(weight)
bmi = weight / height / height
print('你的BMI= ', bmi)
bmi = float(bmi)
if bmi < 18.5:
	print('過輕')
elif bmi >= 18.5 and bmi < 24:
	print('正常')
elif bmi >= 24 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')



