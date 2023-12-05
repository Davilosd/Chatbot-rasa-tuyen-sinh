# 0: PtIT HCM
# 1: PtIT HN
# 2: bach khoa 
# 3: su pham ky thuat

# 0: 2023
# 1: 2022
# 2: 2021

# 0: cntt
# 1: attt
# 2: khmt
# 3: QTKD
# 4: iot
import random
import mysql.connector

host = "localhost"
user = "root"

password = "123456"
database = "chabot"

# Kết nối tới cơ sở dữ liệu
conn = mysql.connector.connect(
    host=host,
    port=3305,
    user=user,
    password=password,
    database=database
)

def mySql():
    import mysql.connector

    host = "localhost"
    user = "root"
    port =3305
    password = "123456"
    database = "chabot"

    # Kết nối tới cơ sở dữ liệu
    conn = mysql.connector.connect(
        host=host,
        port = port,
        user=user,
        password=password,
        database=database
    )
    return conn
# Tạo một đối tượng cursor để thực hiện các truy vấn SQL
# cursor = conn.cursor()

# # Thực hiện truy vấn SQL
# query = "SELECT * FROM truong"
# cursor.execute(query)
# # Lấy kết quả
# results = cursor.fetchall()

# # In kết quả
# for row in results:
#     print(row)

# data_truong = []
# q_truong = 'select idtruong from truong'
# cursor.execute(q_truong)
# results_truong = cursor.fetchall()

# for row in results_truong:
    
#     data_truong.append(row[0])

# Đóng kết nối

def exec_query(query):
    #cursor = conn.cursor()
    # Thực hiện truy vấn SQL
    conn = mySql()
    cursor = conn.cursor()
    cursor.execute(query)
    # Lấy kết quả
    results = cursor.fetchall()
    conn.close()
    return results

def nganh_noi_bat(truong):
    query = exec_query(f"SELECT N.TENNGANH, diem FROM (chabot.nganh_cua_truong t JOIN CHABOT.NGANH n ON t.idtruong = '{truong}' and nam =2023 AND n.idnganh = t.idnganh ) order by diem desc limit 3; ")
    ket_qua = []
    for d in query:
        ket_qua.append(d[0])
    return ket_qua

def cac_khoi_thi():
    query = exec_query(f'select idkhoithi from khoi_thi')
    ket_qua = []
    for d in query:
        ket_qua.append(d[0])
    return ket_qua

def mon_cua_khoi_thi(khoi):
    query = exec_query(f'select thongtin from khoi_thi where idkhoithi="{khoi}"')
    KQ = ''
    if query:
        KQ = query[0][0]
    return KQ

def gioi_thieu_truong(truong):
    query = exec_query(f'select gioithieu from truong where idtruong="{truong}"')
    KQ = ''
    if query:
        KQ = query[0][0]
    return KQ
def ma_truong(truong):
    query = exec_query(f'select matruong from truong where idtruong="{truong}"')
    KQ = ''
    if query:
        KQ = query[0][0]
    return KQ

def hoc_nganh_nay_o_dau(nganh):
    query = exec_query(f'select t.idtruong, t.tentruong from (nganh_cua_truong n join truong t on n.idtruong = t.idtruong) where n.idnganh="{nganh}"')
    ket_qua = []
    for d in query:
        ket_qua.append(d[1])
    return ket_qua

def khoi_thi_cua_nganh(nganh):
    query = exec_query(f'SELECT kt.idkhoithi, kt.thongtin FROM '
    '(chabot.khoi_thi kt join chabot.khoi_thi_nganh ktn on kt.idKhoiThi = ktn.idKhoiThi)'
    f'where ktn.idmanganh = "{nganh}";')
    result = ''
    for q in query:
        result += f'\nKhối thi {q[0]}: {q[1]}'
    return result
    
def truong_phu_hop(nganh, nam, diem):
    query = exec_query(f'select idtruong from nganh_cua_truong where idnganh="{nganh}" and nam={nam} and diem<={diem}')
    ket_qua = []
    for d in query:
        ket_qua.append(d[0])
    return ket_qua

def diem_chuan_nganh_cua_truong(truong,nganh):
    query = exec_query(f"SELECT NAM, DIEM, chitieu FROM chabot.nganh_cua_truong WHERE IDNGANH='{nganh}' AND IDTRUONG ='{truong}'")
    ket_qua = ''
    for d in query:
        ket_qua += f'\nNăm: {d[0]} - Điểm chuẩn: {d[1]} - Chỉ tiêu: {d[2]} Sinh viên'
    return ket_qua
def diem_chuan_truong(truong, nam):
    dct = exec_query(f'select tennganh, diem, CHITIEU from (chabot.nganh_cua_truong nct join chabot.nganh n on n.idNganh= nct.idNganh) where idtruong="{truong}" and nam ={nam}')
    ket_qua = ''
    for d in dct:
        ket_qua += f'\nTên ngành: {d[0]} - Điểm chuẩn: {d[1]} - Chỉ tiêu: {d[2]} sinh viên'
    return ket_qua

def ds_nganh():
    ds = exec_query('select idnganh from nganh')
    ket_qua = []
    for nganh in ds:
        ket_qua.append(nganh[0])
    return ket_qua
def ds_truong():
    ds = exec_query('select idtruong from truong')
    ket_qua = []
    for nganh in ds:
        ket_qua.append(nganh[0])
    return ket_qua

def hinh_thuc_xt(truong):
    results = exec_query(f'select htxt from hinh_thuc_xet_tuyen where idtruong = "{truong}"')
    ketqua =''
    if results:
        ketqua = results[0][0]
    return ketqua

def hoc_bong(truong):
    results = exec_query(f'select hocbong from hinh_thuc_xet_tuyen where idtruong = "{truong}"')
    ketqua =''
    if results:
        ketqua = results[0][0]
    return ketqua

def hoc_phi(truong, nam):
    results = exec_query(f'select hocphi from hinh_thuc_xet_tuyen where idtruong = "{truong}" and nam = {nam}')
    ketqua =''
    if results:
        ketqua = results[0][0]
    return ketqua

def ten_nganh(nganh):
    #cursor = conn.cursor()
    # Thực hiện truy vấn SQL
    conn = mySql()
    cursor = conn.cursor()
    query = f"SELECT tennganh FROM nganh where idnganh = '{nganh}'"
    cursor.execute(query)
    # Lấy kết quả
    results = cursor.fetchall()
    conn.close()
    ketqua =''
    if results:
        ketqua = results[0][0]
    return ketqua

def ten_truong(truong):
    conn = mySql()
    cursor = conn.cursor()
    query = f"SELECT tentruong FROM truong where idtruong = '{truong}'"
    cursor.execute(query)
    # Lấy kết quả
    results = cursor.fetchall()
    conn.close()
    ketqua =''
    if results:
        ketqua = results[0][0]
    return ketqua

def khu_vuc_cua_truong(truong):
    results = exec_query(f'SELECT idkhuvuc FROM khu_vuc_cua_truong where idtruong = "{truong}"')
    ketqua =''
    if results:
        ketqua = results[0][0]
    return ketqua

#
def gioi_thieu_nganh(nganh):
    results = exec_query(f"SELECT gioithieu FROM nganh where idnganh = '{nganh}'")
    ketqua =''
    if results:
        ketqua = results[0][0]
    return ketqua


#conn.close()
#data_nganh = ["cntt", 'attt', 'khmt', 'dt',' iot', 'qtkd', 'ktpm', 'httt', 'mmt', 'ck', 'vt', 'mt', 'ttnt']
data_nganh = ds_nganh()
#data_truong = ['ptit2', 'ptit1', 'bkhcm', 'bkhn', 'spkt', 'qghn', 'dh_cntt', 'khtn_hcm']
data_truong = ds_truong()
#ma_truong = {data_truong[0]: {'BVS'},data_truong[1]:{'BVH'},data_truong[2]: {'QSB'},data_truong[3]: {'BKA'},data_truong[4]: {'SPK'},data_truong[5]:{"QHT"},data_truong[6]:'DTC',data_truong[7]: 'QST'}
danh_sach_truong = {
    data_truong[0]:"Học Viện Công Nghệ Bưu Chính Viễn Thông TP.HCM",
    data_truong[1]:"Học Viện Công Nghệ Bưu Chính Viễn Thông Hà Nội" , 
    data_truong[2]:"Đại Học Bách Khoa TP. Hồ Chí Minh", 
    data_truong[3]:"Đại Học Bách Khoa Hà Nội",
    data_truong[4]:"Đại Học Sư Phạm Kỹ Thuật",
    data_truong[5]: "Đại học khoa học tự nhiên - Đại học Quốc gia Hà Nội",
    data_truong[6]: "Đại học Công nghệ thông tin",
    data_truong[7]: "Đại học khoa học tự nhiên TP. Hồ Chí Minh"}
khu_vuc_hn ={data_truong[1], data_truong[3], data_truong[5]}
khu_vuc_hcm ={data_truong[0], data_truong[2], data_truong[4], data_truong[6], data_truong[7]}

