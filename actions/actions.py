# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from alldata import * 
from cgitb import text
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from googleapiclient.discovery import build
import json
import requests

from bs4 import BeautifulSoup



class ActionFallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        random_FAQ = random.sample(FAQ, len(FAQ))
        buttons_random_FAQ = [
            {
                "title": random_FAQ[0],
                "payload": random_FAQ[0]
            },
            {
                "title": random_FAQ[1],
                "payload": random_FAQ[1]
            },
            {
                "title": random_FAQ[2],
                "payload": random_FAQ[2]
            }]
        
        dispatcher.utter_message(text=f"Xin lỗi, tôi chưa rõ ý của bạn là gì. Dưới đây là một số câu hỏi khác mà bạn có thể sử dụng", buttons = buttons_random_FAQ)
        return []
    


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_custom_greet"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        random_FAQ = random.sample(FAQ, len(FAQ))
        buttons_random_FAQ = [
            {
                "title": random_FAQ[0],
                "payload": random_FAQ[0]
            },
            {
                "title": random_FAQ[1],
                "payload": random_FAQ[1]
            },
            {
                "title": random_FAQ[2],
                "payload": random_FAQ[2]
            }]
        
        dispatcher.utter_message(text=f"Xin chào! Tôi là chatbot tư vấn tuyển sinh. Bạn muốn tôi giúp gì?", buttons = buttons_random_FAQ)
        return []
    
class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food_entity = next(tracker.get_latest_entity_values('food'), None)

        if food_entity:
            dispatcher.utter_message(text=f"You have selected {food_entity} as you food choice")
        else:
            dispatcher.utter_message(text="i am sorry , could not detected the food choice")

        return[]
    

class OrderFoodAction(Action):
    def name(self) -> Text:
        return "action_order_food"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, Which kind of food would you like to order")

        return []
    
class ConfirmOrderAction(Action):
    def name(self) -> Text:
        return "action_confirm_order"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food_entity = next(tracker.get_latest_entity_values('food'), None)

        if food_entity:
            dispatcher.utter_message(text=f"I have ordered {food_entity} for you")
        else:
            dispatcher.utter_message(text="i am sorry , could not detected the food choice")

        return[]
    


    # action nganh

class ExtractNganhEntity(Action):

    def name(self) -> Text:
        return "action_extract_nganh_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        


        nganh = NganhEntityLocation(tracker)

        if nganh != -1:  
            dispatcher.utter_message(text=f"Bạn muốn biết thêm thông tin về ngành {ten_nganh(nganh)} ?")
            return [SlotSet("nganh", nganh)]
        else:
            dispatcher.utter_message(text="Xin lỗi tôi không rõ đó là ngành gì, thay vào đó bạn có thể tìm hiểu thông tin của các ngành sau:",
                                     buttons=buttons_random_nganh)

        return[]
    

class NganhAction(Action):
    def name(self) -> Text:
        return "action_nganh"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Chắc chắn rồi, bạn muốn biết thông tin về ngành nào")

        return []
    
class ConfirmNganhAction(Action):
    def name(self) -> Text:
        return "action_confirm_nganh"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nganh = NganhEntityLocation(tracker)
        gtn= gioi_thieu_nganh(nganh)


        if gtn:
            dispatcher.utter_message(text=f"Đây là thông tin về ngành {ten_nganh(nganh)}: "
                                     f"{gtn}")
            
            return [SlotSet("nganh", nganh)]
        else:
            dispatcher.utter_message(text="Xin lỗi tôi hiện chưa có thông tin về ngành này")

        return[]
    
class ActionCacNganhCuaTruong(Action):
    def name(self) -> Text:
        return "action_cac_nganh_cua_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        buttons = []
        button = {}

        
        for nganh in nganh_cua_truong(truong):
                    button = {
                    "title": ten_nganh(nganh),
                    "payload": ten_nganh(nganh)
                    }
                    buttons.append(button)
        if truong and buttons:
            dispatcher.utter_message(text=f"Trường {ten_truong(truong)} có các ngành: "
             ,buttons=buttons)
            return [SlotSet("truong", truong)]
        elif truong:
            dispatcher.utter_message(text=f"Xin lỗi tôi thông tin về các ngành học của trường {ten_truong(truong)} hiện chưa được cập nhật")
        else:
            dispatcher.utter_message(text="Xin lỗi tôi không rõ đó là trường nào")

        return[]
class ActionChiTietDoiNguyenVong(Action):
    def name(self) -> Text:
        return "action_chi_tiet_doi_nguyen_vong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        co_entity = next(tracker.get_latest_entity_values('co'), None)
        khong_entity = next(tracker.get_latest_entity_values('khong'), None)

        if co_entity:
            dispatcher.utter_message(text=f'Đây là một số lưu ý khác khi đổi nguyện vọng: \n - Thí sinh có thể điều chỉnh, bổ sung nguyện vọng không giới hạn trong khoảng thời gian cho phép cụ thể là: "Từ ngày 10/7 đến 17 giờ 00 ngày 30/7/2023" thời gian có thể thay đổi giữa các năm \n...')
        else :
            dispatcher.utter_message(text="Bạn có yêu cầu nào khác không?")
        return[]

