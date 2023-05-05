def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[6]>18.423649285366366:
            # {"feature": "Alkaline_Phosphotase", "instances": 134, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 104, "metric_value": 0.0, "depth": 5}
               if obj[8]<=96.0396729401198:
                  # {"feature": "Direct_Bilirubin", "instances": 96, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 55, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=31.836363636363636:
                        # {"feature": "Alamine_Aminotransferase", "instances": 39, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=23.23076923076923:
                           return 'normal'
                        elif obj[4]>23.23076923076923:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>31.836363636363636:
                        # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[4]>20:
                           return 'liver'
                        elif obj[4]<=20:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 41, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=83.02439024390245:
                        # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=29:
                           return 'liver'
                        elif obj[1]>29:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>83.02439024390245:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=52:
                           return 'liver'
                        elif obj[1]>52:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>96.0396729401198:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[2]>4:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=24:
                           return 'normal'
                        elif obj[5]>24:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
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
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 30, "metric_value": 0.0, "depth": 5}
               if obj[1]<=217.84510684555033:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=55:
                        # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[4]>19:
                           return 'liver'
                        elif obj[4]<=19:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>55:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>217.84510684555033:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=18.423649285366366:
            # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 4}
            if obj[4]>23:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[8]>11:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]>25:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=11:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=25:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]<=23:
               # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>14:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=14:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[6]>47.559322033898304:
            # {"feature": "Direct_Bilirubin", "instances": 79, "metric_value": -0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 69, "metric_value": -0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Alkaline_Phosphotase", "instances": 65, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 44, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=160.1125953416966:
                        # {"feature": "Total_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=21.675675675675677:
                           return 'liver'
                        elif obj[1]>21.675675675675677:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>160.1125953416966:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 7}
                     if obj[1]>17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]>88:
                           return 'liver'
                        elif obj[4]<=88:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>10:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=10:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[8]<=8:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[1]>6:
                     return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'normal'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[8]>8:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>5:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=5:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[6]<=47.559322033898304:
            # {"feature": "Alkaline_Phosphotase", "instances": 39, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[2]<=13:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=13:
                     # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=28:
                        # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>28:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>13:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        return 'liver'
                     elif obj[4]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]>13:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[6]>60.3448275862069:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 86, "metric_value": -0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 69, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=174.1068790577985:
                     # {"feature": "Alamine_Aminotransferase", "instances": 67, "metric_value": -0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Direct_Bilirubin", "instances": 65, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=18:
                           return 'liver'
                        elif obj[2]>18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>174.1068790577985:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[5]>26:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[4]>26:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'normal'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=26:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=26:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=60.3448275862069:
               # {"feature": "Alamine_Aminotransferase", "instances": 30, "metric_value": 0.0, "depth": 5}
               if obj[4]>14:
                  # {"feature": "Direct_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[5]>16:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'liver'
                        elif obj[8]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=16:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[1]>11:
                        return 'liver'
                     elif obj[1]<=11:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]>8:
                           return 'liver'
                        elif obj[8]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=14:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[8]<=16:
               # {"feature": "Total_Protiens", "instances": 36, "metric_value": 0.0, "depth": 5}
               if obj[6]<=75:
                  # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=39:
                     # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": -0.0, "depth": 7}
                     if obj[4]>33:
                        # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=4:
                           return 'liver'
                        elif obj[2]>4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=33:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>39:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>75:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=24:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>24:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>16:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 70, "metric_value": -0.0, "depth": 4}
            if obj[6]>19.155279749709432:
               # {"feature": "Alamine_Aminotransferase", "instances": 51, "metric_value": 0.0, "depth": 5}
               if obj[4]>11:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 50, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=64:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 45, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=68.08888888888889:
                        # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=68:
                           return 'liver'
                        elif obj[1]>68:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>68.08888888888889:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[1]>15:
                           return 'liver'
                        elif obj[1]<=15:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>64:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>28:
                           return 'liver'
                        elif obj[5]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=11:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=19.155279749709432:
               # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[5]<=32:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>1:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>32:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=6:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>29:
                           return 'liver'
                        elif obj[4]<=29:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>6:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>6:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": -0.0, "depth": 4}
            if obj[8]<=7:
               # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[4]>30:
                  # {"feature": "Total_Protiens", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[6]>8:
                     return 'liver'
                  elif obj[6]<=8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>48:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>15:
                           return 'liver'
                        elif obj[1]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=48:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=30:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>39:
                           return 'normal'
                        elif obj[5]<=39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=21:
                           return 'normal'
                        elif obj[5]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]<=9:
                     # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'liver'
            elif obj[8]>7:
               # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[1]<=25:
                  return 'liver'
               elif obj[1]>25:
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