danh_sach_nganh = {
    data_nganh[0]:"Công nghệ thông tin", 
    data_nganh[1]:"An toàn thông tin", 
    data_nganh[2]:"Khoa học máy tính", 
    data_nganh[3]:"Điện - Điện tử",
    data_nganh[4]:"Internet vạn vật",
    data_nganh[5]:"Quản trị kinh doanh",
    data_nganh[6]:"Kỹ thuật phần mềm",
    data_nganh[7]:"Hệ thống thông tin",
    data_nganh[8]:"Mạng máy tính và truyền thông dữ liệu",
    data_nganh[9]:"Cơ khí",
    data_nganh[10]:"Viễn thông",
    data_nganh[11]:"Môi trường",
    data_nganh[12]:"Trí tuệ nhân tạo",
    
    }

def nganh_cua_truong(truong):
    conn = mySql()
    cursor = conn.cursor()
    query = f"SELECT idnganh FROM nganh_cua_truong where idtruong = '{truong}'"
    cursor.execute(query)
    results = cursor.fetchall()
    nct = []
    for row in results:
        nct.append(row[0])
    conn.close()
    return nct
#nganh_cua_truong('ptit2')
# nganh_cua_truong = {
#     data_truong[0]: {data_nganh[0], data_nganh[1], data_nganh[3], data_nganh[4], data_nganh[5]},
#     data_truong[1]: {data_nganh[0], data_nganh[1], data_nganh[3], data_nganh[4], data_nganh[5]},
#     data_truong[2]: {data_nganh[2], data_nganh[3]},
#     data_truong[3]: {data_nganh[0], data_nganh[3]},
#     data_truong[4]: {data_nganh[0], data_nganh[3], data_nganh[11], data_nganh[9]},
#     data_truong[5]: {data_nganh[0], data_nganh[11]},
#     data_truong[6]: {data_nganh[1], data_nganh[6], data_nganh[7], data_nganh[8]},
# }
random_truong = random.sample(data_truong, len(data_truong))

buttons_random_truong = [
            {
                "title": danh_sach_truong[random_truong[0]],
                "payload": danh_sach_truong[random_truong[0]]
            },
            {
                "title": danh_sach_truong[random_truong[1]],
                "payload": danh_sach_truong[random_truong[1]]
            },
            {
                "title": danh_sach_truong[random_truong[2]],
                "payload": danh_sach_truong[random_truong[2]]
            }]
random_nganh = random.sample(data_nganh, len(data_nganh))
buttons_random_nganh = [
            {
                "title": danh_sach_nganh[random_nganh[0]],
                "payload": danh_sach_nganh[random_nganh[0]]
            },
            {
                "title": danh_sach_nganh[random_nganh[1]],
                "payload": danh_sach_nganh[random_nganh[1]]
            },
            {
                "title": danh_sach_nganh[random_nganh[2]],
                "payload": danh_sach_nganh[random_nganh[2]]
            }]
truong_phu_hop_theo_nganh = {
    data_nganh[0]: [danh_sach_truong[data_truong[0]], danh_sach_truong[data_truong[1]], danh_sach_truong[data_truong[2]]],
    data_nganh[1]: [danh_sach_truong[data_truong[0]], danh_sach_truong[data_truong[1]], danh_sach_truong[data_truong[2]]]

}





khoi_thi = {
    "A00": "Toán, Vật lý, Hóa học",
    "A01": "Toán, Vật lý, Tiếng Anh",
    "A02": "Toán, Vật lí , Sinh học",
    "A03": "Toán, Vật lý, Lịch sử",
    "A04": "Toán, Vật lý, Địa lí",
    "A05": "Toán, Hóa học, Lịch sử",
    "A06": "Toán, Hóa học, Địa lí",
    "A07": "Toán, Lịch sử, Địa lí",
    "A08": "Toán, Lịch sử, Giáo dục công dân",
    "A09": "Toán, Địa lí, Giáo dục công dân",
    "A10": "Toán, Vật lý, Giáo dục công dân",
    "A11": "Toán, Hóa học, Giáo dục công dân",
    "A12": "Toán, Khoa học tự nhiên, Khoa học xã hội",
    "A14": "Toán, Khoa học tự nhiên, Địa lí",
    "A15": "Toán, Khoa học tự nhiên, Giáo dục công dân",
    "A16": "Toán, Khoa học tự nhiên, Văn",
    "A17": "Toán, Khoa học xã hội, Vật lý",
    "A18": "Toán, Khoa học xã hội, Hóa học",
    "D01": "Văn, Toán, tiếng Anh",
    "D02": "Văn, Toán, tiếng Nga",
    "D03": "Văn, Toán, tiếng Pháp",
    "D04": "Văn, Toán, tiếng Trung",
    "D05": "Văn, Toán, Tiếng Đức",
    "D06": "Văn, Toán, Tiếng Nhật",
    "D07": "Toán, Hóa học, Tiếng Anh",
}



ky_thi_nang_luc_hn = [
('''Kỳ thi Đánh giá năng lực ĐHQG Hà Nội là kỳ thi được tổ chức bởi ĐHQG Hà Nội nhằm đánh giá năng lực cơ bản để học đại học của thí sinh như sử dụng ngôn ngữ; tư duy logic, sử dụng dữ liệu; giải quyết vấn đề.
Kỳ thi được nhiều trường đại học sử dụng kết quả để xét tuyển vì đem lại nguồn đầu vào chất lượng và đánh giá được tổng quan được năng lực của thí sinh, tránh tình trạng học lệch, học tủ.
'''),
('''
Cấu trúc đề thi
Bài thi ĐGNL của ĐHQG-HN được xây dựng dựa trên cách tiếp cận với các bài thi năng lực nổi tiếng trên thế giới.
bài thi đánh giá năng lực ĐHQG Hà Nội gồm 03 phần:
Phần 1: Ngôn ngữ _tiếng Việt, tiếng Anh (40 câu)
Phần 2: Toán học, tư duy logic, phân tích số liệu (30 câu)
Phần 3: Giải quyết vấn đề (50 câu)
Về hình thức: Bài thi gồm 120 câu hỏi trắc nghiệm khách quan đa lựa chọn trong thời gian làm bài là 150 phút.
Về nội dung: Bài thi không đánh giá khả năng học thuộc lòng mà cung cấp số liệu, dữ kiện và các công thức cơ bản nhằm đánh giá và suy luận vấn đề, cách tiếp cận được xây dựng như các đề thi SAT (Scholastic Assessment Test) của Hoa kỳ và đề thi TSA (Thinking Skills Assessment) của Anh.
'''),
('''
Để đăng ký dự thi và xét tuyển ĐGNL của ĐHQG-HN thí sinh đăng ký trực tuyến
tại trang thông tin điện tử của kỳ thi tại địa chỉ: https://khaothi.vnu.edu.vn/.
'''),
(
    '\n6 đợt thi Đánh giá tư duy 2024'
    '\n Thời gian tổ chức thi TSA dự kiến diễn ra vào các ngày Thứ Bảy/Chủ Nhật:'
    '\n- Đợt 1: Ngày 2 - 3/12/2023;'
    '\n- Đợt 2: Ngày 20 - 21/1/2024;'
    '\n- Đợt 3: Ngày 9 - 10/3/2024;'
    '\n- Đợt 4: Ngày 27 - 28/4/2024;'
    '\n- Đợt 5: Ngày 8 - 9/6/2024;'
    '\n- Đợt 6: Ngày 15 - 16/6/2024.'
)
]
ky_thi_nang_luc_hcm = [('''Kỳ thi Đánh giá năng lực ĐHQG TP.Hồ Chí Minh là kỳ thi được tổ chức bởi ĐHQG TP.Hồ Chí Minh nhằm đánh giá năng lực cơ bản để học đại học của thí sinh như sử dụng ngôn ngữ; tư duy logic, sử dụng dữ liệu; giải quyết vấn đề.
Kỳ thi được nhiều trường đại học sử dụng kết quả để xét tuyển vì đem lại nguồn đầu vào chất lượng và đánh giá được tổng quan được năng lực của thí sinh, tránh tình trạng học lệch, học tủ.
'''),
('''
Cấu trúc đề thi
Bài thi ĐGNL của ĐHQG-HCM được xây dựng dựa trên cách tiếp cận với các bài thi năng lực nổi tiếng trên thế giới.
Bài thi đánh giá năng lực ĐHQG TP.Hồ Chí Minh gồm 03 phần:
Phần 1: Ngôn ngữ _tiếng Việt, tiếng Anh (40 câu)
Phần 2: Toán học, tư duy logic, phân tích số liệu (30 câu)
Phần 3: Giải quyết vấn đề (50 câu)
Về hình thức: Bài thi gồm 120 câu hỏi trắc nghiệm khách quan đa lựa chọn trong thời gian làm bài là 150 phút.
Về nội dung: Bài thi không đánh giá khả năng học thuộc lòng mà cung cấp số liệu, dữ kiện và các công thức cơ bản nhằm đánh giá và suy luận vấn đề, cách tiếp cận được xây dựng như các đề thi SAT (Scholastic Assessment Test) của Hoa kỳ và đề thi TSA (Thinking Skills Assessment) của Anh.
'''),
('''
Để đăng ký dự thi và xét tuyển ĐGNL của ĐHQG-HCM, thí sinh đăng ký trực tuyến
tại trang thông tin điện tử của kỳ thi tại địa chỉ: http://thinangluc.vnuhcm.edu.vn.
'''),
('''
– Các mốc thời gian của kỳ thi ĐGNL năm 2023:
Đợt thi	Thời gian	Nội dung
Đợt 1
01/02/2023	Mở đăng ký dự thi ĐGNL đợt 1
Đợt 2
05/04/2023	Mở đăng ký dự thi ĐGNL đợt 2 và đăng ký xét tuyển
''')

]
    