class ActionTTKhoiThi(Action):
    def name(self) -> Text:
        return "action_tt_khoi_thi"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cac_mon = ''
        khoi = next(tracker.get_latest_entity_values('khoi'), 0)
        if khoi:
            best_match, score = process.extractOne(khoi, cac_khoi_thi())  
            cac_mon = mon_cua_khoi_thi(best_match)

        if cac_mon:
            dispatcher.utter_message(text=f'Thông tin về khối thi {best_match}: {cac_mon}')
            return [SlotSet("khoi", khoi)]
        else :
            dispatcher.utter_message(text=f"Xin lỗi, tôi chưa có thông tin về khối thi '{khoi}'")
        return[]


class ActionMaTruong(Action):
    def name(self) -> Text:
        return "action_ma_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        khoi = next(tracker.get_latest_entity_values('khoi'), None)
        truong = TruongEntityLocation(tracker)
        #best_match, score = process.extractOne(khoi, khoi_thi)
        mt=ma_truong(truong)

        if mt:
            dispatcher.utter_message(text=f'Mã Trường của trường {ten_truong(truong)} là: {mt}')
            return [SlotSet("truong", truong)]
        else:
            dispatcher.utter_message(text="Bạn có yêu cầu nào khác không?")
        return[]
    
class ActionKhoiThiCuaNganh(Action):
    def name(self) -> Text:
        return "action_khoi_thi_cua_nganh"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        khoi = next(tracker.get_latest_entity_values('khoi'), None)
        nganh = NganhEntityLocation(tracker)
        #best_match, score = process.extractOne(khoi, khoi_thi)
        ktcn = khoi_thi_cua_nganh(nganh)

        if ktcn:
            dispatcher.utter_message(text=f'Các khối thi có thể có của ngành {ten_nganh(nganh)}: {ktcn}')
            return [SlotSet("nganh", nganh)]
        else:
            dispatcher.utter_message(text="Bạn có yêu cầu nào khác không?")
        return[]
    
class ActionCacNganhNoiBat(Action):
    def name(self) -> Text:
        return "action_cac_nganh_noi_bat"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        truong = TruongEntityLocation(tracker)
       
        buttons = []
        button = {}

        for nganh in nganh_noi_bat(truong):
            
                    button = {
                    "title": nganh,
                    "payload": nganh
                    }
                    buttons.append(button)
        if truong:
            dispatcher.utter_message(text=f"Các ngành nổi bật của trường {ten_truong(truong)}:",buttons=buttons)
            return [SlotSet("truong", truong)]
        else :
            dispatcher.utter_message(text="Bạn có yêu cầu nào khác không?")
        return[]

class ActionThongTinDaoTao(Action):
    def name(self) -> Text:
        return "action_thong_tin_dao_tao"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        truong = TruongEntityLocation(tracker)
        buttons = []
        buttons = [
            
            {
                "title": "Học phí",
                "payload": "Học phí trường trên"
            },
            {
                "title": "Học bổng",
                "payload": "Học bổng trường trên"
            },
            ]
        if truong:
            dispatcher.utter_message(text=f'Bạn muốn biết thông tin đào tạo nào của trường {ten_truong(truong)}:', buttons=buttons)

            return [SlotSet("truong", truong)]
        else :
            dispatcher.utter_message(text="Bạn có yêu cầu nào khác không?")
        return[]
    
class ActionXacNhanTruong(Action):
    def name(self) -> Text:
        return "action_xac_nhan_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        buttons_thong_tin = [
            {
                "title": "Thông tin tuyển sinh",
                "payload": "Thông tin tuyển sinh"
            },
            {
                "title": "Thông tin đào tạo",
                "payload": "Thông tin đào tạo"
            },
            {
                "title": "Các ngành đào tạo của trường",
                "payload": "Các ngành đào tạo của trường"
            },
            {
                "title": "Các ngành nổi bật của trường",
                "payload": "Các ngành nổi bật của trường"
            },
            ]
        gioi_thieu = gioi_thieu_truong(truong)

        if gioi_thieu:  
            dispatcher.utter_message(text=f"Đây là thông tin về trường {ten_truong(truong)}: {gioi_thieu}",buttons=buttons_thong_tin)
            
            return [SlotSet("truong", truong)]  # Đặt giá trị của slot 'truong'
        else:
            dispatcher.utter_message(text="Xin lỗi, thông tin của trường này chưa được chúng tôi cập nhật")
        return []

