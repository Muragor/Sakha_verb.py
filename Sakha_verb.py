class Verb:
    '''Переменная а обозначает число. 1 - единственное, 2 - множественное
    А переменная b показывает лицо (1, 2, 3). Переменная v показывает глагол'''
    dict_for_garmony1 = {1: 'и', 2: 'ы', 3: "у", 4: "у", 5: "ү", 6: "ү"}
    dict_for_garmony2 = {1: 'э', 2: 'а', 3: "а", 4: "о", 5: "э", 6: "ө"}
    @staticmethod
    def Garmony_of_sl(v, n):
        if v[-n].lower() == 'и' or v[-n].lower() == 'э':
            return 1
        if v[-n].lower() == 'ы' or v[-n].lower() == 'а':
            return 2
        if v[-n].lower() == 'у':
            return 3
        if v[-n].lower() == 'о':
            try:
                if v[-(n+1)].lower() == 'у':
                    return 3
                else:
                    return 4
            except:
                return 4
        if v[-n].lower() == 'ү':
            return 5
        if v[-n].lower() == 'ө':
            try:
                if v[-(n+1)].lower() == 'ү':
                    return 5
                else:
                    return 6
            except:
                return 6

    @classmethod
    def Garmony(cls, v):

       if v[-1].lower() in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
           if v[-2] == v[-1]:
               try:
                   c1 = Verb.Garmony_of_sl(v, 4)
               except:
                   try:
                       c1 = Verb.Garmony_of_sl(v, 5)
                   except:
                       c1 = Verb.Garmony_of_sl(v, 2)
               return c1
           if v[-1].lower() in ('э', "а", "о", "ө") and v[-2].lower() in ("ы", "у", "и", "ү"):
               return Verb.Garmony_of_sl(v, 2)
           if v[-2] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү') and v[-2] != v[-1]:
               return Verb.Garmony_of_sl(v, 2)
           else:
               return Verb.Garmony_of_sl(v, 1)
       else:
           for i in range(1, len(v)+1):
               if v[-i].lower() in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                   return Verb.Garmony_of_sl(v, i)
    @staticmethod
    def check_for_irregular_verbs(v):
        if v.lower() == 'ыарый':
            return "ыалдь"
        if v.lower() == "сырыт":
            return "сылдь"
        if v.lower() == "уһул":
            return "уст"
        v_new = v
        try:
           if v[-1] == 'с' and v[-2] in ("ы", "у", "и", "ү") and v[-3] in ("р", "й", "л"):
               return v[0:len(v)-2]+v[-1]
           elif v[-1] == 'с' and v[-2] in ("ы", "у", "и", "ү") and v[-3] == 'ҕ':
               v_new = v[0:len(v) - 2] + v[-1]
               for i in v_new:
                   if i == "ҕ":
                       v_new = v_new[0:v_new.find("ҕ")] + "х" + v_new[v_new.find("ҕ") + 1:len(v_new)]
               return v_new
           if v[-1] == 'н' and v[-2] in ("ы", "у", "и", "ү") and v[-3] == "ҥ": #("ҥ", "т", "л", "г", "һ"):
               v_new = v[0:len(v) - 2] + v[-1]
               return v_new
           if v[-1] == 'н' and v[-2] in ("ы", "у", "и", "ү") and v[-3] == "н": #("ҥ", "т", "л", "г", "һ"):
               v_new = v[0:len(v) - 2] + v[-1]
               return v_new
           if v[-1] == 'н' and v[-2] in ("ы", "у", "и", "ү") and v[-3] == "т": #("ҥ", "т", "л", "г", "һ"):
               v_new = v[0:len(v) - 2] + "т"
           if v[-1] == 'н' and v[-2] in ("ы", "у", "и", "ү") and v[-3] == "л": #("ҥ", "т", "л", "г", "һ"):
               v_new = v[0:len(v) - 2] + "л"
           if v[-1] == 'н' and v[-2] in ("ы", "у", "и", "ү") and v[-3] == "г": #("ҥ", "т", "л", "г", "һ"):
               v_new = v[0:len(v) - 2] + "т"
               for i in v_new:
                   if i == "г":
                       v_new = v_new[0:v_new.find("г")] + "к" + v_new[v_new.find("г") + 1:len(v_new)]
           if v[-1] == 'н' and v[-2] in ("ы", "у", "и", "ү") and v[-3] == "һ":
               v_new = v[0:len(v) - 2] + "т"
               for i in v_new:
                   if i == "һ":
                       v_new = v_new[0:v_new.find("һ")] + "с" + v_new[v_new.find("һ") + 1:len(v_new)]
           return v_new
        except:
            return(v)


    @staticmethod
    def lico(a, b, v):
        c1 = Verb.dict_for_garmony1[Verb.Garmony(v)]
        c2 = Verb.dict_for_garmony2[Verb.Garmony(v)]
        if a == 1:
            if b == 1:
                if v[-1] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                    return v+'м'
                else:
                    return v+f'{c1}м'
            if b == 2:
                if v[-1] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                    return v + 'ҥ'
                else:
                    return v+f'{c1}ҥ'
            if b == 3:
                if v[-1] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                    return v
                else:
                   return v+f'{c2}'
        if a == 2:
            if b == 1:
                return v+f'б{c1}т'
            if b == 2:
                return v+f'ҕ{c1}т'
            if b == 3:
                return v+f'л{c2}р{c2}'
    @staticmethod
    def upod_sogl_sl(v_time, d1, v_time_lico, d2, zamena):
        c1 = v_time_lico[len(v_time)::]
        try:
            if v_time[-1] == d1 and c1[0] == d2:
                if len(zamena) > 1:
                    return v_time[0:len(v_time)-1] + zamena + c1[1:len(c1)]
                else:
                    return v_time+zamena+c1[1:len(c1)]
            else:

                return 0
        except:
            return 0
    @staticmethod
    def upod_sogl_of_verb_and_verb_time(v, v_time):
        c3 = v_time[len(v)::]
        if Verb.upod_sogl_sl(v, "т", v_time, "б", 'пп') != 0:
            if v[-2] == 'р' or v[-2] == 'л':
                return v[0:len(v) - 1] + "д" + Verb.dict_for_garmony1[Verb.Garmony(v)] + c3
            return Verb.upod_sogl_sl(v, "т", v_time, "б", 'пп')
        elif Verb.upod_sogl_sl(v, "н", v_time, "б", 'мм') != 0:
            return Verb.upod_sogl_sl(v, "н", v_time, "б", 'мм')
        elif Verb.upod_sogl_sl(v, "м", v_time, "б", 'м') != 0:
            return Verb.upod_sogl_sl(v, "м", v_time, "б", 'м')
        elif Verb.upod_sogl_sl(v, "ҥ", v_time, "б", 'м') != 0:
            return Verb.upod_sogl_sl(v, "ҥ", v_time, "б", 'м')
        elif Verb.upod_sogl_sl(v, "х", v_time, "б", 'п') != 0:
            return Verb.upod_sogl_sl(v, "х", v_time, "б", 'п')
        elif Verb.upod_sogl_sl(v, "п", v_time, "б", 'п') != 0:
            return Verb.upod_sogl_sl(v, "п", v_time, "б", 'п')
        elif Verb.upod_sogl_sl(v, "с", v_time, "б", 'п') != 0:
            return Verb.upod_sogl_sl(v, "с", v_time, "б", 'п')
        elif Verb.upod_sogl_sl(v, "к", v_time, "б", 'п') != 0:
            return Verb.upod_sogl_sl(v, "к", v_time, "б", 'п')
        elif Verb.upod_sogl_sl(v, "л", v_time, "т", 'л') != 0:
            return Verb.upod_sogl_sl(v, "л", v_time, "т", 'л')
        elif Verb.upod_sogl_sl(v, "й", v_time, "т", 'д') != 0:
            return Verb.upod_sogl_sl(v, "й", v_time, "т", 'д')
        elif Verb.upod_sogl_sl(v, "р", v_time, "т", 'д') != 0:
            return Verb.upod_sogl_sl(v, "р", v_time, "т", 'д')
        elif Verb.upod_sogl_sl(v, "н", v_time, "т", 'н') != 0:
            return Verb.upod_sogl_sl(v, "н", v_time, "т", 'н')
        #гласные с согласными
        c1 = v_time.replace(v, '')
        c2 = c1[0]
        if c2 in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
            if Verb.upod_sogl_sl(v, "х", v_time, c2, 'ҕ') != 0:
                return v_time[0:len(v) - 1] + 'ҕ' + c1
            if Verb.upod_sogl_sl(v, "с", v_time, c2, 'һ') != 0:
                if v[len(v)-2] in ("р", "й", "х", "л"):
                    return v_time
                else:
                    return v_time[0:len(v) - 1] + 'һ' + c1
            if Verb.upod_sogl_sl(v, "п", v_time, c2, 'б') != 0:
                return v_time[0:len(v) - 1] + 'б' + c1
            if Verb.upod_sogl_sl(v, "к", v_time, c2, 'г') != 0:
                return v_time[0:len(v) - 1] + 'г' + c1
            if v[-2] == 'р' and v[-1] == 'т':
                return v[0:len(v) - 1] + 'д' + c1
            if v[-2] == 'л' and v[-1] == 'т':
                return v[0:len(v) - 1] + 'дь' + c1
            else:
                return v_time
        else:
            return v_time


    @staticmethod
    def upod_sogl_of_verb_time_and_lic(v_time, v_time_lico):
          if Verb.upod_sogl_sl(v_time, "т", v_time_lico, "б", 'пп') != 0:
              return Verb.upod_sogl_sl(v_time, "т", v_time_lico, "б", 'пп')
          elif Verb.upod_sogl_sl(v_time, "т", v_time_lico, "ҕ", 'кк') != 0:
              return Verb.upod_sogl_sl(v_time, "т", v_time_lico, "ҕ", 'кк')
          elif Verb.upod_sogl_sl(v_time, "т", v_time_lico, "л", 'т') != 0:
              return Verb.upod_sogl_sl(v_time, "т", v_time_lico, "л", 'т')

          elif Verb.upod_sogl_sl(v_time, "х", v_time_lico, "ҕ", 'х') != 0:
              return Verb.upod_sogl_sl(v_time, "х", v_time_lico, "ҕ", 'х')
          elif Verb.upod_sogl_sl(v_time, "х", v_time_lico, "б", 'п') != 0:
              return Verb.upod_sogl_sl(v_time, "х", v_time_lico, "б", 'п')
          elif Verb.upod_sogl_sl(v_time, "х", v_time_lico, "л", 'т') != 0:
              return Verb.upod_sogl_sl(v_time, "х", v_time_lico, "л", 'т')

          c1 = v_time[-1]
          if c1 in ("ы", "у", "и", "ү"):
              if Verb.upod_sogl_sl(v_time, c1, v_time_lico, "ҕ", 'г') != 0:
                  return Verb.upod_sogl_sl(v_time, c1, v_time_lico, "ҕ", 'г')
          else:
              return v_time_lico
    def past_time(self, v, a, b):
        if Verb.check_for_irregular_verbs(v) != v:
            v = Verb.check_for_irregular_verbs(v)+v[-2]
        else:
            v = Verb.check_for_irregular_verbs(v)
        for i in range(1, len(v)+1):
            if v[-i].lower() in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                c = Verb.Garmony_of_sl(v[-i], 0)
                break
        g = Verb.dict_for_garmony1[c]
        v_past = v + f'б{g}т'
        #здесь проблема
        v_time = Verb.upod_sogl_of_verb_and_verb_time(v, v_past)
        ################
        v_lico = Verb.lico(a, b, v_time)
        return Verb.upod_sogl_of_verb_time_and_lic(v_time ,v_lico)
    def future_time(self, v, a , b):
        v= Verb.check_for_irregular_verbs(v)
        c = Verb.Garmony(v)
        g1 = Verb.dict_for_garmony1[c]
        if g1 == 'ы':
            g2 = "а"
        elif g1 == 'у':
            g2 = 'о'
        elif g1 == 'и':
            g2 = 'э'
        elif g1 == 'ү':
            g2 = 'ө'
        g3 = g1+g2
        if a == 1:
            if v[-1] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                if v[-2] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                   if v[-1] in ('э', "а", "о", "ө") and v[-2] in ("ы", "у", "и", "ү"):
                        g3= g3+'х'
                        v_future = Verb.lico(1, b, v[0:len(v)-2] + g3)
                        return Verb.upod_sogl_of_verb_and_verb_time(v[0:len(v)-2] + g3, Verb.upod_sogl_of_verb_and_verb_time(v, v_future))
                   else:
                       v_future = Verb.lico(1, b, v[0:len(v) - 2] + g3)
                       return Verb.upod_sogl_of_verb_and_verb_time(v, v_future)
                else:
                    v_future = Verb.lico(1, b, v[0:len(v) - 1] + g3)
                    return Verb.upod_sogl_of_verb_and_verb_time(v, v_future)

            else:
                v_future = Verb.lico(1, b, v + g3)
                return Verb.upod_sogl_of_verb_and_verb_time(v, v_future)
        else:
            if v[-1] not in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                v_future = v+g3+'х'
            else:
                if v[-2] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                    v_future = v[0:len(v)-2] + g3 + "х"
                else:
                    v_future = v[0:len(v)-1] + g3 + "х"
            v_future1 = Verb.upod_sogl_of_verb_and_verb_time(v, v_future)
            v_future_lico = Verb.lico(2, b, v_future1)
            return Verb.upod_sogl_of_verb_time_and_lic(v_future1, v_future_lico)
    def real_time(self, v, a, b):
        v = Verb.check_for_irregular_verbs(v)
        c1 = Verb.dict_for_garmony2[Verb.Garmony(v)]
        c2 = Verb.dict_for_garmony1[Verb.Garmony(v)]
        if v[-1] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
            if v[-2] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                v_deep1 = v[0:len(v)-2] + c2+c2
            else:
                v_deep1 = v[0:len(v) - 1] + c2 + c2
        else:
            v_deep1 = v + c1
        v_deep = Verb.upod_sogl_of_verb_and_verb_time(v, v_deep1)
        c3 = Verb.dict_for_garmony1[Verb.Garmony(v_deep)]
        c4 = Verb.dict_for_garmony2[Verb.Garmony(v_deep)]
        if a == 1:
            if b == 1:
               return v_deep+f'б{c3}н'
            if b == 2:
                if Verb.upod_sogl_of_verb_time_and_lic(v_deep, v_deep+f'ҕ{c3}н') != 0:
                    return Verb.upod_sogl_of_verb_time_and_lic(v_deep, v_deep+f'ҕ{c3}н')
                else:
                    return v_deep+f'ҕ{c3}н'
            if b == 3:
               return v_deep+f'р'
        else:
            if b == 1:
                return Verb.lico(2, b, v_deep)
            if b == 2:
                return Verb.upod_sogl_of_verb_time_and_lic(v_deep, Verb.lico(2, b, v_deep))
            if b == 3:
                return v_deep+f"лл{c4}р"

    def verb_recent_past(self, v, a, b):
        v = Verb.upod_sogl_of_verb_and_verb_time(v, v+'т')
        if a == 1:
            return Verb.lico(a, b, v)
        else:
            c = Verb.dict_for_garmony1[Verb.Garmony(v)]
            c1 = Verb.dict_for_garmony2[Verb.Garmony(v)]
            if b == 1:
                v = v+f"{c}б{c}т"
            if b == 2:
                v = v + f"{c}г{c}т"
            if b == 3:
                v = v + f"{c}л{c1}р"
            return v
    def verb_not_finished_yet_time(self, v, a, b):
        v = Verb.check_for_irregular_verbs(v)
        c1 = Verb.dict_for_garmony2[Verb.Garmony(v)]
        c2 = Verb.dict_for_garmony1[Verb.Garmony(v)]
        if v[-1] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
            if v[-2] in ('а', 'ы', 'о', 'у', 'э', 'и', 'ө', 'ү'):
                v_deep1 = v[0:len(v) - 2] + c2 + c2
            else:
                v_deep1 = v[0:len(v) - 1] + c2 + c2
        else:
            v_deep1 = v + c1
        v_deep = Verb.upod_sogl_of_verb_and_verb_time(v, v_deep1)
        if a == 1:
            if b == 1:
                return v_deep + " иликпин"
            if b == 2:
                return v_deep + " иликкин"
            if b == 3:
                return v_deep + " илик"
        else:
            if b == 1:
                return v_deep + " иликпит"
            if b == 2:
                return v_deep + " иликкит"
            if b == 3:
                return v_deep + " иликтэр"
    def verb_finnaly(self, v, t, a, b):
       if t == '1':
           return self.future_time(v, a, b)
       if t == '3':
           return self.past_time(v, a, b)
       if t == '2':
           return self.real_time(v, a, b)
       if t == '4':
           return self.verb_recent_past(v, a, b)
       if t == '5':
           return self.verb_not_finished_yet_time(v, a, b)