tt_thi_nang_luc_cua_cac_truong = {
    data_truong[0]: {'''Bạn có thể tham gia vào kỳ thi đánh giá năng lực của Đại học quốc gia Hà Nội và Đại học quốc gia Tp. Hồ Chí Minh để lấy điểm xét tuyển vào trường với điều kiện:
Thí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Hà Nội năm 2023 từ 80 điểm trở lên;
Thí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Tp. Hồ Chí Minh năm 2023 từ 700 điểm trở lên;
Thí sinh có điểm thi đánh giá tư duy của Đại học Bách khoa Hà Nội năm 2023 từ 60 điểm trở lên.'''},
    data_truong[1]: {'''Bạn có thể tham gia vào kỳ thi đánh giá năng lực của Đại học quốc gia Hà Nội và Đại học quốc gia Tp. Hồ Chí Minh để lấy điểm xét tuyển vào trường với điều kiện:
Thí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Hà Nội năm 2023 từ 80 điểm trở lên;
Thí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Tp. Hồ Chí Minh năm 2023 từ 700 điểm trở lên;
Thí sinh có điểm thi đánh giá tư duy của Đại học Bách khoa Hà Nội năm 2023 từ 60 điểm trở lên.'''},
    data_truong[2]: {ky_thi_nang_luc_hcm[0] + ky_thi_nang_luc_hcm[1] + ky_thi_nang_luc_hcm[2] + ky_thi_nang_luc_hcm[3]},
    data_truong[3]: {
    '\n6 đợt thi Đánh giá tư duy 2024'
    '\n Thời gian tổ chức thi TSA dự kiến diễn ra vào các ngày Thứ Bảy/Chủ Nhật:'
    '\n- Đợt 1: Ngày 2 - 3/12/2023;'
    '\n- Đợt 2: Ngày 20 - 21/1/2024;'
    '\n- Đợt 3: Ngày 9 - 10/3/2024;'
    '\n- Đợt 4: Ngày 27 - 28/4/2024;'
    '\n- Đợt 5: Ngày 8 - 9/6/2024;'
    '\n- Đợt 6: Ngày 15 - 16/6/2024.'
    '\nĐịa điểm thi: Hà Nội, Hưng Yên, Nam Định, Hải Phòng, Thái Nguyên, Thanh Hóa, Nghệ An, Đà Nẵng…'   
    '\nNội dung và hình thức thi: Giữ nguyên như năm 2023' 
    '\nBài thi Đánh giá tư duy năm 2023 gồm ba phần: Tư duy Toán học (60 phút), Tư duy Đọc hiểu (30 phút) và Tư duy Khoa học/Giải quyết vấn đề (60 phút) với ba mức độ đánh giá tư duy (tư duy tái hiện, tư duy suy luận và tư duy bậc cao).'
    '\nCác câu hỏi được xây dựng dưới hình thức trắc nghiệm với bốn dạng cấu trúc: Chọn đáp án đúng, đúng/sai, kéo thả và câu trả lời ngắn.'
    '\nKhác với các kỳ thi khác, kỳ thi TSA không tập trung kiểm tra kiến thức nên không đòi hỏi thí sinh dành thời gian ôn luyện nhiều, bởi rèn luyện tư duy đã được hình thành trong suốt quá trình học.'
    '\nNăm 2023, kỳ thi TSA được đánh giá có nhiều điểm thuận lợi cho quá trình làm bài thi của học sinh. Bài thi được điều chỉnh gọn nhẹ (thời lượng 150 phút) và tổ chức theo hình thức trắc nghiệm trên máy tính.'
    '\nCác ngành tuyển sinh đại học có thể sử dụng kết quả kỳ thi TSA được mở rộng, bao gồm Khoa học công nghệ, Kinh tế, Kỹ thuật, Công nghiệp, Nông nghiệp, Tài chính, Ngân hàng, Y dược.'
    '\nTheo Hust.edu.vn   '},
    data_truong[4]: {ky_thi_nang_luc_hcm[0] + ky_thi_nang_luc_hcm[1] + ky_thi_nang_luc_hcm[2] + ky_thi_nang_luc_hcm[3]},
    data_truong[5]: {ky_thi_nang_luc_hn[0]+ ky_thi_nang_luc_hn[1]+ ky_thi_nang_luc_hn[2]+ ky_thi_nang_luc_hn[3]},
    data_truong[6]:{ky_thi_nang_luc_hcm[0] + ky_thi_nang_luc_hcm[1] + ky_thi_nang_luc_hcm[2] + ky_thi_nang_luc_hcm[3]}
}



nganh_de_xuat = {
    "máy tính": ["Công nghệ thông tin", "Khoa học máy tính", "An toàn thông tin"],
    "điện tử": ["Kỹ thuật điện tử", "Kỹ thuật viễn thông"],
    "an toàn thông tin": ["An toàn thông tin", "Công nghệ thông tin"],
    "sư phạm": ["Giáo dục", "Sư phạm"],
}


diem_nganh_truong_nam = {
    "2023": {
        data_truong[0]: {
            data_nganh[0]: 27,
            data_nganh[1]: 26,
            data_nganh[2]: 25
        },
        data_truong[1]: {
            data_nganh[0]: 28,
            data_nganh[1]: 27,
            data_nganh[2]: 26
        },
        data_truong[2]: {
            data_nganh[0]: 28,
            data_nganh[1]: 27,
            data_nganh[2]: 26
        },
        data_truong[3]: {
            data_nganh[0]: 29,
            data_nganh[1]: 28,
            data_nganh[2]: 27
        },
        data_truong[4]: {
            data_nganh[0]: 26.9,
            data_nganh[1]: 27.5,
            data_nganh[2]: 28,
            data_nganh[4]: 25.8,
            data_nganh[3]: 25.38	
        },
        data_truong[5]: {

        },
        data_truong[6]: {
            data_nganh[2]: 27.3,
            data_nganh[0]: 27.3,
            data_nganh[1]: 27,
            data_nganh[8]: 26.35,
            data_nganh[7]: 26.7,
        },
        data_truong[7]: {
            data_nganh[11]: 17,
            data_nganh[0]: 26.5,
            data_nganh[2]: 28.05,
            data_nganh[12]: 27,
            data_nganh[10]: 24.55,
            data_nganh[6]: 24.2
        },

    },
    "2022":
    {
        data_truong[0]: {
            data_nganh[0]: 28,
            data_nganh[1]: 27,
            data_nganh[2]: 26
        },
        data_truong[1]: {
            data_nganh[0]: 29,
            data_nganh[1]: 28,
            data_nganh[2]: 27
        },
        data_truong[2]: {
            data_nganh[0]: 29,
            data_nganh[1]: 25,
            data_nganh[2]: 27
        },
        data_truong[3]: {
            data_nganh[0]: 28.5,
            data_nganh[1]: 27.5,
            data_nganh[2]: 28
        },
        data_truong[4]: {
            data_nganh[0]: 26.9,
            data_nganh[1]: 27.5,
            data_nganh[2]: 28,
            data_nganh[4]: 25.8,
            data_nganh[3]: 25.38	
        },
        data_truong[5]: {

        },
        data_truong[6]: {
            data_nganh[2]: 27.3,
            data_nganh[0]: 27.3,
            data_nganh[1]: 27,
            data_nganh[8]: 26.35,
            data_nganh[7]: 26.7,
        },
        data_truong[7]: {
            data_nganh[11]: 17,
            data_nganh[0]: 26.5,
            data_nganh[2]: 28.05,
            data_nganh[12]: 27,
            data_nganh[10]: 24.55,
            data_nganh[6]: 24.2
        },
    },
    "2021": {

    }
}