class ActionTruongVaNganhCuaBot(Action):
    def name(self) -> Text:
        return "action_nganh_va_truong_ma_bot_co"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text=f"Bot có dữ liệu của {len(danh_sach_truong)} trường  và {len(danh_sach_nganh)} ngành")
        # dispatcher.utter_message(text=f"\nCác trường mà bot có dữ liệu:  ")
        # for t in danh_sach_truong:
        #         dispatcher.utter_message(text=f"button")  
        #         dispatcher.utter_message(text=f"{danh_sach_truong[t]}")   
        # dispatcher.utter_message(text=f"\nCác ngành mà bot có dữ liệu:  ")
        # for n in danh_sach_nganh:
        #         dispatcher.utter_message(text=f"button")  
        #         dispatcher.utter_message(text=f"{danh_sach_nganh[n]}")   


        return []
    
class ActionTSTruong(Action):
    def name(self) -> Text:
        return "action_tuyen_sinh_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        if truong:  
            dispatcher.utter_message(text=f"Đây là thông tin tuyển sinh của trường {ten_truong(truong)}: "
                                     f"{tuyen_sinh_cua_truong_short[truong]}")
                                    #  f"\n Bạn có muốn biết thêm thông tin nào khác của trường {ten_truong(truong)} không?")
            return [SlotSet("truong", truong)]  # Đặt giá trị của slot 'truong'
        
        else:
            dispatcher.utter_message(text=f"Xin lỗi, thông tin tuyển sinh của trường này chưa được chúng tôi cập nhật, bạn có thể tìm hiểu thông tin của các trường khác như:"
                                     , buttons=buttons_random_truong)

        return[]
    
class ActionThiNangLuc(Action):
    def name(self) -> Text:
        return "action_thi_nang_luc"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        truong = TruongEntityLocation(tracker)
        tiep_tuc = next(tracker.get_latest_entity_values("co"), 0)
        # kvhcm = next(tracker.get_latest_entity_values("khu_vuc_hcm"), 0)
        # kvhn = next(tracker.get_latest_entity_values("khu_vuc_hn"), 0)   
        kv = KhuVucEntityLocation(tracker)
        buttons_tt = [
            {
                "title": "Tiếp tục",
                "payload": "Tiếp tục"
            }]

        # if truong in tt_thi_nang_luc_cua_cac_truong and truong in danh_sach_truong and tiep_tuc:  
        #     dispatcher.utter_message(text=f"Đây là thông tin về kỳ thi đánh giá năng lực của trường {ten_truong(truong)} năm 2023:"
        #     f'{tt_thi_nang_luc_cua_cac_truong[truong]}'                
        #     f"\n Bạn có muốn biết thêm thông tin nào khác của trường {ten_truong(truong)} không?")
        #     return [SlotSet("truong", truong)]  # Đặt giá trị của slot 'truong'
        if not tiep_tuc:
            if khu_vuc_cua_truong(truong) == "hn" or kv == "hn":
                dispatcher.utter_message(text=f"{ky_thi_nang_luc_hn[0]}",buttons= buttons_tt)
                return [SlotSet("khu_vuc", "hn")] 
            elif khu_vuc_cua_truong(truong)=="hcm" or kv =="hcm":
                dispatcher.utter_message(text=f"{ky_thi_nang_luc_hcm[0]}", buttons= buttons_tt)
                return [SlotSet("khu_vuc", "hcm")] 
            else:
                dispatcher.utter_message(text="Xin lỗi thông tin về kỳ thi năng lực của trường này chưa được cập nhật")
        else:
            if khu_vuc_cua_truong(truong)=="hn" or kv == "hn":
                dispatcher.utter_message(text=f"{ky_thi_nang_luc_hn[1]}")
            elif khu_vuc_cua_truong(truong)=="hcm" or kv =="hcm":
                dispatcher.utter_message(text=f"{ky_thi_nang_luc_hcm[1]}")
            else:
                dispatcher.utter_message(text="Xin lỗi thông tin về kỳ thi năng lực của trường này chưa được cập nhật action_thi_nang_luc")
        return[]

    
class ActionKoDongY(Action):
    def name(self) -> Text:
        return "action_ko_dong_y"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Vậy bạn có muốn thông tin nào khác không")

        return[]
    

