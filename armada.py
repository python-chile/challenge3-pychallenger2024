from utils import decrypt_message, categorize_words, list_info

def test(n, f, tests, type_=None):
    success = failed = 0
    for inputs_, output_ in tests:
        try:
            if type_ == 'img':
                assert sum(r+g+b+a for r,g,b,a in ImageChops.difference(f(*inputs_), Image.open(output_)).getdata()) < 10
            else:
                assert f(*inputs_) == output_
            success += 1
        except AssertionError:
            failed += 1
    print(f"TEST {n}: {success} exitosos y {failed} erróneos")

tests1 = [
    (('InqfÉd.aa.Éa.É.ÑJaaHHÑaJÑdrJHHaÑíJ.tmaJaÉHíÑÑÉaÉHÑÑÉJhmfd.mHhdHÉ.qH.nJaHJJaJJaJÑÉHdkÑÉábsqÉÉhÉbnaaaHÉJJHaHaHÑÉÑbnm.íJHaÑíÑíHÉ.íHí24HÑú.aaÉÑíííJJHJJÉí.íÑÑííÑÑJ.H.ÑÑaLÑHÉíZHqHÉÉHéZJJdírí.aíÉJÑJííÉíÑ.HÑaHHbH.Éí.ÑZqchÉ.Ñí.ñkíí.íHHÉÑnHÉfZííJíaHJÉ.pHtÉ.Éíd.ÑJJÑÉJíJ.HÉJJHíÉJ..HíÉÑaJsíííÑhdHH..ÑÑímdJÉaaaaÑ3ÑÑH0aíÑaúaCÑ.ííZÉmhd.ÑkZ.HaJÑÉshdÉmí.dÉaHHÑJJí.JÑaHÑaJaÉa.í1..H.É4JÉHaÑíJ.íía.HÑHxJ.íÑíí.dHÉÉrJajhmÉdrhñ..kíHnHÉfZ.íú.aÑJÑ.JJÉJaaKtÉÉH.ÑhrJÉÉÑagÑZ...ÉJ.aJÉÑÑaJíí.aaÉíJíÑa.HÉbÉtÉ.ílíHokhHÉHcíí....HnÉíaí.HJa.ííÉHíH.ÑJÑíííHÑ08JÉíÑHíxJaÉíHadrÑíJHaÉHJÑ..tHÉH.HmJJÉaldÑbHÚ.mhíbínHú.JÑÑH.ÑÉíÑÑJHHaÑHJaJlÉhÉÉH.ÑHdmÑsHHíqÉÑÑÉ.HHZrJJJH.ÑaaHíÑÉÑÉÑJÑ..JptÉ.dJHÉE.H..íd.q.míZ.mícnJíHHÑ.JíÑÑJÉÑaaaÑaHA.íHíZÉH.qÑÉÑÑqdqÑZÑÑaaJÑJ.a.HJÑí.ÉÑaÉííÑ.aíaÑ.diíÑ.dqbÉdJaH.ÉíÉaaÉJcdJHÑííÑH.aJaÉÑaíHíaJ..íHíaíííbÉ.ííÑ.nbHhímdqnHÑJa.HHaJíJíÑaíxíHaaÉJíJHJsÉhíHdmíHd.aJHíaHíÉ1É3',),
        'Jorge es un ingeniero eléctrico con 35, María es cardióloga que tiene 41 , Daniela tiene 25 y es kinesióloga, Luis ha cumplido 19 y es un mecánico, mientras que Fernando Barrera ejerce de cocinero y tiene 24'),
    (('zzCZzzÍmhdkSúXSÍzÍllúSlXúlOzlÍOSúúzOOzlAXZqlqOdÍzqZSOSÍlúOÍlOSÍúúúXSúzlbnlOzmOÍúXlSSúlSÍXXlúSlOX1X2zSzlrdzXzXlOSlOOzlSúOOOXXzzOÍúSúXfqXZczózÍZSOXlÍSÍÍSSOúÍlllOzÍcÍdlÍOSSSlzSúXSSÍlXOzÍZzaXÍnÍXOfzzOzÍlOXlXXOzlÍZczXnl,zSOlzOSEdqzmzZzllmOcZXúSXzlzXÍúzXúXSúXúzOLáÍlzmcdyÍzlOÍXOOúzlzSOSsOqZlaZliZSúzXúlOOlÍSlúXzzÍúlclOÍdOXzSbglnelÍzdzqXXSXZOúlúSXúlúXúXXlÍúlXzXzllOÍÍOzOSXSOXXÍzÍrtrSúSlOúúXl2lzz0ÍO,lOlXSzXOSúÍúllXzXXÍzúIllOlÍtXZÍmúzSXSúlúXXSzKÍldOsOdÍÍOÍlkhOdzOXzqúuhÍXOÍlÍzOuzdSSúrhzdmclOzXzlOXÍnÍzÍúúOczOÍdrÍzZqzqXnXkOXzÍOXkÍzzZXcXXnXXqSOúOÍllúúxXúSSúshdXlmzdÍOÍzSzlú1OlXXlz.zOXzzOXX,',),
        'Daniel Barrera con 23 se gradúa de abogado. Fernanda Méndez trabaja de chofer a sus 31. Juan Letelier vive siendo desarrollador y tiene 20.')
]
tests2 = [
    (("Jorge es un ingeniero eléctrico con 35, María es cardióloga que tiene 41 , Daniela tiene 25 y es kinesióloga, Luis ha cumplido 19 y es un mecánico, mientras que Fernando Barrera ejerce de cocinero y tiene 24",),
        [
        ('Jorge', 'PROPN'),
        ('es', 'AUX'),
        ('un', 'DET'),
        ('ingeniero', 'NOUN'),
        ('eléctrico', 'ADJ'),
        ('con', 'ADP'),
        ('35', 'NUM'),
        (',', 'PUNCT'),
        ('María', 'PROPN'),
        ('es', 'AUX'),
        ('cardióloga', 'ADJ'),
        ('que', 'SCONJ'),
        ('tiene', 'VERB'),
        ('41', 'NUM'),
        (',', 'PUNCT'),
        ('Daniela', 'PROPN'),
        ('tiene', 'VERB'),
        ('25', 'NUM'),
        ('y', 'CCONJ'),
        ('es', 'AUX'),
        ('kinesióloga', 'ADJ'),
        (',', 'PUNCT'),
        ('Luis', 'PROPN'),
        ('ha', 'AUX'),
        ('cumplido', 'VERB'),
        ('19', 'NUM'),
        ('y', 'CCONJ'),
        ('es', 'AUX'),
        ('un', 'DET'),
        ('mecánico', 'NOUN'),
        (',', 'PUNCT'),
        ('mientras', 'CCONJ'),
        ('que', 'SCONJ'),
        ('Fernando', 'PROPN'),
        ('Barrera', 'PROPN'),
        ('ejerce', 'VERB'),
        ('de', 'ADP'),
        ('cocinero', 'NOUN'),
        ('y', 'CCONJ'),
        ('tiene', 'VERB'),
        ('24', 'NUM')]),
    (('Daniel Barrera con 23 se gradúa de abogado. Fernanda Méndez trabaja de chofer a sus 31. Juan Letelier vive siendo desarrollador y tiene 20.',),
        [('Daniel', 'PROPN'),
        ('Barrera', 'PROPN'),
        ('con', 'ADP'),
        ('23', 'NUM'),
        ('se', 'PRON'),
        ('gradúa', 'VERB'),
        ('de', 'ADP'),
        ('abogado', 'NOUN'),
        ('.', 'PUNCT'),
        ('Fernanda', 'PROPN'),
        ('Méndez', 'PROPN'),
        ('trabaja', 'VERB'),
        ('de', 'ADP'),
        ('chofer', 'NOUN'),
        ('a', 'ADP'),
        ('sus', 'PRON'),
        ('31', 'NUM'),
        ('.', 'PUNCT'),
        ('Juan', 'PROPN'),
        ('Letelier', 'PROPN'),
        ('vive', 'VERB'),
        ('siendo', 'AUX'),
        ('desarrollador', 'NOUN'),
        ('y', 'CCONJ'),
        ('tiene', 'VERB'),
        ('20', 'NUM'),
        ('.', 'PUNCT')])
]

