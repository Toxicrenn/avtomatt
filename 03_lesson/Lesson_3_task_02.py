from smartphone import Smartphone

phone1 = Smartphone('IPhone', '16 Pro Max', '+79123456789')
phone2 = Smartphone('Samsung', 'Galaxy A5', '+79987456123')
phone3 = Smartphone('Nokia','1011', '+79852637419')
phone4 = Smartphone('Iphone', '13 Pro', '+79846251349')
phone5 = Smartphone('Xiaomi', 'Note 12', '+7902365026840')

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phonenumber}")