class ActionTruongPhuHop(Action):
    def name(self) -> Text:
        return "action_truong_phu_hop"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nganh = NganhEntityLocation(tracker)
        
        buttons = []
        buttons_limited_by_3 = []
        button = {}

        for truong in hoc_nganh_nay_o_dau(nganh):
            
                    button = {
                    "title": truong,
                    "payload": truong
                    }
                    buttons.append(button)


        # buttons_truong_phu_hop = [
        #     {
        #         "title": ten_nganh(nganh),
        #         "payload": ten_nganh(nganh)
        #     },
        #     {
        #         "title": ten_nganh(nganh),
        #         "payload": ten_nganh(nganh)
        #     },
        #     {
        #         "title": ten_nganh(nganh),
        #         "payload": ten_nganh(nganh)
        #     },
        #     {
        #         "title": ten_nganh(nganh),
        #         "payload": ten_nganh(nganh)
        #     }]
        if buttons:  
            i = 0
            dispatcher.utter_message(text=f"Đây là thông tin một số trường mà bạn có thể theo học ngành {ten_nganh(nganh)}")
            for b in buttons:
                if i < 3:
                    i += 1
                    buttons_limited_by_3.append(b)
                else:
                    i = 1
                    dispatcher.utter_message(text=f"{ten_nganh(nganh)}", buttons = buttons_limited_by_3)
                    buttons_limited_by_3 = []
                    buttons_limited_by_3.append(b)
            
            dispatcher.utter_message(text=f"{ten_nganh(nganh)}", buttons = buttons_limited_by_3)
            #dispatcher.utter_message(text="a",buttons=buttons)
            #dispatcher.utter_message(text="a",buttons=buttons_truong_phu_hop)
            #dispatcher.utter_message(text="b",buttons=buttons_truong_phu_hop)
            return [SlotSet("nganh", nganh)]
        else:
            dispatcher.utter_message(text=f'Hiện tại chúng tôi không có thông tin về ngành này, rất xin lỗi ')
        return []

class ActionHocDuocNganhNaoVoiDiem(Action):
    def name(self) -> Text:
        return "action_hoc_duoc_nganh_nao_cua_truong_nay_voi_so_diem_nay"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        nam = next(tracker.get_latest_entity_values("nam"), '2023')
        diem = next(tracker.get_latest_entity_values("diem"), 0)
        if int(nam) >2023 and int(nam)<2022:
            nam = '2023'
        dsnganh = ''

        if diem and truong:  
            dispatcher.utter_message(text=f'Bạn có thể học các ngành của trường {ten_truong(truong)} với số điểm {diem}: \n Lưu ý đây là số điểm của năm 2023'
                                     f'{diem_chuan_truong(truong,nam)}')
            return [SlotSet("truong", truong)] 
        else:
            dispatcher.utter_message(text=f'Bạn muốn biết điểm tuyển sinh của trường nào?')
        
        return []
    

class ActionDiemChuanNganhTruong(Action):
    def name(self) -> Text:
        return "action_diem_chuan_nganh_truong"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        nganh = NganhEntityLocation(tracker)
        # nam = next(tracker.get_latest_entity_values("nam"), None)
        # tt = ''
        # for n in diem_nganh_truong_nam:
        #     if truong in diem_nganh_truong_nam[n]:
        #         if nganh in diem_nganh_truong_nam[n][truong]:
        #             tt += f'\n- Năm {n}: {diem_nganh_truong_nam[n][truong][nganh]} điểm'   
        ds_diem =diem_chuan_nganh_cua_truong(truong, nganh)
        if ds_diem:
            dispatcher.utter_message(text=f'Đây là thông tin về điểm chuẩn ngành {ten_nganh(nganh)} của trường {ten_truong(truong)}:' 
                                     f'{ds_diem}')
            return [SlotSet("truong", truong), SlotSet("nganh", nganh)]
        elif truong and nganh:
        
            dispatcher.utter_message(text=f'Chúng tôi chưa có thông tin điểm chuẩn ngành {nganh} của trường {truong}')
        else:
            dispatcher.utter_message(text=f'Bạn muốn biết điểm chuẩn của trường nào?')
        return []
    

def TruongEntityLocation(tracker):
    truong_entity = 0
    for entity in data_truong:
        if next(tracker.get_latest_entity_values(entity), 0):
            truong_entity = entity
    if next(tracker.get_latest_entity_values("entity_above"), 0):
        truong_entity = tracker.get_slot("truong")  # Lấy slot truong
    return truong_entity

def NganhEntityLocation(tracker):
    nganh_entity = 0 
    for entity in data_nganh:
        if next(tracker.get_latest_entity_values(entity), 0):
            nganh_entity = entity
    if next(tracker.get_latest_entity_values("entity_above"), 0):
        nganh_entity = tracker.get_slot("nganh")
    return nganh_entity

def KhuVucEntityLocation(tracker):
    kvhcm = next(tracker.get_latest_entity_values("khu_vuc_hcm"), 0)
    kvhn = next(tracker.get_latest_entity_values("khu_vuc_hn"), 0)   
    entity = ''
    if kvhcm:
        entity = 'hcm'
    elif kvhn:
        entity = 'hn'
    else:
        entity = tracker.get_slot("khu_vuc")
    return entity

    
