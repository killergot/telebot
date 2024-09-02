HELP_COMMAND : str = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начинает работу бота</em>
<b>/photo</b> - <em>отправляет картинку дуси</em>
<b>/location</b> - <em>отправляет локацию</em>
<b>/give</b> - <em>Передачка сообщений</em>
<b>/weather</b> - <em>Показывает погоду</em>
<b>/game</b> - <em>Игра в угадывание слов</em>
<b>/weather</b> - <em>Показывает погоду</em>
<b>/cancel</b> - <em>отменяет действие</em>
"""

monkes : list[str] = ['https://sun9-79.userapi.com/impg/-JPgD8xr9rK3WeiFKcwMp5nh3MKAsa1qHis6iw/fUWhUC0J53A.jpg?size=564x695&quality=96&sign=b5fdbf1096ece2427869b5ebe5306494&type=album',
           'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTlFppQFm4VCK-UlCGwBXMWBW1BSM0v_KDxVwXZgEO-4slA_Bq23-4OUg_Lg2ONXc2D',
           'https://sun9-47.userapi.com/impg/vdqyYsdz8bLkE6NUgRx6X2D2JN2TkUDG6T-CxA/t8b5Gk_zd0M.jpg?size=1280x960&quality=95&sign=0d084b26158f553973ac82a2810928ce&type=album',
           'https://sun9-31.userapi.com/impg/PgwnaoKeECJpZZtnQ7I2f7RDJ3-btU4MjosZjA/wTsb_GIKBF8.jpg?size=810x1080&quality=95&sign=0f727722dc394e5b250fc097d1260338&type=album',
            'https://sun9-54.userapi.com/impg/2dGzKMBjdQsm9mOm1-TlpIUmJXDdd0MIccX_3Q/QWeN_VPoMcU.jpg?size=1280x960&quality=95&sign=98dd4c9f466b81d7f6b827649e5076d4&type=album',
            'https://sun9-49.userapi.com/impg/D-L3UGEChNYcF5d-zqZSfkMesg-TUB6yttxhvg/KepnIjf5ZB8.jpg?size=810x1080&quality=95&sign=504e6adced2c77a109c7482b253602ab&type=album',
            'https://sun9-56.userapi.com/impg/k13d9-5kLc87c1QZWbBMJvxGTZn7EaDpvfaS_A/VsjTjebkeh0.jpg?size=1280x1280&quality=95&sign=b368d85e2be2ee60e87e26e26e049866&type=album',
            'https://sun9-24.userapi.com/impg/19gkAKjaaIXukQqvvzPJnHOH7TR10T8uoucAew/Nbj_QZyQQBE.jpg?size=810x1080&quality=95&sign=2f357edf06d9b914680f80aff817b7cc&type=album',
            'https://sun9-78.userapi.com/impg/ZH8j9nliGw3U14BXJmy7EszYYNQn2lqfGsqETg/_ZvJjnGFWSE.jpg?size=1280x960&quality=95&sign=21bddcdeb2b162d0722bf5ed6c6af0d7&type=album',
            'https://sun9-67.userapi.com/impg/j-JRhb2afd4e-RAm_2K4Hsm4fnIzJL0P6ggWog/rVB_7rNO11I.jpg?size=810x1080&quality=95&sign=3cb571b77819c2de0f7daeb9252c89ee&type=album',
            'https://sun9-44.userapi.com/impg/ypH2Gy_Gs5K1knXaYFPit3Rt79Awhp7LEc5P1A/Xemd9eZw4ZU.jpg?size=810x1080&quality=95&sign=c8e37dd9258bfacae94c9304348f36c2&type=album',
            'https://sun9-25.userapi.com/impg/oEv_ZR5X_2f8TlOKKwAHHLUp8TnSfZKc2rMiqw/eTVmw0nx0Pg.jpg?size=810x1080&quality=95&sign=b4f5fc0ef6f792a3432163b3acc87bb0&type=album',
            'https://sun9-47.userapi.com/impg/stKGAt_cveUS0AGlVJhxKo92uIvo_YAp2bA9-w/jJe-4QSIHfQ.jpg?size=810x1080&quality=95&sign=2c251d9b2ac2375ae15120b972d67c26&type=album',
            'https://sun9-53.userapi.com/impg/mnfcnqgZjitO807CDBCy5wB0qyn-GAeS1aYX9Q/f4_RWHg-l8I.jpg?size=810x1080&quality=95&sign=de7c72941ee765181c05c4240eda24a4&type=album',
            'https://sun9-4.userapi.com/impg/YpAjxvhx2UsrKBy6LDI6Y044WsVyCUPAwrkLLg/su8C2hvWOXs.jpg?size=810x1080&quality=95&sign=e6ec4542a2e60704e0c0d07b318cf022&type=album',
            'https://sun9-79.userapi.com/impg/joZvnv4b0zv63fgaK9Y06_soa_xnfH08V8uEPQ/n28SNOVH-ng.jpg?size=802x1080&quality=95&sign=ace18ca6b2372b9bcf318f87ecae0576&type=album',
            'https://sun9-6.userapi.com/impg/I6f13MWyhuxfM9u4KSJArdtYNJj5ZGv9ItdfQQ/Q0Rie9lz8zU.jpg?size=810x1080&quality=95&sign=6a6690023b3a5e1580092f58edfadb2b&type=album',
            'https://sun9-25.userapi.com/impg/RNqRUVYrONNRn1qkgZx-CY7jLHs61ylqdk1ZNQ/Ai169g8LE-4.jpg?size=810x1080&quality=95&sign=1783fbc4d5111bf387bb462b7093cfc5&type=album']

TOKEN_ADMIN : str = '6695234791:AAG4Y9ZHh9rRmcyAwghFob1ErjHlZ_rIDXk'
TOKEN_OWM : str = '381daa25d46266525eee2ff2281df295'


host = "127.0.0.1"
user = "postgres"
password = "132435"
db_name = "telebot"