# lam o dâywdyaywdiaywiyhawdhiuaw
diem_chuan = {
    "2023": { 
        data_truong[0]: {
            '\n- Kỹ thuật Điều khiển và tự động hóa: 18.00 '
            '\n- Công nghệ Kỹ thuật Điện, điện tử: 18.15'
            '\n- Kế toán: 20.00'
            '\n- Công nghệ Inernet vạn vật: 21.70'
            '\n- ...'}, 
        data_truong[1]: {
            '\nCông nghệ thông tin: 26.59'
            '\nAn toàn thông tin: 26.04'
            '\nKhoa học máy tính (định hướng Khoa học dữ liệu): 26.55'
            '\nCông nghệ đa phương tiện: 25.89'
            '\nCông nghệ thông tin (CLC): 25.38'
            '\nQuản trị kinh doanh: ''25.15'},
        data_truong[2]: {
            'STT	Mã tuyển sinh	Tên chương trình đào tạo	Tổ hợp	Điểm chuẩn'
            '\n1	BF1 	Kỹ thuật Sinh học	A00; B00; D07	24.60'
            '\n2	BF2 	Kỹ thuật Thực phẩm	A00; B00; D07	24.49'
            '\n3	BF-E12	Kỹ thuật Thực phẩm (CT tiên tiến)	A00; B00; D07	22.70'
            '\n4	BF-E19	Kỹ thuật sinh học (CT tiên tiến)	A00; B00; D07	21.00'
            '\n5	CH1 	Kỹ thuật Hóa học	A00; B00; D07	23.70'
            '\n6	CH2 	Hóa học	A00; B00; D07	23.04'
            '\n7	CH3 	Kỹ thuật In	A00; A01; D07	22.70'
            '\n8	CH-E11	Kỹ thuật Hóa dược (CT tiên tiến)	A00; B00; D07	23.44'
            '\n9	ED2 	Công nghệ Giáo dục	A00; A01; D01	24.55'
            '\n10	EE1 	Kỹ thuật điện	A00; A01	25.55'
            '\n11	EE2 	Kỹ thuật điều khiển & Tự động hóa	A00; A01	27.57'
            '\n12	EE-E18	Hệ thống điện và năng lượng tái tạo (CT tiên tiến)	A00; A01	24.47'
            '\n13	EE-E8	Kỹ thuật Điều khiển - Tự động hoá (CT tiên tiến)	A00; A01	26.74'
            '\n14	EE-EP	Tin học công nghiệp và Tự động hóa (Chương trình Việt - Pháp PFIEV)	A00; A01; D29	25.14'
}, 
            data_truong[3]: ('STT	Mã tuyển sinh	Tên chương trình đào tạo	Tổ hợp	Điểm chuẩn'
            '\n1	BF1 	Kỹ thuật Sinh học	A00; B00; D07	24.60'
            '\n2	BF2 	Kỹ thuật Thực phẩm	A00; B00; D07	24.49'
            '\n3	BF-E12	Kỹ thuật Thực phẩm (CT tiên tiến)	A00; B00; D07	22.70'
            '\n4	BF-E19	Kỹ thuật sinh học (CT tiên tiến)	A00; B00; D07	21.00'
            '\n5	CH1 	Kỹ thuật Hóa học	A00; B00; D07	23.70'
            '\n6	CH2 	Hóa học	A00; B00; D07	23.04'
            '\n7	CH3 	Kỹ thuật In	A00; A01; D07	22.70'
            '\n8	CH-E11	Kỹ thuật Hóa dược (CT tiên tiến)	A00; B00; D07	23.44'
            '\n9	ED2 	Công nghệ Giáo dục	A00; A01; D01	24.55'),
            data_truong[4]: (
                f'{danh_sach_nganh[data_nganh[4]]}: '
            )
        },
    "2022": {
            data_truong[0]:{},
            data_truong[1]: {'''Học viện Công nghệ Bưu chính Viễn thông thông báo điểm chuẩn trúng tuyển năm 2022. Dưới đây là mức điểm chuẩn trúng tuyển vào các ngành học:

Kỹ thuật Điện tử viễn thông: 25.60 điểm (TTNV <= 3).
Công nghệ kỹ thuật Điện, điện tử: 25.10 điểm (TTNV <= 2).
Công nghệ thông tin: 27.25 điểm (TTNV = 1).
An toàn thông tin: 26.70 điểm (TTNV <= 3).
Khoa học máy tính: 26.90 điểm (TTNV <= 2).
Công nghệ đa phương tiện: 26.45 điểm (TTNV <= 3).
Truyền thông đa phương tiện: 26.20 điểm (TTNV = 1).
Báo chí: 24.40 điểm (TTNV <= 3).
Quản trị kinh doanh: 25.55 điểm (TTNV = 1).
Thương mại điện tử: 26.35 điểm (TTNV <= 3).
Marketing: 26.10 điểm (TTNV <= 2).
Kế toán: 25.35 điểm (TTNV <= 8).'''},
            data_truong[2]: {''''''}
            

        }}