class ActionTSNganhCuaTruong(Action):
    def name(self) -> Text:
        return "action_ts_nganh_cua_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nganh = NganhEntityLocation(tracker)
        truong = TruongEntityLocation(tracker)
        nganh_dc_chat = ""
        entity_above = next(tracker.get_latest_entity_values("entity_above"), 0)
        for n in data_nganh:
            if next(tracker.get_latest_entity_values(n), 0):
                nganh_dc_chat = n
                
        nam = next(tracker.get_latest_entity_values("nam"), "2023")

        if diem_chuan_truong(truong, nam) and (not entity_above and not nganh_dc_chat) :
            dispatcher.utter_message(text=f"Đây là thông tin tuyển sinh của trường {ten_truong(truong)} năm {nam}: "
                                     f"{diem_chuan_truong(truong, nam)}"
                                     f"\n Bạn có muốn biết thêm thông tin nào khác của trường {ten_truong(truong)} không?")
            return [SlotSet("truong", truong)]  # Đặt giá trị của slot 'truong'
        elif (entity_above or nganh_dc_chat) and diem_chuan_nganh_cua_truong(truong, nganh):  
            #truong_duoc_chon = danh_sach_truong[location_truong]
            dispatcher.utter_message(text=f"Đây là thông tin tuyển sinh ngành {ten_nganh(nganh)} của trường {ten_truong(truong)}: "
                                        f'{diem_chuan_nganh_cua_truong(truong, nganh)}'
                                     f"\nBạn có muốn biết thêm thông tin nao khac của trường {ten_truong(truong)} không?")
            return [SlotSet("nganh", nganh), SlotSet("truong", truong)]
        # elif nam in chi_tiet_nganh and truong in chi_tiet_nganh[nam]:
        #      dispatcher.utter_message(text=f"Đây là thông tin về trường {ten_truong(truong)}: "
        #                              f"{gioi_thieu_so_ve_truong[truong]}"      )  
        # elif nam in chi_tiet_nganh and truong in chi_tiet_nganh[nam]:
        #     print("ádasdasdasd")
        #     print(nganh)
        #     dispatcher.utter_message(text=f"Đây là thông tin về ngành {ten_nganh(nganh)}: "
        #                              f"{gioi_thieu_nganh[nganh]}"
        #     f"\n Đây là thông tin các trường tốt nhất để học {ten_nganh(nganh)}: <button class='option-button'>{danh_sach_truong['ptit2']}</button>,<button class='option-button'>{danh_sach_truong['bkhn']}</button>, <button class='option-button'>{danh_sach_truong['dh_cntt']}</button> \nĐây chỉ là các trường được đánh giá cao và có danh tiếng tốt, tất nhiên bạn vẫn có thể lựa chọn các ngôi trường khác có những tiêu chí khác phù hợp hơn với bạn.')")
        elif (entity_above or nganh_dc_chat) and not truong :
            dispatcher.utter_message(text=f"{gioi_thieu_nganh(nganh)} ")
            dispatcher.utter_message(text=f"Một số trường có đào tạo ngành {ten_nganh(nganh)}", buttons=buttons_random_truong)

        else:
            dispatcher.utter_message(text=f"Xin lỗi, thông tin tuyển sinh này chưa được chúng tôi cập nhật ")

        return[]
    
class ActionDiemCanDeDoTruong(Action):
    def name(self) -> Text:
        return "action_diem_can_de_do_truong"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        nam = next(tracker.get_latest_entity_values("nam"), '2023')
        if int(nam) >2023 and int(nam)<2022:
            nam = '2023'
        dc = diem_chuan_truong(truong,nam)

        if dc:  
            dispatcher.utter_message(text=f'Đây là thông tin về điểm chuẩn các ngành của {ten_truong(truong)} năm {nam}'
                                     f'{diem_chuan_truong(truong,nam)}')
            return [SlotSet("truong", truong)] 
        else:
            dispatcher.utter_message(text=f'Bạn muốn biết điểm tuyển sinh của trường nào?')
        
        return []


