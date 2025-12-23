from addres import Address

from mailing import Mailing

to_adr = Address('1505', 'moscow', 'dream', 15, 22)
from_adr = Address ('1606', 'tver', 'search', 89, 87)

mail = Mailing(to_adr, from_adr, 555.6, 'ABC321')

print(
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)