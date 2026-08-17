import pandas as pd 
file_path = "D:/Tài Liệu Môn Học/Năm 3/Data_analyst/sales_data_sample.xlsx"
dataFrame = pd.read_excel(file_path)
print("data: ")
print(dataFrame)
#hiển thị 5 dòng đầu và 5 dòng cuối 
print("5 dòng đầu của data là: ", dataFrame.head(5))
print("5 dòng cuối của data là:  ", dataFrame.tail(5))
#hiển số dòng và số cột
print("số dòng và số cột của data là: ", dataFrame.shape)
#hiển thị kiểu dữ liệu cho từng cột
data_types = dataFrame.dtypes
print("kiểu dữ liệu cho từng cột là: ", data_types)
#kiểm tra giá trị bị thiếu 
missing_values = dataFrame.isna().sum() 
print("giá trị bị thiếu là: ", missing_values)
# kiểm tra giá trị bị trùng lặp 
duplicate_values = dataFrame[dataFrame.duplicated()]
print("giá trị bị trùng lặp là: ", duplicate_values)
#thống kê mô tả dữ liệu 
describe_data = dataFrame.describe()
print("thống kê mô tả: ", describe_data)
#tìm quốc gia khác nhau 
count_different_country_values = dataFrame['COUNTRY'].nunique()
print("số lượng thành phố khác nhau là: ", count_different_country_values)
#hiển thị tên các quốc gia khác nhau 
different_countrys = dataFrame['COUNTRY'].unique()
print("tên các thành phố khác nhau là: ")
print(different_countrys)
#check giá trị khác nhau trong status và dealsize 
different_status = dataFrame['STATUS'].unique() 
different_dealsizes = dataFrame['DEALSIZE'].unique()
print("giá trị khác nhau trong status là: ", different_status)
print("giá trị khác nhau trong dealsize là: ", different_dealsizes)