class ActionTinhDiemUuTien(Action):
    def name(self) -> Text:
        return "action_tinh_diem_uu_tien"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #best_match, score = process.extractOne(uu_tien, ds_dien_uu_tien)
        diem = next(tracker.get_latest_entity_values("diem"), 0)
        uu_tien = 0
        for entity in ds_uu_tien:
            if next(tracker.get_latest_entity_values(entity), 0):
                uu_tien = entity
        if not uu_tien:
            uu_tien = tracker.get_slot("uu_tien")  
    
        diemgoc=diem
        diem = TinhDiemUuTien(diem,uu_tien)
        if diem and uu_tien and diem<=30 and diem >= 0:  
            dispatcher.utter_message(text=f"Công thức tính điểm ưu tiên: \nĐiểm ưu tiên thí sinh được hưởng = [(30 - tổng điểm đạt được của thí sinh)/7,5] x Tổng điểm ưu tiên được xác định thông thường. Đối với thí sinh có điểm thực tế từ 22,5 trở lên (tính theo thang 10 điểm và tổng điểm 3 môn tối đa là 30)"
                                     f"\nĐiểm của bạn là {diemgoc} và có điểm cộng là {diem_uu_tien[uu_tien]} từ {ds_dien_uu_tien[uu_tien]} áp dụng công thức thì tổng điểm của bạn sẽ là {diem}")
        elif uu_tien:
            dispatcher.utter_message(text=''
            f"Bạn thuộc diện{uu_tien} là {'THEM CHO THONG TIN VAO DAY'} trong quá trình tuyển sinh: sẽ được cộng 1 d kv2, 2d uT1")
        elif not uu_tien and not diem:
             dispatcher.utter_message(text=f"Công thức tính điểm ưu tiên: \nĐiểm ưu tiên thí sinh được hưởng = [(30 - tổng điểm đạt được của thí sinh)/7,5] x Tổng điểm ưu tiên được xác định thông thường. Đối với thí sinh có điểm thực tế từ 22,5 trở lên (tính theo thang 10 điểm và tổng điểm 3 môn tối đa là 30)")


        return[]

def TinhDiemUuTien(diem, uu_tien):
    diem_cong = 0
    if uu_tien == 'kv1':
        diem_cong = 0.75
    elif uu_tien == 'kv2':
        diem_cong = 0.25
    elif uu_tien == 'kv2nt':
        diem_cong = 0.5    
    elif uu_tien == 'ut1':
        diem_cong = 2    
    elif uu_tien == 'ut2':
        diem_cong = 1    
    diem = int(diem) + ((30-int(diem))/7.5)*diem_cong

    return round(diem,2)
    
class ActionDiemVaNganh(Action):
    def name(self) -> Text:
        return "action_diem_va_nganh"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        diem_entity = next(tracker.get_latest_entity_values('diem'), 0)
        nam = next(tracker.get_latest_entity_values('nam'), 2023)
        nganh = NganhEntityLocation(tracker)

        ds_truong_phu_hop = []
        buttons = []
        button = {}
        
        # if nganh in diem_truong_nganh_nam["2023"]:
        #     for t in diem_truong_nganh_nam["2023"][nganh]:
        #         if diem_truong_nganh_nam["2023"][nganh][t] <= float(diem_entity):
        #             ds_truong_phu_hop.append(danh_sach_truong[t])
        #             button = {
        #             "title": danh_sach_truong[t],
        #             "payload": danh_sach_truong[t]
        #             }
        #             buttons.append(button)

        for t in truong_phu_hop(nganh,  nam, diem_entity):
            #ds_truong_phu_hop.append(danh_sach_truong[t])
            button = {
                    "title": ten_truong(t),
                    "payload": ten_truong(t)
                    }
            buttons.append(button)
        if buttons:  
            dispatcher.utter_message(text=f'Đây là gợi ý một số trường tốt để học {ten_nganh(nganh)} với số điểm {diem_entity}, Tuy nhiên bạn vẫn có thể lựa chọn các ngôi trường khác có những tiêu chí khác phù hợp hơn với bạn.'
            ,buttons=buttons
            )
            return [SlotSet("nganh", nganh)]
        else:
            dispatcher.utter_message(text=f'Với số điểm này sẽ khá khó để bạn trúng tuyển, vì vậy bạn nên xem xét việc tham gia kỳ thi đánh giá năng lực hoặc xét tuyển vào những trường có ngành {ten_nganh(nganh)} ')
            
        return []
    
class ActionTinhDiemTest(Action):
    def name(self) -> Text:
        return "action_tinh_diem_test"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        diem_entity = next(tracker.get_latest_entity_values('diemTN'), None)
        tong_diem_test = tracker.get_slot("tong_diem_test")
        if not tong_diem_test:
            tong_diem_test = 0
        if diem_entity :  # Điều chỉnh ngưỡng dựa trên yêu cầu của bạn
            return [SlotSet("tong_diem_test", tong_diem_test + int(diem_entity))]
        return []
    
class ActionHinhThucXetTuyen(Action):
    def name(self) -> Text:
        return "action_phuong_thuc_xet_tuyen"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_truong = TruongEntityLocation(tracker)
        truong = ''
        htxt = ''
        truong = TruongEntityLocation(tracker)

        entity_above = next(tracker.get_latest_entity_values("entity_above"), 0)
        
        
        if truong:
            htxt = hinh_thuc_xt(truong)
        else:
            htxt = hinh_thuc_xt(slot_truong)

        if not entity_above and not truong:
            htxt = ''

        if htxt:
            dispatcher.utter_message(f"Hình thức xét tuyển của trường {ten_truong(truong)}:\n {htxt}")
            return [SlotSet("truong", truong)]
        else:            
            dispatcher.utter_message(response = "utter_hinh_thuc_xet_tuyen")
        return []