chi_tiet_nganh = {
    "2023": {
        data_truong[0]: {
            data_nganh[0]:(
                '''Ngành Công nghệ thông tin (gồm có 4 chuyên ngành Máy tính và truyền thông, Khoa học máy tính, Kỹ thuật máy tính, Hệ thống thông tin, không xét tuyển theo chuyên ngành, khi vào học sinh viên tự chọn chuyên ngành)'
                1. Mã ngành: 7480201
                2. Khối lượng chương trình: 150 tín chỉ (không bao gồm Giáo dục thể chất, Giáo dục quốc phòng và Kỹ năng mềm)
                3. Chi tiêu:
                - Năm 2023: Chỉ tiêu theo KQ thi THPT là 110 SV - Chỉ tiêu theo PT kết hợp là 60 SV - Chỉ tiêu theo kết quả ĐGNL, ĐGTD là 30 SV '
                - Năm 2022: 840
                - Năm 2021: 770'''
                '4. Điểm trúng tuyển:'
                '\n- Năm 2023: 25,1'
                '\n- Năm 2022: 27,25'
                '\n- Năm 2021: 26,90'
                '\n5. Tổ hợp xét tuyển: Toán – Lý – Hóa (A00) hoặc Toán – Lý – Anh (A01) '
                '\n6. Nguyện vọng: <=10 ',
            ),
            data_nganh[1]: ('\n1. Mã ngành: 7480202'
                '\n2. Khối lượng chương trình: 150 tín chỉ (không bao gồm Giáo dục thể chất, Giáo dục quốc phòng và Kỹ năng mềm)'
                '\n3. Chi tiêu:'
                '\n- Năm 2023: Chỉ tiêu theo KQ thi THPT : 40 SV'
                '\n            Chỉ tiêu theo PT kết hợp: 20 SV'
                '\n            Chỉ tiêu theo kết quả ĐGNL, ĐGTD: 10 SV'
                '\n- Năm 2022: 60'
                '\n- Năm 2021: 70'
                '\n4. Điểm trúng tuyển:'
                '\n- Năm 2022: 26,70'
                '\n- Năm 2021: 26,55'
                '\n5. Tổ hợp xét tuyển: Toán – Lý – Hóa (A00) hoặc Toán – Lý – Anh (A01)'),
        data_truong[1]: {
            data_nganh[0]: (
            '''Ngành Công nghệ thông tin (gồm có 4 chuyên ngành Máy tính và truyền thông, Khoa học máy tính, Kỹ thuật máy tính, Hệ thống thông tin, không xét tuyển theo chuyên ngành, khi vào học sinh viên tự chọn chuyên ngành)'
            '''# 1. Mã ngành: 7480201
            # 2. Khối lượng chương trình: 150 tín chỉ (không bao gồm Giáo dục thể chất, Giáo dục quốc phòng và Kỹ năng mềm)
            # 3. Chi tiêu:
            # '\n- Năm 2023: 730'
            # '\n- Năm 2022: 840'
            # '\n- Năm 2021: 770'
            # '\n4. Điểm trúng tuyển:'
            # '\n- Năm 2023: 25,1'
            # '\n- Năm 2022: 27,25'
            # '\n- Năm 2021: 26,90'
            # '\n5. Tổ hợp xét tuyển: Toán – Lý – Hóa (A00) hoặc Toán – Lý – Anh (A01) '
            # '\n6. Nguyện vọng: <=10 ',

            # '\n1. Mã ngành: 7480202'
            # '\n2. Khối lượng chương trình: 150 tín chỉ (không bao gồm Giáo dục thể chất, Giáo dục quốc phòng và Kỹ năng mềm)'
            # '\n3. Chi tiêu:'
            # '\n- Năm 2023: '
            # '\n- Năm 2022: 240'
            # '\n- Năm 2021: 220'
            # '\n4. Điểm trúng tuyển:'
            # '\n- Năm 2022: 26,70'
            # '\n- Năm 2021: 26,55'
            # '\n5. Tổ hợp xét tuyển: Toán – Lý – Hóa (A00) hoặc Toán – Lý – Anh (A01)',

            # 'Ngành Quản trị kinh doanh (gồm có 3 chuyên ngành Quản trị Marketing, Thương mại điện tử, Quản trị doanh nghiệp, không xét tuyển theo chuyên ngành, khi vào học sinh viên tự chọn chuyên ngành)'
            # '\n1. Mã ngành: 7340101'
            # '\n2. Khối lượng chương trình: 130 tín chỉ (không bao gồm Giáo dục thể chất, Giáo dục quốc phòng và Kỹ năng mềm)''3. Chi tiêu'
            # '\n- Năm 2023:'
            # '\n- Năm 2022: 190'
            # '\n- Năm 2021: 175'
            # '\n4. Điểm trúng tuyển:'
            # '\n- Năm 2022: 25,55'
            # '\n- Năm 2021: 25,9'
            # '\n5. Tổ hợp xét tuyển: Toán – Lý – Hóa (A00) hoặc Toán – Lý – Anh (A01) hoặc Toán - Văn - Anh (D01)',

            # '\nChỉ tiêu theo KQ thi THPT : 40 SV'
            # '\nChỉ tiêu theo PT kết hợp: 20 SV'
            # '\nChỉ tiêu theo kết quả ĐGNL, ĐGTD: 15 SV'
            # '\nMã ngành: 7520208'
            ),
            data_nganh[1]: ()


        },
        data_truong[2]: [],
        "bkhcm": [],
        data_truong[7]: {
            data_nganh[2]: ('''Mã ngành: 7480101
Tên ngành: Khoa học máy tính
Chỉ tiêu 2023: 270
Tổ hợp môn xét tuyển: A00, A01, D01, D07'''),
        
            data_nganh[12]: ('''Mã ngành: 7480107
Tên ngành: Trí tuệ nhân tạo
Chỉ tiêu 2023: 40
Tổ hợp môn xét tuyển: A00, A01, D01, D07'''),
            data_nganh[8]: ('''Mã ngành: 7480102
Tên ngành: Mạng máy tính và truyền thông dữ liệu
Chỉ tiêu 2023: 200
Tổ hợp môn xét tuyển: A00, A01, D01, D07'''),
            data_nganh[6]:('''Mã ngành: 7480103
Tên ngành: Kỹ thuật phần mềm
Chỉ tiêu 2023: 225
Tổ hợp môn xét tuyển: A00, A01, D01, D07'''),
            data_nganh[7]: ('''Mã ngành: 7480104
Tên ngành: Hệ thống thông tin
Chỉ tiêu 2023: 175
Tổ hợp môn xét tuyển: A00, A01, D01, D07'''),
            data_nganh[0]: ('''Mã ngành: 7480201
Tên ngành: Công nghệ thông tin
Chỉ tiêu 2023: 115
Tổ hợp môn xét tuyển: A00, A01, D01, D07'''),
            data_nganh[1]: ('''Mã ngành: 7480202
Tên ngành: An toàn thông tin
Chỉ tiêu 2023: 160
Tổ hợp môn xét tuyển: A00, A01, D01, D07''')
},
        }
    }
}
tuyen_sinh_cua_truong_short = {
    #ptit2
    "ptit2":(
        '''
PHƯƠNG ÁN XÉT TUYỂN
Đại học hệ chính quy năm 2023
    Phương thức 1
        Xét tuyển thẳng và ưu tiên xét tuyển: Học viện thực hiện xét tuyển thẳng và ưu tiên xét tuyển theo Quy chế tuyển sinh đại học của Bộ Giáo dục và Đào tạo (có thông báo chi tiết riêng)
    Phương thức 2
        Phương thức xét tuyển dựa vào kết quả thi tốt nghiệp THPT năm 2023
            Xét tuyển theo ngành và theo tổ hợp bài thi/môn thi xét tuyển;
            Điểm trúng tuyển của các tổ hợp bài thi/môn thi trong cùng một ngành là bằng nhau (không có điểm chênh lệch giữa các tổ hợp trong cùng một ngành);
            Xét trúng tuyển từ thí sinh có kết quả cao xuống và đảm bảo chất lượng tuyển sinh;
            '''
            # Xét tuyển các nguyện vọng bình đẳng (không có điểm chênh lệch giữa các nguyện vọng trong cùng một ngành), nếu thí sinh không trúng tuyển nguyện vọng ở thứ tự ưu tiên thứ nhất (nguyện vọng 1) thì sẽ được tự động xét tuyển ở nguyện vọng ưu tiên thứ hai (nguyện vọng 2) và kế tiếp;
            # Thí sinh chỉ trúng tuyển vào 1 nguyện vọng ưu tiên cao nhất trong danh sách các nguyện vọng đã đăng ký, khi đã trúng tuyển ở nguyện vọng nào thì không được xét tuyển tiếp ở nguyện vọng sau;
            # Điểm trúng tuyển được tính theo thang điểm 10 trên tổng điểm tối đa của 3 môn thi trong tổ hợp xét tuyển là 30 điểm;
            # Đối với các thí sinh bằng điểm xét tuyển ở cuối danh sách, nếu vẫn còn vượt chỉ tiêu thì ưu tiên thí sinh có nguyện vọng cao hơn theo Quy chế tuyển sinh của Bộ Giáo dục & Đào tạo, Học viện không sử dụng tiêu chí phụ riêng để xét tuyển;
            # Thí sinh trúng tuyển phải xác nhận nhập học trong thời gian quy định của Học viện. Nếu quá thời hạn này, thí sinh không xác nhận nhập học được xem là từ chối nhập học.
            # Các điều kiện khác thực hiện theo Quy chế tuyển sinh đại học hệ chính quy hiện hành của Bộ Giáo dục và Đào tạo và của Học viện.
    '''Phương thức 3
        Xét tuyển kết hợp:
           Thí sinh có Chứng chỉ quốc tế SAT, trong thời hạn 02 năm (tính đến ngày xét tuyển) từ 1130/1600 trở lên hoặc ATC từ 25/36 trở lên; và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 7,5 trở lên và có hạnh kiểm Khá trở lên;
           Thí sinh có Chứng chỉ tiếng Anh quốc tế trong thời hạn (tính đến ngày xét tuyển) đạt IELTS 5.5 trở lên hoặc TOEFL iBT 65 trở lên hoặc TOEFL ITP 513 trở lên; và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 7,5 trở lên và có hạnh kiểm Khá trở lên;
           Thí sinh đạt giải Khuyến khích trong kỳ thi chọn học sinh giỏi quốc gia hoặc đã tham gia kỳ thi chọn học sinh giỏi quốc gia hoặc đạt giải Nhất, Nhì, Ba trong kỳ thi chọn học sinh giỏi cấp Tỉnh, Thành phố trực thuộc Trung ương (TW) các môn Toán, Lý, Hóa, Tin học và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 7,5 trở lên và có hạnh kiểm Khá trở lên.
           Là học sinh chuyên các môn Toán, Lý, Hóa, Tin học của trường THPT chuyên trên phạm vi toàn quốc (các trường THPT chuyên thuộc Tỉnh, Thành phố trực thuộc TW và các trường THPT chuyên thuộc Cơ sở giáo dục đại học) hoặc hệ chuyên thuôc các trường THPT trọng điểm quốc gia; Và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 8,0 trở lên và có hạnh kiểm Khá trở lên.
    Phương thức 4
        Xét tuyển dựa vào kết quả bài thi đánh giá năng lực hoặc đánh giá tư duy
            Thí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Hà Nội năm 2023 từ 80 điểm trở lên;
            Thí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Hồ Chí Minh năm 2023 từ 700 điểm trở lên;
            Thí sinh có điểm thi đánh giá tư duy của Đại học Bách khoa Hà Nội năm 2023 từ 60 điểm trở lên.
    '''
)
    , 
    #ptit1

    data_truong[1]:(

    
        '''PHƯƠNG ÁN XÉT TUYỂN
    Đại học hệ chính quy năm 2023
    Phương thức 1'''
    'Xét tuyển thẳng và ưu tiên xét tuyển: Học viện thực hiện xét tuyển thẳng và ưu tiên xét tuyển theo Quy chế tuyển sinh đại học của Bộ Giáo dục và Đào tạo (có thông báo chi tiết riêng)'
    '\nPhương thức 2'
    '\n    Phương thức xét tuyển dựa vào kết quả thi tốt nghiệp THPT năm 2023'
    '\n       Xét tuyển theo ngành và theo tổ hợp bài thi/môn thi xét tuyển;'
    '\n       Điểm trúng tuyển của các tổ hợp bài thi/môn thi trong cùng một ngành là bằng nhau (không có điểm chênh lệch giữa các tổ hợp trong cùng một ngành);'
    '\n       Xét trúng tuyển từ thí sinh có kết quả cao xuống và đảm bảo chất lượng tuyển sinh;'
    # '\n       Xét tuyển các nguyện vọng bình đẳng (không có điểm chênh lệch giữa các nguyện vọng trong cùng một ngành), nếu thí sinh không trúng tuyển nguyện vọng ở thứ tự ưu tiên thứ nhất (nguyện vọng 1) thì sẽ được tự động xét tuyển ở nguyện vọng ưu tiên thứ hai (nguyện vọng 2) và kế tiếp;'
    # '\n       Thí sinh chỉ trúng tuyển vào 1 nguyện vọng ưu tiên cao nhất trong danh sách các nguyện vọng đã đăng ký, khi đã trúng tuyển ở nguyện vọng nào thì không được xét tuyển tiếp ở nguyện vọng sau;'
    # '\n       Điểm trúng tuyển được tính theo thang điểm 10 trên tổng điểm tối đa của 3 môn thi trong tổ hợp xét tuyển là 30 điểm;'
    # '\n       Đối với các thí sinh bằng điểm xét tuyển ở cuối danh sách, nếu vẫn còn vượt chỉ tiêu thì ưu tiên thí sinh có nguyện vọng cao hơn theo Quy chế tuyển sinh của Bộ Giáo dục & Đào tạo, Học viện không sử dụng tiêu chí phụ riêng để xét tuyển;'
    # '\n       Thí sinh trúng tuyển phải xác nhận nhập học trong thời gian quy định của Học viện. Nếu quá thời hạn này, thí sinh không xác nhận nhập học được xem là từ chối nhập học.'
    # '\n       Các điều kiện khác thực hiện theo Quy chế tuyển sinh đại học hệ chính quy hiện hành của Bộ Giáo dục và Đào tạo và của Học viện.'    
    
'\nPhương thức 3'
'\n   Xét tuyển kết hợp:'

'\n       Thí sinh có Chứng chỉ quốc tế SAT, trong thời hạn 02 năm (tính đến ngày xét tuyển) từ 1130/1600 trở lên hoặc ATC từ 25/36 trở lên; và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 7,5 trở lên và có hạnh kiểm Khá trở lên;'
'\n       Thí sinh có Chứng chỉ tiếng Anh quốc tế trong thời hạn (tính đến ngày xét tuyển) đạt IELTS 5.5 trở lên hoặc TOEFL iBT 65 trở lên hoặc TOEFL ITP 513 trở lên; và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 7,5 trở lên và có hạnh kiểm Khá trở lên;'
'\n       Thí sinh đạt giải Khuyến khích trong kỳ thi chọn học sinh giỏi quốc gia hoặc đã tham gia kỳ thi chọn học sinh giỏi quốc gia hoặc đạt giải Nhất, Nhì, Ba trong kỳ thi chọn học sinh giỏi cấp Tỉnh, Thành phố trực thuộc Trung ương (TW) các môn Toán, Lý, Hóa, Tin học và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 7,5 trở lên và có hạnh kiểm Khá trở lên.'
'\n       Là học sinh chuyên các môn Toán, Lý, Hóa, Tin học của trường THPT chuyên trên phạm vi toàn quốc (các trường THPT chuyên thuộc Tỉnh, Thành phố trực thuộc TW và các trường THPT chuyên thuộc Cơ sở giáo dục đại học) hoặc hệ chuyên thuôc các trường THPT trọng điểm quốc gia; Và có kết quả điểm trung bình chung học tập lớp 10, 11, 12 hoặc học kỳ 1 lớp 12 đạt từ 8,0 trở lên và có hạnh kiểm Khá trở lên.'
   
'\nPhương thức 4'
'   \nXét tuyển dựa vào kết quả bài thi đánh giá năng lực hoặc đánh giá tư duy'

'   \nThí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Hà Nội năm 2023 từ 80 điểm trở lên;'
'   \nThí sinh có điểm thi đánh giá năng lực của Đại học quốc gia Hồ Chí Minh năm 2023 từ 700 điểm trở lên;'
'   \nThí sinh có điểm thi đánh giá tư duy của Đại học Bách khoa Hà Nội năm 2023 từ 60 điểm trở lên.'
), 
    #kbhcm
    
    'bkhcm': (),
    #bkhn
    data_truong[3]:(
    '1. Thông tin chung'
    '\nTổng chỉ tiêu tuyển sinh dự kiến: 7.985 sinh viên'
    '\nGồm 3 phương thức tuyển sinh:'
    '\n1. Phương thức xét tuyển tài năng (XTTN);'
    '\n2. Phương thức xét tuyển dựa theo kết quả Kỳ thi đánh giá tư duy (ĐGTD);'
    '\n3. Phương thức xét tuyển dựa theo kết quả thi tốt nghiệp THPT 2023 (THPT);'
    '\n2. Các phương thức tuyển sinh'
    '\n(1) Xét tuyển tài năng: gồm các phương thức sau:'
    '\n(1.1) Xét tuyển thẳng học sinh giỏi theo quy định của Bộ Giáo dục và Đào tạo;'
    '\n(1.2) Xét tuyển dựa trên các chứng chỉ quốc tế SAT, ACT, A-Level, AP và IB;'
    '\n(1.3) Xét tuyển dựa theo hồ sơ năng lực kết hợp phỏng vấn.'
    '\n1.1. Xét tuyển thẳng theo quy định của Bộ GD&ĐT'
    '\n1.2. Xét tuyển theo chứng chỉ Quốc tế'
    '\n1.3. Xét tuyển theo Hồ sơ năng lực kết hợp phỏng vấn'
    '\n(2) Xét tuyển theo kết quả kỳ thi đánh giá tư duy'
    '\n(3) Xét tuyển dựa trên điểm thi tốt nghiệp THPT 2023'

        )

    }