tests3 = [
    (('InqfÉd.aa.Éa.É.ÑJaaHHÑaJÑdrJHHaÑíJ.tmaJaÉHíÑÑÉaÉHÑÑÉJhmfd.mHhdHÉ.qH.nJaHJJaJJaJÑÉHdkÑÉábsqÉÉhÉbnaaaHÉJJHaHaHÑÉÑbnm.íJHaÑíÑíHÉ.íHí24HÑú.aaÉÑíííJJHJJÉí.íÑÑííÑÑJ.H.ÑÑaLÑHÉíZHqHÉÉHéZJJdírí.aíÉJÑJííÉíÑ.HÑaHHbH.Éí.ÑZqchÉ.Ñí.ñkíí.íHHÉÑnHÉfZííJíaHJÉ.pHtÉ.Éíd.ÑJJÑÉJíJ.HÉJJHíÉJ..HíÉÑaJsíííÑhdHH..ÑÑímdJÉaaaaÑ3ÑÑH0aíÑaúaCÑ.ííZÉmhd.ÑkZ.HaJÑÉshdÉmí.dÉaHHÑJJí.JÑaHÑaJaÉa.í1..H.É4JÉHaÑíJ.íía.HÑHxJ.íÑíí.dHÉÉrJajhmÉdrhñ..kíHnHÉfZ.íú.aÑJÑ.JJÉJaaKtÉÉH.ÑhrJÉÉÑagÑZ...ÉJ.aJÉÑÑaJíí.aaÉíJíÑa.HÉbÉtÉ.ílíHokhHÉHcíí....HnÉíaí.HJa.ííÉHíH.ÑJÑíííHÑ08JÉíÑHíxJaÉíHadrÑíJHaÉHJÑ..tHÉH.HmJJÉaldÑbHÚ.mhíbínHú.JÑÑH.ÑÉíÑÑJHHaÑHJaJlÉhÉÉH.ÑHdmÑsHHíqÉÑÑÉ.HHZrJJJH.ÑaaHíÑÉÑÉÑJÑ..JptÉ.dJHÉE.H..íd.q.míZ.mícnJíHHÑ.JíÑÑJÉÑaaaÑaHA.íHíZÉH.qÑÉÑÑqdqÑZÑÑaaJÑJ.a.HJÑí.ÉÑaÉííÑ.aíaÑ.diíÑ.dqbÉdJaH.ÉíÉaaÉJcdJHÑííÑH.aJaÉÑaíHíaJ..íHíaíííbÉ.ííÑ.nbHhímdqnHÑJa.HHaJíJíÑaíxíHaaÉJíJHJsÉhíHdmíHd.aJHíaHíÉ1É3',),
    {
        'Jorge': {'profession': 'ingeniero eléctrico', 'age': '35'},
        'María': {'profession': 'cardióloga', 'age': '41'},
        'Daniela': {'profession': 'kinesióloga', 'age': '25'},
        'Luis': {'profession': 'mecánico', 'age': '19'},
        'Fernando Barrera': {'profession': 'cocinero', 'age': '24'}
        }),
    (('zzCZzzÍmhdkSúXSÍzÍllúSlXúlOzlÍOSúúzOOzlAXZqlqOdÍzqZSOSÍlúOÍlOSÍúúúXSúzlbnlOzmOÍúXlSSúlSÍXXlúSlOX1X2zSzlrdzXzXlOSlOOzlSúOOOXXzzOÍúSúXfqXZczózÍZSOXlÍSÍÍSSOúÍlllOzÍcÍdlÍOSSSlzSúXSSÍlXOzÍZzaXÍnÍXOfzzOzÍlOXlXXOzlÍZczXnl,zSOlzOSEdqzmzZzllmOcZXúSXzlzXÍúzXúXSúXúzOLáÍlzmcdyÍzlOÍXOOúzlzSOSsOqZlaZliZSúzXúlOOlÍSlúXzzÍúlclOÍdOXzSbglnelÍzdzqXXSXZOúlúSXúlúXúXXlÍúlXzXzllOÍÍOzOSXSOXXÍzÍrtrSúSlOúúXl2lzz0ÍO,lOlXSzXOSúÍúllXzXXÍzúIllOlÍtXZÍmúzSXSúlúXXSzKÍldOsOdÍÍOÍlkhOdzOXzqúuhÍXOÍlÍzOuzdSSúrhzdmclOzXzlOXÍnÍzÍúúOczOÍdrÍzZqzqXnXkOXzÍOXkÍzzZXcXXnXXqSOúOÍllúúxXúSSúshdXlmzdÍOÍzSzlú1OlXXlz.zOXzzOXX,',),
    {
    'Daniel Barrera': {'profession': 'abogado', 'age': '23'},
    'Fernanda Méndez': {'profession': 'chofer', 'age': '31'},
    'Juan Letelier': {'profession': 'desarrollador', 'age': '20'}
    })
]

test(1, decrypt_message, tests1)
test(2, categorize_words, tests2)
test(3, list_info, tests3)