class ActionKetQuaTest(Action):
    def name(self) -> Text:
        return "action_ket_qua_test"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        tong_diem_test = tracker.get_slot("tong_diem_test")
        if tong_diem_test>40 :
            dispatcher.utter_message(f"Toi nghi ban phu hop voi cac nganh: Cong nghe thong tin, khoa hoc may tinh, an toan thong tin.")
        else:
            dispatcher.utter_message(f"Toi nghi ban phu hop voi cac nganh: Cong nghe thong tin, khoa hoc may tinh, an toan thong tin.")

            
        return []
    

class ActionHocPhiCuaTruong(Action):
    def name(self) -> Text:
        return "action_hoc_phi_cua_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        nam = 2023
        hp = hoc_phi(truong, nam)
        if hp:
            dispatcher.utter_message(f"Thông tin học phí của trường {ten_truong(truong)}:\n1 tín chỉ: {hp}.000 Đ, một học kỳ sẽ học khoảng 20 tín chỉ nên học phí một học kỳ sẽ khoảng {int(hp*0.02)}.000.000 Đ")
            return [SlotSet("truong", truong)]
        else:
            dispatcher.utter_message(f"Bạn muốn biết thông tin học phí của trường nào? ", 
                                     buttons=buttons_random_truong)
        
        return []
    

class ActionHocPhiPhuHop(Action):
    def name(self) -> Text:
        return "action_hoc_phi_phu_hop"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tien = 0
        trieu= next(tracker.get_latest_entity_values('trieu'), 0)
        dong = next(tracker.get_latest_entity_values('dong'), 0)
        if trieu:
            tien = int(trieu)*1000000
        else:
            tien = dong
        if tien:
            dispatcher.utter_message(f"Các trường có học phí dưới {tien}: ...updating")

        else:

            dispatcher.utter_message(f"Đây là danh sách các trường có học phí hợp lý ", buttons=buttons_random_truong)

        return []
    

class ActionHocBongCuaTruong(Action):
    def name(self) -> Text:
        return "action_cac_hoc_bong_cua_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        
        if truong and hoc_bong(truong):
            dispatcher.utter_message(f"Thông tin học bổng của trường {ten_truong(truong)}: {hoc_bong(truong)}")
            return [SlotSet("truong", truong)]
        elif truong:
            dispatcher.utter_message(f"Xin lỗi, thông tin học bổng của trường này chưa được cập nhật.")
        else:
            dispatcher.utter_message(f"Bạn muốn biết thông tin học bổng của trường nào? ", buttons=buttons_random_truong)

        return []


class ActionCoSoCuaTruong(Action):
    def name(self) -> Text:
        return "action_cac_co_so_cua_truong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        truong = TruongEntityLocation(tracker)
        
        if truong:
            dispatcher.utter_message(f"Thông tin cơ sở của trường {ten_truong(truong)}: ...updating")
            return [SlotSet("truong", truong)]
        else:
            dispatcher.utter_message(f"Bạn muốn biết thông tin cơ sở của trường nào? {danh_sach_truong[random_truong[1]]}, {danh_sach_truong[random_truong[0]]}, {danh_sach_truong[random_truong[2]]}")
        return []
    


nganh_de_xuat = {
    "máy tính": ["Công nghệ thông tin", "Khoa học máy tính", "An toàn thông tin"],
    "chơi game": ["Lập trình game", "Khoa học máy tính"],
    "hacker": ["An toàn thông tin", "Khoa học máy tính"],
    "làm phần mềm": ["Công nghệ thông tin", "Kỹ thuật phần mềm"],
    "điện tử": ["Kỹ thuật điện tử", "Kỹ thuật viễn thông"],
    "an toàn thông tin": ["An toàn thông tin", "Công nghệ thông tin"],
    "sư phạm": ["Giáo dục", "Sư phạm"],
}

def de_xuat_nganh(interest):
    # Kiểm tra xem sở thích có trong từ điển ánh xạ không
    if interest in nganh_de_xuat:
        nganh = nganh_de_xuat[interest]
        # Trả về danh sách ngành dựa trên sở thích
        return ", ".join(nganh)
    else:
        # Nếu không tìm thấy đề xuất nào, bạn có thể trả về một ngành mặc định hoặc thông báo không có đề xuất.
        return "Không có đề xuất ngành nào cho sở thích này."
    


class ActionHoiKhoiThi(Action):
    def name(self):
        return "action_hoi_khoi_thi"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Bạn thi khối nào?")

class ActionHoiNganh(Action):
    def name(self) -> Text:
        return "action_hoi_nganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Bạn thích lĩnh vực nào?")
        return []

