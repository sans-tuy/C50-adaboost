def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Total_Protiens", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[6]>61.73856209150327:
         # {"feature": "Age", "instances": 227, "metric_value": 0.0, "depth": 3}
         if obj[0]<=42.25991189427313:
            # {"feature": "Alkaline_Phosphotase", "instances": 115, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 82, "metric_value": 0.0, "depth": 5}
               if obj[4]<=61.24390243902439:
                  # {"feature": "Total_Bilirubin", "instances": 68, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=12:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 55, "metric_value": -0.0, "depth": 7}
                     if obj[8]>9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 36, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=35.416666666666664:
                           return 'normal'
                        elif obj[5]>35.416666666666664:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>12:
                     # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=34:
                           return 'liver'
                        elif obj[5]>34:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>27:
                           return 'liver'
                        elif obj[5]<=27:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>61.24390243902439:
                  # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[1]<=13:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=133:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[5]>58:
                           return 'liver'
                        elif obj[5]<=58:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>133:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=23:
                           return 'liver'
                        elif obj[5]>23:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=28:
                           return 'normal'
                        elif obj[4]>28:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>13:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]>8:
                           return 'liver'
                        elif obj[2]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]>42.25991189427313:
            # {"feature": "Alkaline_Phosphotase", "instances": 112, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 85, "metric_value": 0.0, "depth": 5}
               if obj[1]<=41.39001842471912:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 80, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=45.05:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 57, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 43, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=24.58139534883721:
                           return 'liver'
                        elif obj[4]>24.58139534883721:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>45.05:
                     # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28.84756423765451:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=13:
                           return 'liver'
                        elif obj[8]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28.84756423765451:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>41.39001842471912:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[1]>6:
                  # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 6}
                  if obj[2]>3:
                     return 'liver'
                  elif obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=6:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[6]<=61.73856209150327:
         # {"feature": "Total_Bilirubin", "instances": 79, "metric_value": -0.0, "depth": 3}
         if obj[1]<=21.658227848101266:
            # {"feature": "Age", "instances": 62, "metric_value": 0.0, "depth": 4}
            if obj[0]>46.58064516129032:
               # {"feature": "Direct_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=87:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]>13:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=44:
                           return 'liver'
                        elif obj[5]>44:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=13:
                        # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>87:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>17:
                           return 'liver'
                        elif obj[4]<=17:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[8]>11:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[5]>25:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]>48:
                           return 'liver'
                        elif obj[4]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=25:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=11:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=46.58064516129032:
               # {"feature": "Aspartate_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 5}
               if obj[5]<=85.51724137931035:
                  # {"feature": "Alkaline_Phosphotase", "instances": 23, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]>85.51724137931035:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]>33:
                     return 'liver'
                  elif obj[4]<=33:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[1]>21.658227848101266:
            # {"feature": "Age", "instances": 17, "metric_value": 0.0, "depth": 4}
            if obj[0]<=46:
               # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[2]<=42:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[4]>50:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>140:
                           return 'liver'
                        elif obj[5]<=140:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=50:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>42:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]>46:
               # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  return 'liver'
               elif obj[2]<=1:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Total_Bilirubin", "instances": 151, "metric_value": 0.0, "depth": 3}
         if obj[1]>1:
            # {"feature": "Total_Protiens", "instances": 146, "metric_value": 0.0, "depth": 4}
            if obj[6]>21.367585172257165:
               # {"feature": "Age", "instances": 111, "metric_value": -0.0, "depth": 5}
               if obj[0]<=45.612612612612615:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 61, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=76:
                     # {"feature": "Direct_Bilirubin", "instances": 58, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=41:
                        # {"feature": "Alamine_Aminotransferase", "instances": 49, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=46.857142857142854:
                           return 'liver'
                        elif obj[4]>46.857142857142854:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>41:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>76:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>29:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=29:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[0]>45.612612612612615:
                  # {"feature": "Alamine_Aminotransferase", "instances": 50, "metric_value": 0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 49, "metric_value": 0.0, "depth": 7}
                     if obj[8]>4:
                        # {"feature": "Direct_Bilirubin", "instances": 40, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=11:
                           return 'liver'
                        elif obj[2]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]<=21.367585172257165:
               # {"feature": "Aspartate_Aminotransferase", "instances": 35, "metric_value": 0.0, "depth": 5}
               if obj[5]<=105.54285714285714:
                  # {"feature": "Age", "instances": 31, "metric_value": 0.0, "depth": 6}
                  if obj[0]<=71.64663104208394:
                     # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=26:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=8:
                           return 'liver'
                        elif obj[2]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>26:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=5:
                           return 'liver'
                        elif obj[8]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]>71.64663104208394:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>105.54285714285714:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[1]<=1:
            # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 4}
            if obj[4]>22:
               # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[5]>13:
                  return 'liver'
               elif obj[5]<=13:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[4]<=22:
               return 'normal'
            else:
               return 'normal'
         else:
            return 'normal'
      elif obj[3]>291.0539499036609:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 62, "metric_value": 0.0, "depth": 3}
         if obj[8]<=35:
            # {"feature": "Age", "instances": 55, "metric_value": -0.0, "depth": 4}
            if obj[0]>45.81818181818182:
               # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 5}
               if obj[1]>7:
                  # {"feature": "Direct_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": 0.0, "depth": 7}
                     if obj[4]>16:
                        # {"feature": "Total_Protiens", "instances": 26, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=55:
                           return 'liver'
                        elif obj[6]>55:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=7:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[0]<=45.81818181818182:
               # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 5}
               if obj[2]<=82:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[4]>38:
                        # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[6]>6:
                           return 'liver'
                        elif obj[6]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=38:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[5]>21:
                           return 'liver'
                        elif obj[5]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>82:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>35:
            # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 4}
            if obj[4]>30:
               # {"feature": "Age", "instances": 4, "metric_value": -0.0, "depth": 5}
               if obj[0]>50:
                  return 'liver'
               elif obj[0]<=50:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": -0.0, "depth": 6}
                  if obj[1]>3:
                     return 'normal'
                  elif obj[1]<=3:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[4]<=30:
               # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[1]>5:
                  return 'liver'
               elif obj[1]<=5:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
