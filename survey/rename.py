from pandas.core.frame import DataFrame
from pandas.core.series import Series
import pandas as pd

rename_dict = {
    "1. Оцените, насколько обучение в РХТУ им. Д.И. Менделеева соответствует Вашим ожиданиям": "ожидания_от_вуза",
    "2. Оцените, насколько Вы удовлетворены информированием по вопросам учебного процесса деканатом факультета/института": "информирование_деканатом",
    "3. Оцените, насколько Вы удовлетворены информированием по вопросам обучения по дисциплинам профессорско-преподавательским составом": "информирование_преподавателями",
    "4. Оцените, насколько Вы удовлетворены перечнем дисциплин, которые Вы изучаете в рамках образовательной программы": "перечень_дисциплин",
    "5. Оцените, насколько Вы удовлетворены методами и технологиями чтения лекций по образовательной программе": "методы_чтения_лекции",
    "6. Оцените, насколько Вы удовлетворены технологиями проведения практических и лабораторных занятий": "практики_лабораторные",
    "7. Оцените, насколько Вы удовлетворены разъяснениями критериев оценки знаний, умений и навыков по дисциплинам": "критерии_оценок",
    "8. Оцените, насколько Вы удовлетворены объективностью оценивания учебных достижений": "объективность_оценок",
    "9. Оцените, насколько Вы удовлетворены доброжелательностью, вежливостью сотрудников деканата/института, кафедр при непосредственном обращении": "вежливость_сотрудников",
    "10. Оцените, насколько Вы удовлетворены доброжелательностью, вежливостью преподавателей при непосредственном обращении": "вежливость_преподавателей",
    "11. Оцените, насколько вы удовлетворены доступностью учебной и учебно-методической литературы, электронных ресурсов по образовательной программе": "доступность_литературы",
    "12. Оцените, насколько Вы удовлетворены состоянием учебных аудиторий, лабораторий, в которых проходят занятия": "состояние_аудиторий",
    "13. Оцените, насколько Вы удовлетворены организацией практик": "организация_практик",
    "14. Оцените, насколько Вы удовлетворены доступностью сети Internet в Университете": "интернет",
    "15. Оцените, насколько Вы удовлетворены качеством беспроводного подключения для коммуникации различных устройств (Wi-Fi) в Университете?": "качество_wifi",
    "16. Оцените, насколько Вы удовлетворены возможностями академической мобильности обучающихся (включенное обучение в отечественных и зарубежных вузах, участие в летних/зимних школах, проектных сессиях, научно-практических конференциях)": "академическая_мобильность",
    "17. Оцените, насколько Вы удовлетворены информационной наполненностью сайта Университета": "сайт",
    "18. Оцените, насколько Вы удовлетворены доступностью информации о дополнительных образовательных программах": "доп_программы",
    "19. Оцените, насколько Вы удовлетворены возможностью занятиями спортом в Университете": "организации_занятия_спортом",
    "20. Оцените, насколько Вы удовлетворены организацией занятий по физической культуре и спорту": "организация_занятий_физкультуры",
    "21. Оцените, насколько Вы удовлетворены требованиями и критериями оценки ваших достижений по физической культуре и спорту со стороны профессорско-преподавательского состава кафедры физического воспитания": "оценка_физкультура",
    "22. Оцените, насколько Вы удовлетворены организацией досуга в Университете": "досуг_в_университете",
    "23. Оцените, насколько Вы удовлетворены доступностью услуг размещения в общежитии": "услуги_общежития",
    "24. Оцените, насколько Вы удовлетворены безопасностью и охраной жизни в Университете": "безопасность_университета",
    "Укажите название образовательной программы / направленности / профиля / шифр и наименование научной специальности, по которой/му вы обучаетесь": "Шифр",
    "Ваши комментарии и предложения (по желанию):": "комментарии",
}


def rename_columns(df: DataFrame) -> DataFrame:
    df = df.rename(columns=rename_dict)
    return df

def rename_ciphers(ciphers: Series) -> Series:
    return ciphers.apply(lambda cipher: str(cipher).split()[0] if pd.notna(cipher) else cipher)