class ActionDeXuatNganh(Action):
    def name(self) -> Text:
        return "action_de_xuat_nganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nganh = tracker.latest_message['entities'][0]['value']

        # Thực hiện logic đề xuất ngành dựa trên sở thích
        de_xuat_nganh_ = de_xuat_nganh(nganh)  # Hãy thay thế hàm này bằng logic thực tế của bạn
        dispatcher.utter_message(f"Với sở thích của bạn, tôi đề xuất bạn nên học ngành {de_xuat_nganh_}.")
        return []
    
class ActionAskQuestion(Action):
    def name(self):
        return "action_ask_question"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Hãy đặt câu hỏi của bạn ở đây.")

        return []

class ActionOtherInfo(Action):
    def name(self):
        return "action_other_info"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Thông tin khác có thể là gì?")

        return []

class ActionProvideOptions(Action):
    def name(self) -> Text:
        return "action_provide_options"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Danh sách các tùy chọn cho người dùng
        options = ["Option 1", "Option 2", "Option 3"]
        
        # Hiển thị tùy chọn cho người dùng
        dispatcher.utter_message(text="Here are some options:", buttons=options)
        
        return []
    
class ActionHandleOption(Action):
    def name(self) -> Text:
        return "action_handle_option"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy tùy chọn người dùng đã chọn từ tracker
        selected_option = tracker.get_slot("selected_option")
        
        # Xử lý tùy chọn ở đây và tạo phản hồi tương ứng
        if selected_option == "Option 1":
            dispatcher.utter_message(text="You chose Option 1")
        elif selected_option == "Option 2":
            dispatcher.utter_message(text="You chose Option 2")
        elif selected_option == "Option 3":
            dispatcher.utter_message(text="You chose Option 3")
        
        return []

# gôgle



class SearchGoogleCSE(Action):
    def name(self):
        return "action_search_google_cse"

    def run(self, dispatcher, tracker, domain):
        # Lấy thông tin từ người dùng (ví dụ: từ khóa tìm kiếm)
        # user_query = tracker.latest_message.get('text')

        # # Sử dụng CX (Custom Search Engine ID) của bạn
        # cx = "61fab5edd4ebe41ae"

        # # Khóa API của bạn
        # api_key = "AIzaSyCsU05_1q-Mz4tznH_uQCWe2cUiizrfTH4"

        # # Tạo kết nối tới Google CSE API
        # service = build("customsearch", "v1", developerKey=api_key)

        # # Thực hiện cuộc gọi API
        # results = service.cse().list(q=user_query, cx=cx).execute()

        # # Xử lý kết quả
        # if 'items' in results:
        #     search_results = results['items']
        #     link = search_results[0]['link']
        #     response = requests.get(link)
        #     if response.status_code == 200:
        #             # Sử dụng BeautifulSoup để phân tích nội dung trang web
        #         soup = BeautifulSoup(response.text, 'html.parser')
                    
        #             # Lấy toàn bộ nội dung của trang web
        #         full_content = soup.get_text()
        #         paragraphs = soup.find_all("p")
        #         intro = paragraphs[1].get_text()
        #         print(paragraphs[1])
        #         # for paragraph in paragraphs:
        #         #     paragraph_text = paragraph.get_text()
                    
        #         #     # Gửi nội dung đầy đủ của trang web dưới dạng tin nhắn
        #         #     dispatcher.utter_message(text=paragraph_text)
        #         # else:
        #         #     print("Không tìm thấy đoạn giới thiệu.")
        #         dispatcher.utter_message(text=intro)
        # else:
        #    
        dispatcher.utter_message(text="Không tìm thấy kết quả phù hợp.")
        return []
    
class SearchThiSinhTuDo(Action):
    def name(self):
        return "action_thi_sinh_tu_do"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(text="Bạn có thể đăng ký dự thi THPT Quốc gia trực tiếp tại các đơn vị đăng ký dự thi do Sở Giáo dục và Đào tạo quy định. Nếu bạn muốn đăng ký dự thi trực tuyến, bạn có thể truy cập vào trang web của Bộ Giáo dục và Đào tạo để đăng ký. \n Sau khi nộp đầy đủ hồ sơ đăng ký dự thi, thí sinh được đơn vị đăng ký dự thi cấp tài khoản và mật khẩu để đăng nhập hệ thống quản lý thi http://thisinh.thitotnghiepthpt.edu.vn.")
        # buttons = [
        #     {
        #         "title": "Hướng dẫn đăng ký trực tuyến",
        #         "payload": "Hướng dẫn đăng ký trực tuyến"
        #     },

        # ]
        
        #dispatcher.utter_message(buttons=buttons)

        return []

class ClearSlotsAction(Action):
    def name(self):
        return "action_clear_slots"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet(slot, None) for slot in tracker.slots.keys()]