tuyen_sinh_cua_truong_full = [
    #ptit2
    'PTIT2', 
    #ptit1
    'PTIT1', 
    #bkhn
    ''
    #kbhcm

    ]

gioi_thieu_so_ve_truong = {
    #ptit2
    data_truong[0]: (
        
    'Học viện Công nghệ Bưu chính Viễn thông (PTIT) là một đơn vị sự nghiệp trực thuộc Bộ Thông tin và Truyền thông. Học viện này có thế mạnh về nghiên cứu và đào tạo Đại học, sau Đại học trong lĩnh vực Công nghệ Thông tin và Truyền thông. Học viện cung cấp các chương trình đào tạo về khoa học máy tính, mạng máy tính, truyền thông dữ liệu, công nghệ phần mềm, kỹ thuật máy tính, hệ thống quản lý thông tin, robot và trí tuệ nhân tạo.'
    # '\nNgoài ra, Học viện Công nghệ Bưu chính Viễn thông còn có các chương trình đào tạo khác như đào tạo sau đại học, đào tạo từ xa và các chương trình liên kết với các trường đại học trong và ngoài nước.'
    # '\nSau khi tốt nghiệp, sinh viên có thể làm việc trong các lĩnh vực như bảo mật thông tin, giám sát an ninh mạng, kiểm tra bảo mật và xác thực, quản lý rủi ro an ninh mạng và nghiên cứu phát triển sản phẩm an ninh mạng ' 
    ),#ptit1
    data_truong[1]: (
    'Học viện Công nghệ Bưu chính Viễn thông (PTIT) là một đơn vị sự nghiệp trực thuộc Bộ Thông tin và Truyền thông. Học viện này có thế mạnh về nghiên cứu và đào tạo Đại học, sau Đại học trong lĩnh vực Công nghệ Thông tin và Truyền thông. Học viện cung cấp các chương trình đào tạo về khoa học máy tính, mạng máy tính, truyền thông dữ liệu, công nghệ phần mềm, kỹ thuật máy tính, hệ thống quản lý thông tin, robot và trí tuệ nhân tạo.'
    '\nNgoài ra, Học viện Công nghệ Bưu chính Viễn thông còn có các chương trình đào tạo khác như đào tạo sau đại học, đào tạo từ xa và các chương trình liên kết với các trường đại học trong và ngoài nước.'
    '\nSau khi tốt nghiệp, sinh viên có thể làm việc trong các lĩnh vực như bảo mật thông tin, giám sát an ninh mạng, kiểm tra bảo mật và xác thực, quản lý rủi ro an ninh mạng và nghiên cứu phát triển sản phẩm an ninh mạng '
    ),
    #kbhcm
    data_truong[2]: (
    'Trường Đại học Bách Khoa Thành phố Hồ Chí Minh (HCMUT) là một trường đại học đầu ngành về lĩnh vực kỹ thuật ở miền Nam Việt Nam, có trụ sở tại Thành phố Hồ Chí Minh. Trường cung cấp các chương trình đào tạo về khoa học máy tính, mạng máy tính, truyền thông dữ liệu, công nghệ phần mềm, kỹ thuật máy tính, hệ thống quản lý thông tin, robot và trí tuệ nhân tạo.'
    '\nSau khi tốt nghiệp, sinh viên có thể làm việc trong các lĩnh vực như bảo mật thông tin, giám sát an ninh mạng, kiểm tra bảo mật và xác thực, quản lý rủi ro an ninh mạng và nghiên cứu phát triển sản phẩm an ninh mạng '
    ),
    
    #bkhn
    data_truong[3]: (
    'Trường Đại học Bách Khoa Hà Nội được thành lập vào ngày 06/03/1956 theo lệnh của Bộ trưởng Bộ Giáo dục Nguyễn Văn Huyên. Đây là trường đại học kỹ thuật đầu tiên của Việt Nam có nhiệm vụ đào tạo kỹ sư công nghiệp. Trường cung cấp các chương trình đào tạo về khoa học máy tính, mạng máy tính, truyền thông dữ liệu, công nghệ phần mềm, kỹ thuật máy tính, hệ thống quản lý thông tin, robot và trí tuệ nhân tạo.'
    '\nSau khi tốt nghiệp, sinh viên có thể làm việc trong các lĩnh vực như bảo mật thông tin, giám sát an ninh mạng, kiểm tra bảo mật và xác thực, quản lý rủi ro an ninh mạng và nghiên cứu phát triển sản phẩm an ninh mạng '
    ),
    
    # spkt
    data_truong[4]: (
    'Trường Đại học Sư phạm Kỹ thuật Thành phố Hồ Chí Minh (HCMUTE) là một trường đại học đa ngành tại Việt Nam, với thế mạnh về đào tạo kỹ thuật, được đánh giá là một trong những trường đại học kỹ thuật hàng đầu về đào tạo khối ngành kỹ thuật tại miền Nam. Trường cung cấp các chương trình đào tạo về khoa học máy tính, mạng máy tính, truyền thông dữ liệu, công nghệ phần mềm, kỹ thuật máy tính, hệ thống quản lý thông tin, robot và trí tuệ nhân tạo.'
    '\nNgoài ra, HCMUTE còn có các chương trình đào tạo khác như đào tạo sau đại học, đào tạo từ xa và các chương trình liên kết với các trường đại học trong và ngoài nước.'
    '\nSau khi tốt nghiệp, sinh viên có thể làm việc trong các lĩnh vực như bảo mật thông tin, giám sát an ninh mạng, kiểm tra bảo mật và xác thực, quản lý rủi ro an ninh mạng và nghiên cứu phát triển sản phẩm an ninh mạng.'
    ),

    # dh cntt
    data_truong[5]: (
    'Trường Đại học Công nghệ Thông tin (UIT) là một trung tâm hàng đầu về nghiên cứu khoa học và chuyển giao công nghệ về công nghệ thông tin – truyền thông, được xếp vào nhóm trường đại học trọng điểm quốc gia và là thành viên của Đại học Quốc gia Thành phố Hồ Chí Minh. Trường cung cấp các chương trình đào tạo về khoa học máy tính, mạng máy tính, truyền thông dữ liệu, công nghệ phần mềm, kỹ thuật máy tính, hệ thống quản lý thông tin, robot và trí tuệ nhân tạo.'
    '\nSau khi tốt nghiệp, sinh viên có thể làm việc trong các lĩnh vực như bảo mật thông tin, giám sát an ninh mạng, kiểm tra bảo mật và xác thực, quản lý rủi ro an ninh mạng và nghiên cứu phát triển sản phẩm an ninh mạng.'
    )
}

