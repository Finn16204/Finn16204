import pandas as pd
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.transactions_file = "transactions.csv"
        self.categories = [
            "Ăn uống", "Di chuyển", "Mua sắm", "Giải trí",
            "Hóa đơn", "Y tế", "Giáo dục", "Khác"
        ]
        
        if not os.path.exists(self.transactions_file):
            self.create_empty_database()
            
    def create_empty_database(self):
        df = pd.DataFrame(columns=[
            'ngay', 'loai', 'danh_muc', 'so_tien', 'mo_ta'
        ])
        df.to_csv(self.transactions_file, index=False)
        
    def load_transactions(self):
        return pd.read_csv(self.transactions_file)
        
    def add_transaction(self, date, type_trans, category, amount, description):
        df = self.load_transactions()
        new_row = {
            'ngay': date,
            'loai': type_trans,
            'danh_muc': category,
            'so_tien': amount,
            'mo_ta': description
        }
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(self.transactions_file, index=False)
        
    def get_balance(self):
        df = self.load_transactions()
        income = df[df['loai'] == 'Thu'].so_tien.sum()
        expense = df[df['loai'] == 'Chi'].so_tien.sum()
        return income - expense
        
    def get_category_summary(self):
        df = self.load_transactions()
        return df[df['loai'] == 'Chi'].groupby('danh_muc')['so_tien'].sum()
