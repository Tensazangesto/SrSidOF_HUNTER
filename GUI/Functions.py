import googletrans as gt


def translate(e):
    if e.data == "transs":
        translator = gt.Translator()
        text = txtF_Entertxt.value
        language = dropdown_lang_select.value
        translation = translator.translate(text, dest=language).text
        txtF_Resualt_trans.value = translation
        page.update([txtF_Resualt_trans])


def clear(e):
    if e.data == "clear":
        page.update([txtF_Entertxt, txtF_Resualt_trans])