# gioi_thieu_nganh = {
#     #  0: cntt
#     data_nganh[0]:(
#     '''Ngành Công nghệ thông tin (CNTT) là một lĩnh vực khoa học kỹ thuật sử dụng máy tính và các phần mềm máy tính, mạng lưới internet để lưu trữ, bảo vệ xử lý, trao đổi, thu thập và sử dụng thông tin. Ngành này gồm nhiều chuyên ngành như Khoa học máy tính, Mạng máy tính và truyền thông dữ liệu, Công nghệ phần mềm, Kỹ thuật máy tính, Hệ thống quản lý thông tin, Robot và Trí tuệ nhân tạo.'
#     '''
#     ), # 1 :attt
#     data_nganh[1]:(
#     'An toàn thông tin là một ngành học liên quan đến bảo vệ thông tin khỏi các cuộc tấn công, truy cập trái phép, sửa đổi trái phép, phát tán trái phép và phá hoại dữ liệu. Ngành này cung cấp cho sinh viên những kiến thức nền tảng về mạng máy tính và hệ thống thông tin. Đồng thời, sinh viên cũng được trang bị các kiến thức chuyên sâu về kỹ thuật mật mã, an toàn hệ điều hành, cơ sở dữ liệu, an toàn trong các ứng dụng web và Internet, an toàn trong giao dịch và thương mại điện tử, các kỹ thuật tấn công và xâm nhập mạng, cùng với mô hình bảo vệ và các kỹ thuật phòng thủ chống tấn công đột nhập. Ngành An toàn thông tin là một ngành học hấp dẫn và đầy hứa hẹn trong bối cảnh công nghệ thông tin phát triển mạnh mẽ như hiện nay. Sau khi ra trường, sinh viên có thể làm việc trong các lĩnh vực như bảo mật thông tin, giám sát an ninh mạng, kiểm tra bảo mật và xác thực, quản lý rủi ro an ninh mạng và nghiên cứu phát triển sản phẩm an ninh mạng '
#     ),# 2: khmt
#     data_nganh[2]:()
#     ,# 3: QTKD
#     data_nganh[3]:(
#     'Quản trị kinh doanh là một ngành học liên quan đến việc quản lý, tổ chức và điều hành các hoạt động kinh doanh trong một tổ chức hoặc doanh nghiệp nhằm đạt được mục tiêu kinh doanh. Ngành này cung cấp cho sinh viên kiến thức về lập kế hoạch, tài chính, quản lý nhân sự, tiếp thị, kiểm soát và định hướng chiến lược để đảm bảo hoạt động hiệu quả và phát triển bền vững của doanh nghiệp 1234. Sau khi ra trường, sinh viên có thể làm việc trong các lĩnh vực như quản lý doanh nghiệp, tư vấn kinh doanh, quản lý nhân sự, tiếp thị và bán hàng, tài chính và ngân hàng, khởi nghiệp và phát triển sản phẩm.'
#     ),# 4: iot
#     data_nganh[4]:(
#     '''Internet of Things (IoT) là một ngành công nghệ liên quan đến việc kết nối các thiết bị điện tử thông minh với nhau và với internet, cho phép chúng ta thu thập, truyền tải và xử lý dữ liệu thông qua mạng internet. Ngành này bao gồm nhiều chuyên ngành như khoa học máy tính, mạng máy tính, truyền thông dữ liệu, công nghệ phần mềm, kỹ thuật máy tính, hệ thống quản lý thông tin, robot và trí tuệ nhân tạo. '
# Sinh viên theo học ngành này sẽ được đào tạo các môn liên quan đến khoa học máy tính như: Mạng máy tính căn bản, Lập trình cao cấp, Lập trình cao cấp Python, Lập trình ứng dụng Android kết nối thiết bị IoT, Dịch vụ đám mây, Khoa học dữ liệu, v.v'
# Các ứng dụng của IoT rất đa dạng và phong phú. Ví dụ như trong lĩnh vực y tế, IoT có thể được sử dụng để giám sát sức khỏe của bệnh nhân từ xa. Trong lĩnh vực sản xuất, IoT có thể được sử dụng để giám sát quá trình sản xuất và tối ưu hóa hiệu suất sản xuất. Trong lĩnh vực nông nghiệp, IoT có thể được sử dụng để giám sát và điều khiển các hoạt động trồng trọt 
# '''
#     )
# }



diem_truong_nganh_nam = {
    "2023": {
        data_nganh[0]: {
            data_truong[0]: 27,
            data_truong[1]: 26,
            data_truong[2]: 25
        },
        data_nganh[1]: {
            data_truong[0]: 28,
            data_truong[1]: 27,
            data_truong[6]: 29
        },
        data_nganh[2]: {
            data_truong[0]: 28,
            data_truong[1]: 27,
            data_truong[2]: 26
        },
        data_nganh[3]: {
            data_truong[0]: 29,
            data_truong[1]: 28,
            data_truong[2]: 27
        },

    },
    "2022":{}
}

# khoi_thi_cua_nganh= {
#     data_nganh[0]:(
# '''Có nhiều lựa chọn về khối thi để học ngành Công nghệ thông tin, bao gồm khối A và khối D. Khối A bao gồm A00 (Toán, Lý, Hóa) và A01 (Toán, Lý, Anh), được sử dụng rộng rãi để xét tuyển vào ngành CNTT. Nếu bạn muốn đăng ký vào ngành CNTT ở các trường, chọn khối A00 có thể là lựa chọn an toàn nhất.
# Khối A01 cũng được sử dụng nhiều hơn trong việc xét tuyển vào ngành CNTT trong những năm gần đây, do ngành nghề này đòi hỏi nhân sự có tư duy logic và ngoại ngữ. Nếu bạn chuyên khối A và có năng lực với ngoại ngữ, khối A01 là cơ hội cho bạn.
# Khối D bao gồm D01, D02, D03, D04, D05 và D06. Tiếng Anh có thể được thay thế bằng các ngoại ngữ khác như Trung, Nhật, Pháp, Nga,... Ngoài khối D truyền thống, một số trường sử dụng khối D09 và D10 để xét tuyển vào ngành CNTT. Đối với các học sinh chọn học khối D, tiếng Anh có thể giúp gỡ điểm và nâng điểm. Bạn cũng cần cố gắng nâng mức điểm ở các môn như Ngữ văn và Địa lý nếu muốn đăng ký vào ngành CNTT.
# '''
#     ),
#     data_nganh[1]:(
# '''Có nhiều lựa chọn về khối thi để học ngành An toàn thông tin, bao gồm khối A và khối D. Khối A bao gồm A00 (Toán, Lý, Hóa) và A01 (Toán, Lý, Anh), được sử dụng rộng rãi để xét tuyển vào ngành ATTT. Nếu bạn muốn đăng ký vào ngành ATTT ở các trường, chọn khối A00 có thể là lựa chọn an toàn nhất.
# Khối A01 cũng được sử dụng nhiều hơn trong việc xét tuyển vào ngành ATTT trong những năm gần đây, do ngành nghề này đòi hỏi nhân sự có tư duy logic và ngoại ngữ. Nếu bạn chuyên khối A và có năng lực với ngoại ngữ, khối A01 là cơ hội cho bạn.
# Khối D bao gồm D01, D02, D03, D04, D05 và D06. Tiếng Anh có thể được thay thế bằng các ngoại ngữ khác như Trung, Nhật, Pháp, Nga,... Ngoài khối D truyền thống, một số trường sử dụng khối D09 và D10 để xét tuyển vào ngành ATTT. Đối với các học sinh chọn học khối D, tiếng Anh có thể giúp gỡ điểm và nâng điểm. Bạn cũng cần cố gắng nâng mức điểm ở các môn như Ngữ văn và Địa lý nếu muốn đăng ký vào ngành ATTT.
# '''
#     ),
#     data_nganh[2]:(
#         ),
#     data_nganh[3]:(
#         ),
#     data_nganh[4]:(
#         'Ngành Quản trị Kinh doanh là một ngành thuộc khối kinh tế, do đó các khối thi chính của ngành này thường là A00, A01 và D01.'
#         ),


# }

data_diem_uu_tien = [
    (
        '''1. Điểm ưu tiên là mức điểm thí sinh thuộc diện đặc biệt được cộng thêm vào số điểm thi thực tế. Đây là căn cứ để các đơn vị giáo dục thực hiện việc xét tuyển. Có 2 loại điểm ưu tiên bao gồm: Điểm ưu tiên theo khu vực và điểm ưu tiên theo đối tượng.'''
    ),(
         '2. Quy định về điểm ưu tiên khi thi xét tuyển Đại học 2023:'
        
# - Chính sách cộng điểm ưu tiên Đại học 2023 theo khu vực

# Theo Quy chế tuyển sinh Đại học 2022, chính sách cộng điểm ưu tiên được quy định cụ thể như sau:
# Đối tượng thuộc khu vực 1 (KV1) được cộng 0,75 điểm: Bao gồm các xã đặc biệt khó khăn thuộc vùng sâu vùng xa, vùng dân tộc thiểu số, miền núi, biên giới và hải đảo; các xã an toàn khu vào diện đầu tư của Chương trình 135 theo quy định của Thủ tướng Chính phủ.
# Khu vực 2 (KV2) được cộng 0,25 điểm: Các huyện và thị xã ngoại thành của thành phố trực thuộc Trung ương hoặc thành phố trực thuộc tỉnh, ngoại trừ các địa phương thuộc KV1.
# Khu vực 3 (KV3) không được cộng điểm ưu tiên: Bao gồm các quận trong nội thành của thành phố trực thuộc trung ương.
# Khu vực 2 nông thôn (KV2-NT) được cộng 0,5 điểm: Các địa phương không thuộc KV1, KV2, KV3.

# - Chính sách cộng điểm ưu tiên Đại học 2022 theo đối tượng chính sách

# Có 2 nhóm đối tượng ưu tiên bao gồm: Ưu tiên 1 (ƯT1) và Ưu tiên 2 (ƯT2).

# Nhóm ƯT1 được cộng 2 điểm, bao gồm:

# Công dân Việt Nam là người dân tộc thiểu số có nơi thường trú trong thời gian học THPT hoặc trung cấp trên 18 tháng tại KV1.
# Công nhân trực tiếp sản xuất đã làm việc liên tục 5 năm trở lên, trong đó tối thiểu 2 năm là chiến sĩ thi đua cấp tỉnh được công nhận và được nhận giấy khen.
# Đối tượng là thương binh, bệnh binh, người có giấy chứng nhận được hưởng chính sách như thương binh.
# Những người là sĩ quan, hạ sĩ quan, chiến sĩ nghĩa vụ phục vụ trong Công an nhân dân tại ngũ có thời gian phục vụ từ 12 tháng trở lên đối với KV1, 18 tháng trở lên tại các khu vực còn lại hoặc đã hoàn thành nghĩa vụ phục vụ theo quy định.
# Đối tượng là con của thương binh liệt sĩ, con của người hoạt động kháng chiến bị nhiễm chất độc màu da cam và bị suy giảm khả năng lao động từ 81% trở lên. Những người là con của người hoạt động kháng chiến bị dị tật, dị dạng do chất độc hóa học và đang được nhận trợ cấp hàng tháng.
# Đối tượng là của con Anh hùng Lực lượng vũ trang nhân dân hoặc Anh hùng lao động trong thời kỳ kháng chiến.
# Nhóm ƯT2 được cộng 1 điểm, bao gồm:

# Đối tượng là thanh niên xung phong được cử đi học.
# Những người là sĩ quan, hạ sĩ quan, chiến sĩ nghĩa vụ phục vụ trong Công an nhân dân tại ngũ có thời gian phục vụ từ 12 tháng trở lên đối với KV1, 18 tháng trở lên tại các khu vực còn lại.
# Chỉ huy trưởng, chỉ huy phó ban chỉ huy quân sự xã, phường, thị trấn; những người là trưởng thôn, trung đội trưởng dân quân tự vệ. Dân quân tự vệ đã hoàn thành tham gia thực hiện nghĩa vụ Dân quân tự vệ từ 12 tháng trở lên, dự thi vào ngành Quân sự cơ sở. Lưu ý thời hạn tối đa được hưởng chế độ cộng điểm ưu tiên là 18 tháng kể từ ngày ký quyết định xuất ngũ đến ngày đăng ký xét tuyển.
# Công dân Việt Nam là người dân tộc thiểu số có nơi thường trú tại nơi ngoài khu vực của đối tượng thuộc nhóm ƯT1.
# Người khuyết tật nặng được cơ quan có thẩm quyền xác nhận.
# Giáo viên đã giảng dạy tối thiểu 3 năm tại các cơ sở giáo dục đăng ký dự tuyển vào các ngành đào tạo giáo viên.
# Những người là y tá, hộ lý, dược tá, điều dưỡng viên,... có bằng trung cấp Dược tá đã công tác tối thiểu 3 năm đăng ký dự tuyển vào các ngành có liên quan đến chuyên môn.
''''''
    ),(
'''3. Cách tính điểm ưu tiên thi Đại học 2023
Năm 2023 là năm đầu tiên áp dụng cách tính điểm ưu tiên mới trong kỳ thi THPT quốc gia, xét tuyển Đại học, Cao đẳng, cụ thể:

Điểm ưu tiên thí sinh được hưởng = [(30 - tổng điểm đạt được của thí sinh)/7,5] x Tổng điểm ưu tiên được xác định thông thường.

Đối với thí sinh có điểm thực tế từ 22,5 trở lên (tính theo thang 10 điểm và tổng điểm 3 môn tối đa là 30) sẽ giảm dần đến 0 khi thí sinh đạt số điểm thi thực tế tổng 3 môn là 30 điểm.

Áp dụng công thức ở trên:

Thí sinh thuộc đối tượng khu vực 1 thi thực tế đạt 22,5 trở xuống thì được cộng 0,75 điểm ưu tiên khu vực. Trường hợp đạt 27 điểm thực tế thì điểm ưu tiên chỉ còn là 0,3; và 29 điểm chỉ còn 0,1 điểm ưu tiên khu vực.'''
    ),(
'''
Xét tuyển Đại học bằng học bạ có được cộng điểm ưu tiên?
Xét học bạ được là hình thức xét tuyển đại học phổ biến hiện nay. Trong phương thức xét tuyển Đại học 2022 theo quy định của Bộ giáo dục và đào tạo, xét tuyển học bạ vẫn sẽ được cộng điểm ưu tiên.

'''
    )
]
ds_uu_tien = ['kv1', 'kv2', 'kv2nt', 'kv3', 'ut1', 'ut2']

ds_dien_uu_tien = {ds_uu_tien[0]: {'Khu vực 1'}, ds_uu_tien[1]:{'Khu vực 2'}, ds_uu_tien[2]:{'Khu vực 2 nông thôn'}, ds_uu_tien[3]:{'Khu vực 3'}, ds_uu_tien[4]:{'Ưu tiên 1'}, ds_uu_tien[5]:{'Ưu tiên 2'}}


diem_uu_tien = {ds_uu_tien[0]: {0,75}, ds_uu_tien[1]:{0,25}, ds_uu_tien[2]:{0,5}, ds_uu_tien[3]:{0}, ds_uu_tien[4]:{2}, ds_uu_tien[5]:{1}}


FAQ = [f'Tuyển sinh {danh_sach_truong[random_truong[1]]}',
       f'Giới thiệu ngành {danh_sach_nganh [random_nganh[0]]}',
       f'Điểm chuẩn {danh_sach_truong[random_truong[0]]}',
       'Điểm ưu tiên là gì',
       'Các ngành hot',
        'Cách đổi nguyện vọng',
        'Thí sinh tự do',
        f'Khối thi của ngành {danh_sach_nganh [random_nganh[1]]}',
        f'Đào tạo {danh_sach_truong[random_truong[2]]}',
        'Thi năng lực TP.HCM',
        'Thi năng lực Hà Nội',
        f'Học phí {danh_sach_truong[random_truong[3]]}',
        f'Trường có ngành {danh_sach_nganh [random_nganh[2]]}'
       ]
